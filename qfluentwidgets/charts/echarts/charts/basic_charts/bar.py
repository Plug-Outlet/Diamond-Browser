from ... import options as opts
from ... import echarts_types
from ...charts.chart import RectChart
from ...globals import ChartType


class Bar(RectChart):
    """
    <<< Bar Chart >>>

    Bar chart presents categorical data with rectangular bars
    with heights or lengths proportional to the values that they represent.
    """

    def add_yaxis(
        self,
        series_name: str,
        y_axis: echarts_types.Sequence[echarts_types.Union[echarts_types.Numeric, opts.BarItem, dict]],
        *,
        xaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        yaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        is_legend_hover_link: bool = True,
        color: echarts_types.Optional[str] = None,
        is_realtime_sort: bool = False,
        is_show_background: bool = False,
        background_style: echarts_types.Union[echarts_types.BarBackground, dict, None] = None,
        stack: echarts_types.Optional[str] = None,
        stack_strategy: echarts_types.Optional[str] = "samesign",
        sampling: echarts_types.Optional[str] = None,
        cursor: echarts_types.Optional[str] = "pointer",
        bar_width: echarts_types.Union[echarts_types.Numeric, str] = None,
        bar_max_width: echarts_types.Union[echarts_types.Numeric, str] = None,
        bar_min_width: echarts_types.Union[echarts_types.Numeric, str] = None,
        bar_min_height: echarts_types.Numeric = 0,
        category_gap: echarts_types.Union[echarts_types.Numeric, str] = "20%",
        gap: echarts_types.Optional[str] = "30%",
        is_large: bool = False,
        large_threshold: echarts_types.Numeric = 400,
        dimensions: echarts_types.Union[echarts_types.Sequence, None] = None,
        series_layout_by: str = "column",
        dataset_index: echarts_types.Numeric = 0,
        is_clip: bool = True,
        z_level: echarts_types.Numeric = 0,
        z: echarts_types.Numeric = 2,
        label_opts: echarts_types.Label = opts.LabelOpts(),
        markpoint_opts: echarts_types.MarkPoint = None,
        markline_opts: echarts_types.MarkLine = None,
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
        encode: echarts_types.Union[echarts_types.JSFunc, dict, None] = None,
    ):
        self._append_color(color)
        self._append_legend(series_name)

        if self.options.get("dataset") is not None:
            y_axis = None

        self.options.get("series").append(
            {
                "type": ChartType.BAR,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "legendHoverLink": is_legend_hover_link,
                "data": y_axis,
                "realtimeSort": is_realtime_sort,
                "showBackground": is_show_background,
                "backgroundStyle": background_style,
                "stack": stack,
                "stackStrategy": stack_strategy,
                "sampling": sampling,
                "cursor": cursor,
                "barWidth": bar_width,
                "barMaxWidth": bar_max_width,
                "barMinWidth": bar_min_width,
                "barMinHeight": bar_min_height,
                "barCategoryGap": category_gap,
                "barGap": gap,
                "large": is_large,
                "largeThreshold": large_threshold,
                "dimensions": dimensions,
                "seriesLayoutBy": series_layout_by,
                "datasetIndex": dataset_index,
                "clip": is_clip,
                "zlevel": z_level,
                "z": z,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "encode": encode,
            }
        )
        return self
