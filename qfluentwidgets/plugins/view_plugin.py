# coding: utf-8
from qtpy.QtCore import Qt, QSize
from qtpy.QtGui import QColor
from qtpy.QtDesigner import QPyDesignerCustomWidgetPlugin

from qfluentwidgets import (ListWidget, ListView, TreeView, TreeWidget, TableView, TableWidget,
                            HorizontalFlipView, VerticalFlipView, HorizontalPipsPager, VerticalPipsPager)
from qfluentwidgetspro import (Pager, Skeleton, ArticleSkeleton, SquarePersonaSkeleton, CirclePersonaSkeleton,
                               RoundTableView, RoundTableWidget, LineTableView, LineTableWidget, GridTableView,
                               GridTableWidget, HorizontalCarousel, VerticalCarousel, HorizontalCircleColorPicker,
                               VerticalCircleColorPicker, FlowCircleColorPicker, RoundListView, RoundListWidget)

from plugin_base import PluginBase, ProPluginBase


class ViewPlugin(PluginBase):

    def group(self):
        return super().group() + ' (View)'


class ProViewPlugin(ProPluginBase):

    def group(self):
        return super().group() + ' (View)'


class HorizontalCircleColorPickerPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):

    def createWidget(self, parent):
        w = HorizontalCircleColorPicker(parent)
        w.addColors(["#51b1f4", QColor(32, 57, 106), QColor(203, 176, 238)])
        return w

    def icon(self):
        return super().icon("EasingFunction")

    def name(self):
        return "HorizontalCircleColorPicker"


class VerticalCircleColorPickerPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):

    def createWidget(self, parent):
        w = VerticalCircleColorPicker(parent)
        w.addColors(["#51b1f4", QColor(32, 57, 106), QColor(203, 176, 238)])
        return w

    def icon(self):
        return super().icon("EasingFunction")

    def name(self):
        return "VerticalCircleColorPicker"


class FlowCircleColorPickerPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):

    def createWidget(self, parent):
        w = FlowCircleColorPicker(parent)
        w.addColors(["#51b1f4", QColor(32, 57, 106), QColor(203, 176, 238)])
        return w

    def icon(self):
        return super().icon("EasingFunction")

    def name(self):
        return "FlowCircleColorPicker"


