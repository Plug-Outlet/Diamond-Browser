# coding: utf-8
from qtpy.QtWidgets import QWidget
from qtpy.QtDesigner import (QPyDesignerCustomWidgetPlugin, QDesignerFormWindowInterface, QExtensionFactory,
                              QPyDesignerContainerExtension)

from qfluentwidgets import (ScrollArea, SmoothScrollArea, SingleDirectionScrollArea, OpacityAniStackedWidget,
                            PopUpAniStackedWidget, CardWidget, ElevatedCardWidget, SimpleCardWidget,
                            HeaderCardWidget, InfoBarIcon)
from qfluentwidgetspro import (DropSingleFileWidget, DropMultiFilesWidget, ToolBox, Splitter, TimeLineWidget,
                               TimeLineCard, SlideAniStackedWidget, DropMultiFoldersWidget, DropSingleFolderWidget)

from plugin_base import PluginBase


class ContainerPlugin(PluginBase):

    def group(self):
        return super().group() + ' (Container)'

    def isContainer(self):
        return True


class ProContainerPlugin(ContainerPlugin):

    def includeFile(self):
        return "qfluentwidgetspro"


class CardWidgetPlugin(ContainerPlugin, QPyDesignerCustomWidgetPlugin):
    """ Card widget plugin """

    def createWidget(self, parent):
        return CardWidget(parent)

    def icon(self):
        return super().icon("CommandBar")

    def name(self):
        return "CardWidget"


class DropSingleFileWidgetPlugin(ProContainerPlugin, QPyDesignerCustomWidgetPlugin):
    """ Card widget plugin """

    def createWidget(self, parent):
        return DropSingleFileWidget(parent)

    def icon(self):
        return super().icon("AnimatedIcon")

    def name(self):
        return "DropSingleFileWidget"


class DropMultiFileWidgetPlugin(ProContainerPlugin, QPyDesignerCustomWidgetPlugin):
    """ Card widget plugin """

    def createWidget(self, parent):
        return DropMultiFilesWidget(parent)

    def icon(self):
        return super().icon("AnimatedIcon")

    def name(self):
        return "DropMultiFilesWidget"


class DropSingleFolderWidgetPlugin(ProContainerPlugin, QPyDesignerCustomWidgetPlugin):
    """ Card widget plugin """

    def createWidget(self, parent):
        return DropSingleFolderWidget(parent)

    def icon(self):
        return super().icon("AnimatedIcon")

    def name(self):
        return "DropSingleFolderWidget"


class DropMultiFolderWidgetPlugin(ProContainerPlugin, QPyDesignerCustomWidgetPlugin):
    """ Card widget plugin """

    def createWidget(self, parent):
        return DropMultiFoldersWidget(parent)

    def icon(self):
        return super().icon("AnimatedIcon")

    def name(self):
        return "DropMultiFoldersWidget"


class ElevatedCardWidgetPlugin(ContainerPlugin, QPyDesignerCustomWidgetPlugin):
    """ Elevated card widget plugin """

    def createWidget(self, parent):
        return ElevatedCardWidget(parent)

    def icon(self):
        return super().icon("CommandBar")

    def name(self):
        return "ElevatedCardWidget"


class SimpleCardWidgetPlugin(ContainerPlugin, QPyDesignerCustomWidgetPlugin):
    """ Simple card widget plugin """

    def createWidget(self, parent):
        return SimpleCardWidget(parent)

    def icon(self):
        return super().icon("CommandBar")

    def name(self):
        return "SimpleCardWidget"


class HeaderCardWidgetPlugin(ContainerPlugin, QPyDesignerCustomWidgetPlugin):
    """ Header card widget plugin """

    def createWidget(self, parent):
        return HeaderCardWidget(parent)

    def icon(self):
        return super().icon("CommandBar")

    def name(self):
        return "HeaderCardWidget"


class TimeLineWidgetPlugin(ProContainerPlugin, QPyDesignerCustomWidgetPlugin):
    """ Header card widget plugin """

    def createWidget(self, parent):
        w = TimeLineWidget(parent)
        w.addItem(InfoBarIcon.SUCCESS, "已完成", [TimeLineCard("上传我家 aiko 的 MV『シアワセ』", parent, InfoBarIcon.WARNING)])
        return w

    def icon(self):
        return super().icon("ListView")

    def name(self):
        return "TimeLineWidget"


class ToolBoxPlugin(ProContainerPlugin, QPyDesignerCustomWidgetPlugin):
    """ Header card widget plugin """

    def createWidget(self, parent):
        w = ToolBox(parent)
        w.addItem(QWidget(), "Tool Box")
        return w

    def icon(self):
        return super().icon("ComboBox")

    def name(self):
        return "ToolBox"


class SplitterPlugin(ProContainerPlugin, QPyDesignerCustomWidgetPlugin):
    """ Header card widget plugin """

    def createWidget(self, parent):
        return Splitter(parent)

    def icon(self):
        return super().icon("Line")

    def name(self):
        return "Splitter"


