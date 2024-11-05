# coding: utf-8
from qtpy.QtCore import QSize, Qt
from qtpy.QtDesigner import QPyDesignerCustomWidgetPlugin

from qfluentwidgets import (InfoBar, ProgressBar, IndeterminateProgressBar, ProgressRing, StateToolTip, InfoBarPosition,
                            IndeterminateProgressRing, InfoBadge, DotInfoBadge, IconInfoBadge, FluentIcon)
from qfluentwidgetspro import (StepProgressBar, FilledProgressBar, ProgressPushButton, SingleScoreWidget,
                               MultiScoreWidget, Tag, RadialGauge)

from plugin_base import PluginBase, ProPluginBase


class StatusInfoPlugin(PluginBase):

    def group(self):
        return super().group() + ' (Status & Info)'


class ProStatusInfoPlugin(ProPluginBase):

    def group(self):
        return super().group() + ' (Status & Info)'


class ProgressBarPlugin(StatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Progress bar plugin """

    def createWidget(self, parent):
        return ProgressBar(parent)

    def icon(self):
        return super().icon("ProgressBar")

    def name(self):
        return "ProgressBar"


class FilledProgressBarPlugin(ProStatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Progress bar plugin """

    def createWidget(self, parent):
        return FilledProgressBar(parent)

    def icon(self):
        return super().icon("ProgressBar")

    def name(self):
        return "FilledProgressBar"


class IndeterminateProgressBarPlugin(StatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Indeterminate progress bar plugin """

    def createWidget(self, parent):
        return IndeterminateProgressBar(parent)

    def icon(self):
        return super().icon("ProgressBar")

    def name(self):
        return "IndeterminateProgressBar"


class StepProgressBarPlugin(ProStatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Step progress bar plugin """

    def createWidget(self, parent):
        w = StepProgressBar(parent)
        w.addStep('Your Order', FluentIcon.CALENDAR)
        w.addStep('Cart', FluentIcon.SHOPPING_CART)
        return w

    def icon(self):
        return super().icon("ProgressBar")

    def name(self):
        return "StepProgressBar"


class ProgressRingPlugin(StatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Progress ring plugin """

    def createWidget(self, parent):
        return ProgressRing(parent)

    def icon(self):
        return super().icon("ProgressRing")

    def name(self):
        return "ProgressRing"


class IndeterminateProgressRingPlugin(StatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Progress ring plugin """

    def createWidget(self, parent):
        return IndeterminateProgressRing(parent)

    def icon(self):
        return super().icon("ProgressRing")

    def name(self):
        return "IndeterminateProgressRing"


class RadialGaugePlugin(ProStatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Progress ring plugin """

    def createWidget(self, parent):
        return RadialGauge(parent)

    def icon(self):
        return super().icon("ProgressRing")

    def name(self):
        return "RadialGauge"


class ProgressButtonPlugin(ProStatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Progress button plugin """

    def createWidget(self, parent):
        return ProgressPushButton(self.toolTip(), parent)

    def icon(self):
        return super().icon("Button")

    def name(self):
        return "ProgressPushButton"


class TagPlugin(ProStatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Dot info badge plugin """

    def createWidget(self, parent):
        return Tag("Tag", parent)

    def icon(self):
        return super().icon("InfoBadge")

    def name(self):
        return "Tag"


class InfoBadgePlugin(StatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Info badge plugin """

    def createWidget(self, parent):
        return InfoBadge('10', parent)

    def icon(self):
        return super().icon("InfoBadge")

    def name(self):
        return "InfoBadge"


class DotInfoBadgePlugin(StatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Dot info badge plugin """

    def createWidget(self, parent):
        return DotInfoBadge(parent)

    def icon(self):
        return super().icon("InfoBadge")

    def name(self):
        return "DotInfoBadge"


class IconInfoBadgePlugin(StatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Icon info badge plugin """

    def createWidget(self, parent):
        return IconInfoBadge.success(FluentIcon.ACCEPT_MEDIUM, parent)

    def icon(self):
        return super().icon("InfoBadge")

    def name(self):
        return "IconInfoBadge"


class SingleScoreWidgetPlugin(ProStatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Progress bar plugin """

    def createWidget(self, parent):
        return SingleScoreWidget(parent)

    def icon(self):
        return super().icon("RatingControl")

    def name(self):
        return "SingleScoreWidget"


class MultiScoreWidgetPlugin(ProStatusInfoPlugin, QPyDesignerCustomWidgetPlugin):
    """ Progress bar plugin """

    def createWidget(self, parent):
        return MultiScoreWidget(parent)

    def icon(self):
        return super().icon("RatingControl")

    def name(self):
        return "MultiScoreWidget"
