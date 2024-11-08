# coding: utf-8
from qtpy.QtCore import Qt
from qtpy.QtDesigner import QPyDesignerCustomWidgetPlugin

from qfluentwidgets import (NavigationInterface, NavigationPanel, Pivot, SegmentedWidget, NavigationBar,
                            FluentIcon, TabBar, BreadcrumbBar, SegmentedToolWidget, SegmentedToggleToolWidget)
from qfluentwidgetspro import TopNavigationBar, ExclusiveLiteFilter, MultiSelectionLiteFilter
from plugin_base import PluginBase, ProPluginBase


class NavigationPlugin(PluginBase):

    def group(self):
        return super().group() + ' (Navigation)'


class ProNavigationPlugin(ProPluginBase):

    def group(self):
        return super().group() + ' (Navigation)'


class BreadcrumbBarPlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Breadcrumb plugin """

    def createWidget(self, parent):
        w = BreadcrumbBar(parent)
        w.addItem('Home', 'Home')
        w.addItem('Documents', 'Documents')
        return w

    def icon(self):
        return super().icon("BreadcrumbBar")

    def name(self):
        return "BreadcrumbBar"



class NavigationInterfacePlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Navigation interface plugin """

    def createWidget(self, parent):
        return NavigationInterface(parent, True, True)

    def icon(self):
        return super().icon("NavigationView")

    def name(self):
        return "NavigationInterface"


class NavigationPanelPlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Navigation panel plugin """

    def createWidget(self, parent):
        return NavigationPanel(parent)

    def icon(self):
        return super().icon("NavigationView")

    def name(self):
        return "NavigationPanel"


class NavigationBarPlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Navigation bar plugin """

    def createWidget(self, parent):
        bar = NavigationBar(parent)
        bar.addItem('item', FluentIcon.HOME, 'Home')
        return bar

    def icon(self):
        return super().icon("NavigationView")

    def name(self):
        return "NavigationBar"


class PivotPlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Navigation panel plugin """

    def createWidget(self, parent):
        p = Pivot(parent)
        for i in range(1, 4):
            p.addItem(f'Item{i}', f'Item{i}', print)

        p.setCurrentItem('Item1')
        return p

    def icon(self):
        return super().icon("Pivot")

    def name(self):
        return "Pivot"


# class TopNavigationBarPlugin(ProNavigationPlugin, QPyDesignerCustomWidgetPlugin):
#     """ Navigation panel plugin """
# 
#     def createWidget(self, parent):
#         p = TopNavigationBar(parent)
#         p.addItem('home', 'Home', FluentIcon.HOME)
#         p.addItem('history', 'History', FluentIcon.HISTORY)
#         p.setCurrentItem('home')
#         return p
# 
#     def icon(self):
#         return super().icon("Pivot")
# 
#     def name(self):
#         return "TopNavigationBar"


class SegmentedWidgetPlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Segmented widget plugin """

    def createWidget(self, parent):
        p = SegmentedWidget(parent)
        for i in range(1, 4):
            p.addItem(f'Item{i}', f'Item{i}', print)

        p.setCurrentItem('Item1')
        return p

    def icon(self):
        return super().icon("Pivot")

    def name(self):
        return "SegmentedWidget"


class SegmentedToolWidgetPlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Segmented tool widget plugin """

    def createWidget(self, parent):
        p = SegmentedToolWidget(parent)
        p.addItem(f'k1', FluentIcon.TRANSPARENT)
        p.addItem(f'k2', FluentIcon.CHECKBOX)
        p.addItem(f'k3', FluentIcon.CONSTRACT)
        p.setCurrentItem('k1')
        return p

    def icon(self):
        return super().icon("Pivot")

    def name(self):
        return "SegmentedToolWidget"


class SegmentedToggleToolWidgetPlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Segmented tool widget plugin """

    def createWidget(self, parent):
        p = SegmentedToggleToolWidget(parent)
        p.addItem(f'k1', FluentIcon.TRANSPARENT)
        p.addItem(f'k2', FluentIcon.CHECKBOX)
        p.addItem(f'k3', FluentIcon.CONSTRACT)
        p.setCurrentItem('k1')
        return p

    def icon(self):
        return super().icon("Pivot")

    def name(self):
        return "SegmentedToggleToolWidget"


class TabBarPlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Tab bar plugin """

    def createWidget(self, parent):
        p = TabBar(parent)
        for i in range(1, 4):
            p.addTab(f'Tab {i}', f'Tab {i}', FluentIcon.BASKETBALL)

        return p

    def icon(self):
        return super().icon("TabView")

    def name(self):
        return "TabBar"


class ExclusiveLiteFilterPlugin(ProNavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Tab bar plugin """

    def createWidget(self, parent):
        p = ExclusiveLiteFilter(parent)
        p.addItems(["All", "App", "Documents"])
        return p

    def icon(self):
        return super().icon("Pivot")

    def name(self):
        return "ExclusiveLiteFilter"


class MultiSelectionLiteFilterPlugin(ProNavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Tab bar plugin """

    def createWidget(self, parent):
        p = MultiSelectionLiteFilter(parent)
        p.addItems(["All", "App", "Documents"])
        return p

    def icon(self):
        return super().icon("Pivot")

    def name(self):
        return "MultiSelectionLiteFilter"
