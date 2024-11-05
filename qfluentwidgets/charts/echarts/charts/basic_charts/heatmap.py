from ... import options as opts
from ... import echarts_types
from ...charts.chart import RectChart
from ...globals import ChartType


class HeatMap(RectChart):
    """
    <<< HeatMap >>>

    The heat map is mainly used to represent the size of the value by color,
    which must be used in conjunction with the visualMap component.
    Two categories of axes must be used in rectangular coordinates.
    """

    def __init__(
        self,
        init_opts: echarts_types.Init = opts.InitOpts(),
        render_opts: echarts_types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.set_global_opts(visualmap_opts=opts.VisualMapOpts(orient="horizontal"))

    def add_yaxis(
        self,
        series_name: str,
        yaxis_data: echarts_types.Sequence[echarts_types.Union[dict]],
        value: echarts_types.Sequence[echarts_types.Union[dict]],
        *,
        xaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        yaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        label_opts: echarts_types.Label = opts.LabelOpts(),
        markpoint_opts: echarts_types.MarkPoint = None,
        markline_opts: echarts_types.MarkLine = None,
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
    ):
        self._append_legend(series_name)
        self.options.get("yAxis")[0].update(data=yaxis_data)
        self.options.get("series").append(
            {
                "type": ChartType.HEATMAP,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "data": value,
                "label": label_opts,
                "markLine": markline_opts,
                "markPoint": markpoint_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
