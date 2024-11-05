from ... import options as opts
from ... import echarts_types
from ...charts.chart import RectChart
from ...globals import ChartType


class EffectScatter(RectChart):
    """
    <<< Scatter plots with ripple effects animation >>>

    Use animation effects to visually highlight designated data set.
    """

    def add_yaxis(
        self,
        series_name: str,
        y_axis: echarts_types.Sequence[echarts_types.Union[opts.EffectScatterItem, dict]],
        *,
        xaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        yaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        color: echarts_types.Optional[str] = None,
        symbol: echarts_types.Optional[str] = None,
        symbol_size: echarts_types.Numeric = 10,
        symbol_rotate: echarts_types.Optional[echarts_types.Numeric] = None,
        label_opts: echarts_types.Label = opts.LabelOpts(),
        effect_opts: echarts_types.Effect = opts.EffectOpts(),
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
    ):
        self._append_color(color)
        self._append_legend(series_name)

        if all([isinstance(d, opts.EffectScatterItem) for d in y_axis]):
            y_axis = y_axis
        else:
            y_axis = [list(z) for z in zip(self._xaxis_data, y_axis)]

        self.options.get("series").append(
            {
                "type": ChartType.EFFECT_SCATTER,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "showEffectOn": "render",
                "rippleEffect": effect_opts,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "symbolRotate": symbol_rotate,
                "data": y_axis,
                "label": label_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
