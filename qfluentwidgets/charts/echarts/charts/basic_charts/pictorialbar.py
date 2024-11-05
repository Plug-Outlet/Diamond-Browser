from ... import options as opts
from ... import echarts_types
from ...charts.chart import RectChart
from ...globals import ChartType


class PictorialBar(RectChart):
    """
    <<< PictorialBar Chart >>>

    PictorialBar is a histogram that can set various figurative graphic
    elements (such as images, SVG PathData, etc.)
    """

    def add_yaxis(
        self,
        series_name: str,
        y_axis: echarts_types.Sequence[echarts_types.Union[echarts_types.Numeric, opts.BarItem, dict]],
        *,
        symbol: echarts_types.Optional[str] = None,
        symbol_size: echarts_types.Union[echarts_types.Numeric, echarts_types.Sequence, None] = None,
        symbol_pos: echarts_types.Optional[str] = None,
        symbol_offset: echarts_types.Optional[echarts_types.Sequence] = None,
        symbol_rotate: echarts_types.Optional[echarts_types.Numeric] = None,
        symbol_repeat: echarts_types.Optional[str] = None,
        symbol_repeat_direction: echarts_types.Optional[str] = None,
        symbol_margin: echarts_types.Union[echarts_types.Numeric, str, None] = None,
        is_symbol_clip: bool = False,
        xaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        yaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        color: echarts_types.Optional[str] = None,
        category_gap: echarts_types.Union[echarts_types.Numeric, str] = "20%",
        gap: echarts_types.Optional[str] = None,
        label_opts: echarts_types.Label = opts.LabelOpts(),
        markpoint_opts: echarts_types.MarkPoint = None,
        markline_opts: echarts_types.MarkLine = None,
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
        encode: echarts_types.Union[echarts_types.JsCode, dict] = None,
    ):
        self._append_color(color)
        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": ChartType.PICTORIALBAR,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "symbolPosition": symbol_pos,
                "symbolOffset": symbol_offset,
                "symbolRotate": symbol_rotate,
                "symbolRepeat": symbol_repeat,
                "symbolRepeatDirection": symbol_repeat_direction,
                "symbolMargin": symbol_margin,
                "symbolClip": is_symbol_clip,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "data": y_axis,
                "barCategoryGap": category_gap,
                "barGap": gap,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "encode": encode,
            }
        )
        return self
