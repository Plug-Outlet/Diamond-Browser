# coding: utf-8
from qtpy.QtCore import Qt
from qtpy.QtDesigner import QPyDesignerCustomWidgetPlugin

from qfluentwidgetspro import (DropDownColorPalette, CustomDropDownColorPalette, DropDownColorPicker,
                               CustomDropDownColorPicker, ShortcutPicker, ScreenColorPicker)

from plugin_base import ProPluginBase


class FlyoutPlugin(ProPluginBase):

    def group(self):
        return super().group() + ' (Flyout)'


class ScreenColorPickerPlugin(FlyoutPlugin, QPyDesignerCustomWidgetPlugin):
    """ Command bar plugin """

    def createWidget(self, parent):
        return ScreenColorPicker(parent)

    def icon(self):
        return super().icon("ColorPaletteResources")

    def name(self):
        return "ScreenColorPicker"


class DropDownColorPalettePlugin(FlyoutPlugin, QPyDesignerCustomWidgetPlugin):
    """ Command bar plugin """

    def createWidget(self, parent):
        return DropDownColorPalette(parent)

    def icon(self):
        return super().icon("ColorPaletteResources")

    def name(self):
        return "DropDownColorPalette"


class CustomDropDownColorPalettePlugin(FlyoutPlugin, QPyDesignerCustomWidgetPlugin):
    """ Command bar plugin """

    def createWidget(self, parent):
        return CustomDropDownColorPalette(parent)

    def icon(self):
        return super().icon("ColorPaletteResources")

    def name(self):
        return "CustomDropDownColorPalette"


class DropDownColorPickerPlugin(FlyoutPlugin, QPyDesignerCustomWidgetPlugin):
    """ Command bar plugin """

    def createWidget(self, parent):
        return DropDownColorPicker(parent)

    def icon(self):
        return super().icon("ColorPicker")

    def name(self):
        return "DropDownColorPicker"


class CustomDropDownColorPickerPlugin(FlyoutPlugin, QPyDesignerCustomWidgetPlugin):
    """ Command bar plugin """

    def createWidget(self, parent):
        return CustomDropDownColorPicker(parent)

    def icon(self):
        return super().icon("ColorPicker")

    def name(self):
        return "CustomDropDownColorPicker"


class ShortcutPickerPlugin(FlyoutPlugin, QPyDesignerCustomWidgetPlugin):
    """ Command bar plugin """

    def createWidget(self, parent):
        return ShortcutPicker(parent)

    def icon(self):
        return super().icon("Button")

    def name(self):
        return "ShortcutPicker"