class ScrollAreaPluginBase(ContainerPlugin):
    """ Scroll area plugin base """

    def domXml(self):
        return f"""
            <widget class="{self.name()}" name="{self.name()}">
                <property name="widgetResizable">
                    <bool>true</bool>
                </property>
                <widget class="QWidget" name="scrollAreaWidgetContents" />
            </widget>
        """


class ScrollAreaPlugin(ScrollAreaPluginBase, QPyDesignerCustomWidgetPlugin):
    """ Scroll area plugin """

    def createWidget(self, parent):
        return ScrollArea(parent)

    def icon(self):
        return super().icon("ScrollViewer")

    def name(self):
        return "ScrollArea"

    def toolTip(self):
        return "Smooth scroll area"


class SmoothScrollAreaPlugin(ScrollAreaPluginBase, QPyDesignerCustomWidgetPlugin):
    """ Smooth scroll area plugin """

    def createWidget(self, parent):
        return SmoothScrollArea(parent)

    def icon(self):
        return super().icon("ScrollViewer")

    def name(self):
        return "SmoothScrollArea"


class SingleDirectionScrollAreaPlugin(ScrollAreaPluginBase, QPyDesignerCustomWidgetPlugin):
    """ Single direction scroll area plugin """

    def createWidget(self, parent):
        return SingleDirectionScrollArea(parent)

    def icon(self):
        return super().icon("ScrollViewer")

    def name(self):
        return "SingleDirectionScrollArea"


class StackedWidgetPlugin(ContainerPlugin):

    def domXml(self):
        return f"""
            <widget class="{self.name()}" name="{self.name()}">'
                <widget class="QWidget" name="page" />'
            </widget>
        """

    def onCurrentIndexChanged(self, index):
        widget = self.sender()
        form = QDesignerFormWindowInterface.findFormWindow(widget)
        if form:
            form.emitSelectionChanged()


class StackedWidgetExtension(QPyDesignerContainerExtension):
    """ Stacked widget extension """

    def __init__(self, stacked, parent=None) -> None:
        super().__init__(parent)
        self.stacked = stacked

    def addWidget(self, widget) -> None:
        self.stacked.addWidget(widget)

    def count(self):
        return self.stacked.count()

    def currentIndex(self):
        return self.stacked.currentIndex()

    def insertWidget(self, index, widget):
        self.stacked.insertWidget(index, widget)

    def remove(self, index):
        self.stacked.removeWidget(self.stacked.widget(index))

    def setCurrentIndex(self, index):
        self.stacked.setCurrentIndex(index)

    def widget(self, index):
        return self.stacked.widget(index)


class StackedWidgetExtensionFactory(QExtensionFactory):
    """ Stacked widget extension factory """

    widgets = []
    IID = "org.qt-project.Qt.Designer.Container"

    def createExtension(self, object, iid, parent):
        if iid != StackedWidgetExtensionFactory.IID:
            return None

        if object.__class__.__name__ not in self.widgets:
            return None

        return StackedWidgetExtension(object, parent)

    @classmethod
    def register(cls, Plugin):
        if Plugin.__name__ not in cls.widgets:
            cls.widgets.append(Plugin().name())
            Plugin.Factory = cls

        return Plugin


@StackedWidgetExtensionFactory.register
class OpacityAniStackedWidgetPlugin(StackedWidgetPlugin, QPyDesignerCustomWidgetPlugin):
    """ opacity ani stacked widget plugin """

    def createWidget(self, parent):
        w = OpacityAniStackedWidget(parent)
        w.currentChanged.connect(self.onCurrentIndexChanged)
        return w

    def icon(self):
        return super().icon("StackPanel")

    def name(self):
        return "OpacityAniStackedWidget"


@StackedWidgetExtensionFactory.register
class PopUpAniStackedWidgetPlugin(StackedWidgetPlugin, QPyDesignerCustomWidgetPlugin):
    """ pop up ani stacked widget plugin """

    def createWidget(self, parent):
        w = PopUpAniStackedWidget(parent)
        w.currentChanged.connect(self.onCurrentIndexChanged)
        return w

    def icon(self):
        return super().icon("StackPanel")

    def name(self):
        return "PopUpAniStackedWidget"


@StackedWidgetExtensionFactory.register
class SlideAniStackedWidgetPlugin(StackedWidgetPlugin, QPyDesignerCustomWidgetPlugin):
    """ pop up ani stacked widget plugin """

    def createWidget(self, parent):
        w = SlideAniStackedWidget(parent)
        w.currentChanged.connect(self.onCurrentIndexChanged)
        return w

    def icon(self):
        return super().icon("StackPanel")

    def name(self):
        return "SlideAniStackedWidget"

    def includeFile(self):
        return "qfluentwidgetspro"
