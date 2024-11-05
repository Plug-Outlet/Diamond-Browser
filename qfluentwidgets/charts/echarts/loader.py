import os
from collections import abc

from jinja2.loaders import BaseLoader, split_template_path
from jinja2.exceptions import TemplateNotFound

from qtpy.QtCore import QDir, QDirIterator, QFile, QFileInfo, QIODevice, QFileDevice


class QFileSystemLoader(BaseLoader):
    """ File loader for qt file system """

    def __init__(self, searchpath, encoding="utf-8", followlinks=False):
        if not isinstance(searchpath, abc.Iterable) or isinstance(searchpath, str):
            searchpath = [searchpath]

        self.searchpath = list(searchpath)
        self.encoding = encoding
        self.followlinks = followlinks

    def get_source(self, environment, template):
        pieces = split_template_path(template)
        for searchpath in self.searchpath:
            filename = os.path.join(searchpath, *pieces)

            f = QFile(filename)
            if not f.exists():
                continue
            if not f.open(QIODevice.OpenModeFlag.ReadOnly):
                continue
            contents = f.readAll().data().decode(self.encoding)
            f.close()

            dt = QFileInfo(f).lastModified()

            def uptodate():
                return QFileInfo(filename).lastModified() == dt

            return contents, filename, uptodate

        raise TemplateNotFound(template)

    def list_templates(self):
        found = set()
        for searchpath in self.searchpath:
            d = QDir(searchpath)
            it_flag = QDirIterator.IteratorFlag.Subdirectories
            if self.followlinks:
                it_flag |= QDirIterator.IteratorFlag.FollowSymlinks

            it_filter = QDir.Filter.Files | QDir.Filter.NoDotAndDotDot | QDir.Filter.Hidden | QDir.Filter.Readable
            if not self.followlinks:
                it_filter |= QDir.Filter.NoSymLinks

            it = QDirIterator(searchpath, it_filter, it_flag)
            while it.hasNext():
                it.next()
                found.add(d.relativeFilePath(it.filePath()))

        return sorted(found)