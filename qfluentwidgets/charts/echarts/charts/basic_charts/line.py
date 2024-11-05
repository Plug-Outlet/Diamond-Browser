from ... import options as opts
from ... import echarts_types
from ...charts.chart import RectChart
from ...globals import ChartType


class Line(RectChart):
    """
    <<< Line Chart >>>

    Line chart is a graph that connects all data points
    with single line to show the change trend of data.
    """

    def add_yaxis(
        self,
        series_name: str,
        y_axis: echarts_types.Sequence[echarts_types.Union[opts.LineItem, dict]],
        *,
        is_connect_nones: bool = False,
        xaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        yaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        color: echarts_types.Optional[str] = None,
        is_symbol_show: bool = True,
        symbol: echarts_types.Optional[str] = None,
        symbol_size: echarts_types.Union[echarts_types.Numeric, echarts_types.Sequence] = 4,
        stack: echarts_types.Optional[str] = None,
        is_smooth: bool = False,
        is_clip: bool = True,
        is_step: bool = False,
        is_hover_animation: bool = True,
        z_level: echarts_types.Numeric = 0,
        z: echarts_types.Numeric = 0,
        log_base: echarts_types.Numeric = 10,
        sampling: echarts_types.Optional[str] = None,
        dimensions: echarts_types.Union[echarts_types.Sequence, None] = None,
        series_layout_by: str = "column",
        markpoint_opts: echarts_types.MarkPoint = None,
        markline_opts: echarts_types.MarkLine = None,
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
        label_opts: echarts_types.Label = opts.LabelOpts(),
        linestyle_opts: echarts_types.LineStyle = opts.LineStyleOpts(),
        areastyle_opts: echarts_types.AreaStyle = opts.AreaStyleOpts(),
        encode: echarts_types.Union[echarts_types.JSFunc, dict, None] = None,
    ):
        self._append_color(color)
        self._append_legend(series_name)

        if all([isinstance(d, opts.LineItem) for d in y_axis]):
            data = y_axis
        else:
            # 合并 x 和 y 轴数据，避免当 X 轴的类型设置为 'value' 的时候，
            # X、Y 轴均显示 Y 轴数据
            try:
                xaxis_index = xaxis_index or 0
                data = [
                    list(z)
                    for z in zip(self.options["xAxis"][xaxis_index]["data"], y_axis)
                ]
            except IndexError:
                data = [list(z) for z in zip(self._xaxis_data, y_axis)]

        if self.options.get("dataset") is not None and not y_axis:
            data = None

        self.options.get("series").append(
            {
                "type": ChartType.LINE,
                "name": series_name,
                "connectNulls": is_connect_nones,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "showSymbol": is_symbol_show,
                "smooth": is_smooth,
                "clip": is_clip,
                "step": is_step,
                "stack": stack,
                "data": data,
                "hoverAnimation": is_hover_animation,
                "label": label_opts,
                "logBase": log_base,
                "sampling": sampling,
                "dimensions": dimensions,
                "encode": encode,
                "seriesLayoutBy": series_layout_by,
                "lineStyle": linestyle_opts,
                "areaStyle": areastyle_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "zlevel": z_level,
                "z": z,
            }
        )
        return self