class ListWidgetPlugin(ViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ List widget plugin """

    def createWidget(self, parent):
        return ListWidget(parent)

    def icon(self):
        return super().icon("ListView")

    def name(self):
        return "ListWidget"


class ListViewPlugin(ViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ List view plugin """

    def createWidget(self, parent):
        return ListView(parent)

    def icon(self):
        return super().icon("ListView")

    def name(self):
        return "ListView"


class RoundListWidgetPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ List widget plugin """

    def createWidget(self, parent):
        return RoundListWidget(parent)

    def icon(self):
        return super().icon("ListView")

    def name(self):
        return "RoundListWidget"


class RoundListViewPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ List view plugin """

    def createWidget(self, parent):
        return RoundListView(parent)

    def icon(self):
        return super().icon("ListView")

    def name(self):
        return "RoundListView"


class TableWidgetPlugin(ViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Table widget plugin """

    def createWidget(self, parent):
        return TableWidget(parent)

    def icon(self):
        return super().icon("DataGrid")

    def name(self):
        return "TableWidget"


class TableViewPlugin(ViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Table widget plugin """

    def createWidget(self, parent):
        return TableView(parent)

    def icon(self):
        return super().icon("DataGrid")

    def name(self):
        return "TableView"


class RoundTableWidgetPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Table widget plugin """

    def createWidget(self, parent):
        return RoundTableWidget(parent)

    def icon(self):
        return super().icon("DataGrid")

    def name(self):
        return "RoundTableWidget"


class RoundTableViewPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Table widget plugin """

    def createWidget(self, parent):
        return RoundTableView(parent)

    def icon(self):
        return super().icon("DataGrid")

    def name(self):
        return "RoundTableView"


class LineTableWidgetPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Table widget plugin """

    def createWidget(self, parent):
        return LineTableWidget(parent)

    def icon(self):
        return super().icon("DataGrid")

    def name(self):
        return "LineTableWidget"


class LineTableViewPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Table widget plugin """

    def createWidget(self, parent):
        return LineTableView(parent)

    def icon(self):
        return super().icon("DataGrid")

    def name(self):
        return "LineTableView"


class GridTableWidgetPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Table widget plugin """

    def createWidget(self, parent):
        return GridTableWidget(parent)

    def icon(self):
        return super().icon("DataGrid")

    def name(self):
        return "GridTableWidget"


class GridTableViewPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Table widget plugin """

    def createWidget(self, parent):
        return GridTableView(parent)

    def icon(self):
        return super().icon("DataGrid")

    def name(self):
        return "GridTableView"


class TreeWidgetPlugin(ViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Tree widget plugin """

    def createWidget(self, parent):
        return TreeWidget(parent)

    def icon(self):
        return super().icon("TreeView")

    def name(self):
        return "TreeWidget"


class TreeViewPlugin(ViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Tree view plugin """

    def createWidget(self, parent):
        return TreeView(parent)

    def icon(self):
        return super().icon("TreeView")

    def name(self):
        return "TreeView"


class PagerPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Tree view plugin """

    def createWidget(self, parent):
        return Pager(parent)

    def icon(self):
        return super().icon("PipsPager")

    def name(self):
        return "Pager"


class HorizontalFlipViewPlugin(ViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Horizontal flip view plugin """

    def createWidget(self, parent):
        return HorizontalFlipView(parent)

    def icon(self):
        return super().icon("FlipView")

    def name(self):
        return "HorizontalFlipView"


class VerticalFlipViewPlugin(ViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Vertical flip view plugin """

    def createWidget(self, parent):
        return VerticalFlipView(parent)

    def icon(self):
        return super().icon("FlipView")

    def name(self):
        return "VerticalFlipView"


class HorizontalCarouselPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Horizontal flip view plugin """

    def createWidget(self, parent):
        return HorizontalCarousel(parent)

    def icon(self):
        return super().icon("FlipView")

    def name(self):
        return "HorizontalCarousel"


class VerticalCarouselPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Vertical flip view plugin """

    def createWidget(self, parent):
        return VerticalCarousel(parent)

    def icon(self):
        return super().icon("FlipView")

    def name(self):
        return "VerticalCarousel"


class HorizontalPipsPagerPlugin(ViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Horizontal flip view plugin """

    def createWidget(self, parent):
        w = HorizontalPipsPager(parent)
        w.setPageNumber(5)
        return w

    def icon(self):
        return super().icon("PipsPager")

    def name(self):
        return "HorizontalPipsPager"


class VerticalPipsPagerPlugin(ViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Vertical flip view plugin """

    def createWidget(self, parent):
        w = VerticalPipsPager(parent)
        w.setPageNumber(5)
        return w

    def icon(self):
        return super().icon("PipsPager")

    def name(self):
        return "VerticalPipsPager"


class SkeletonPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Tree view plugin """

    def createWidget(self, parent):
        return Skeleton(parent)

    def icon(self):
        return super().icon("RadioButtons")

    def name(self):
        return "Skeleton"


class ArticleSkeletonPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Tree view plugin """

    def createWidget(self, parent):
        return ArticleSkeleton(parent)

    def icon(self):
        return super().icon("RadioButtons")

    def name(self):
        return "ArticleSkeleton"


class SquarePersonaSkeletonPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Tree view plugin """

    def createWidget(self, parent):
        return SquarePersonaSkeleton(parent)

    def icon(self):
        return super().icon("RadioButtons")

    def name(self):
        return "SquarePersonaSkeleton"


class CirclePersonaSkeletonPlugin(ProViewPlugin, QPyDesignerCustomWidgetPlugin):
    """ Tree view plugin """

    def createWidget(self, parent):
        return CirclePersonaSkeleton(parent)

    def icon(self):
        return super().icon("RadioButtons")

    def name(self):
        return "CirclePersonaSkeleton"
