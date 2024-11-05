from ... import options as opts
from ... import echarts_types
from ...charts.chart import Chart
from ...globals import ChartType


class Calendar(Chart):
    """
    <<< Calendar Diagram >>>

    The calendar diagram is mainly used to represent the size of a value by
    color and must be used in conjunction with the visualMap component.
    Two categories of axes must be used in rectangular coordinates.
    """

    def __init__(
        self,
        init_opts: echarts_types.Init = opts.InitOpts(),
        render_opts: echarts_types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(calendar=opts.CalendarOpts().opts)

    def add(
        self,
        series_name: str,
        yaxis_data: echarts_types.Sequence,
        *,
        type_: echarts_types.Union[str, ChartType] = ChartType.HEATMAP,
        calendar_index: echarts_types.Optional[echarts_types.Numeric] = None,
        label_opts: echarts_types.Label = opts.LabelOpts(is_show=False, position="inside"),
        calendar_opts: echarts_types.Union[echarts_types.Calendar, echarts_types.List[echarts_types.Calendar]] = None,
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
        visualmap_opts: echarts_types.VisualMap = None,
        **other_calendar_opts,
    ):
        if calendar_opts:
            self.options.update(calendar=calendar_opts)
        if visualmap_opts:
            self.options.update(visualMap=visualmap_opts)

        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": type_,
                "coordinateSystem": "calendar",
                "calendarIndex": calendar_index,
                "name": series_name,
                "data": yaxis_data,
                "label": label_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                **other_calendar_opts,
            }
        )
        return self
