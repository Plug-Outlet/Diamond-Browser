# coding: utf-8
from qtpy.QtCore import Qt
from qtpy.QtDesigner import QPyDesignerCustomWidgetPlugin

from qfluentwidgets import DatePicker, TimePicker, ZhDatePicker, AMTimePicker, CalendarPicker
from qfluentwidgetspro import RangeCalendarPicker, ProCalendarPicker

from plugin_base import PluginBase, ProPluginBase


class DateTimePlugin(PluginBase):

    def group(self):
        return super().group() + ' (Date Time)'


class ProDateTimePlugin(ProPluginBase):

    def group(self):
        return super().group() + ' (Date Time)'


class CalendarPickerPlugin(DateTimePlugin, QPyDesignerCustomWidgetPlugin):
    """ Calendar picker plugin """

    def createWidget(self, parent):
        return CalendarPicker(parent)

    def icon(self):
        return super().icon("CalendarDatePicker")

    def name(self):
        return "CalendarPicker"


class ProCalendarPickerPlugin(ProDateTimePlugin, QPyDesignerCustomWidgetPlugin):
    """ Calendar picker plugin """

    def createWidget(self, parent):
        return ProCalendarPicker(parent)

    def icon(self):
        return super().icon("CalendarDatePicker")

    def name(self):
        return "ProCalendarPicker"


class RangeCalendarPickerPlugin(ProDateTimePlugin, QPyDesignerCustomWidgetPlugin):
    """ Calendar picker plugin """

    def createWidget(self, parent):
        return CalendarPicker(parent)

    def icon(self):
        return super().icon("CalendarDatePicker")

    def name(self):
        return "RangeCalendarPicker"


class DatePickerPlugin(DateTimePlugin, QPyDesignerCustomWidgetPlugin):
    """ Date picker plugin """

    def createWidget(self, parent):
        return DatePicker(parent)

    def icon(self):
        return super().icon("DatePicker")

    def name(self):
        return "DatePicker"


class ZhDatePickerPlugin(DateTimePlugin, QPyDesignerCustomWidgetPlugin):
    """ Chinese Date picker plugin """

    def createWidget(self, parent):
        return ZhDatePicker(parent)

    def icon(self):
        return super().icon("DatePicker")

    def name(self):
        return "ZhDatePicker"

    def toolTip(self):
        return "Chinese date picker"


class TimePickerPlugin(DateTimePlugin, QPyDesignerCustomWidgetPlugin):
    """ Time picker plugin """

    def createWidget(self, parent):
        return TimePicker(parent)

    def icon(self):
        return super().icon("TimePicker")

    def name(self):
        return "TimePicker"

    def toolTip(self):
        return "24 hours time picker"


class AMTimePickerPlugin(DateTimePlugin, QPyDesignerCustomWidgetPlugin):
    """ AM/PM time picker plugin """

    def createWidget(self, parent):
        return AMTimePicker(parent)

    def icon(self):
        return super().icon("TimePicker")

    def name(self):
        return "AMTimePicker"

    def toolTip(self):
        return "AM/PM time picker"
