import itertools

from ... import options as opts
from ... import echarts_types
from ...charts.chart import RectChart
from ...globals import ChartType


class Scatter(RectChart):
    """
    <<< Scatter >>>

    The scatter diagram on the rectangular coordinate system can be used to
    show the relationship between x and y of the data. If the data item has
    multiple dimensions, it can be represented by color, and the
    visualmap component can be used.
    """

    def _parse_data(
        self, y_axis: echarts_types.Sequence[echarts_types.Union[opts.ScatterItem, dict]]
    ) -> echarts_types.Optional[echarts_types.Sequence]:
        if self.options.get("dataset") is not None:
            return None
        elif len(self._xaxis_data) == 0:
            return y_axis
        elif isinstance(y_axis[0], (opts.ScatterItem, dict)):
            return y_axis
        elif isinstance(y_axis[0], echarts_types.Sequence):
            return [
                list(itertools.chain(list([x]), y))
                for x, y in zip(self._xaxis_data, y_axis)
            ]
        else:
            return [list(z) for z in zip(self._xaxis_data, y_axis)]

    def add_yaxis(
        self,
        series_name: str,
        y_axis: echarts_types.Sequence[echarts_types.Union[opts.ScatterItem, dict]],
        *,
        xaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        yaxis_index: echarts_types.Optional[echarts_types.Numeric] = None,
        color: echarts_types.Optional[str] = None,
        symbol: echarts_types.Optional[str] = None,
        symbol_size: echarts_types.Union[echarts_types.Numeric, echarts_types.Sequence] = 10,
        symbol_rotate: echarts_types.Optional[echarts_types.Numeric] = None,
        label_opts: echarts_types.Label = opts.LabelOpts(position="right"),
        markpoint_opts: echarts_types.MarkPoint = None,
        markline_opts: echarts_types.MarkLine = None,
        markarea_opts: echarts_types.MarkArea = None,
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
        encode: echarts_types.Union[echarts_types.JSFunc, dict, None] = None,
    ):
        self._append_color(color)
        self._append_legend(series_name)

        data = self._parse_data(y_axis=y_axis)

        self.options.get("series").append(
            {
                "type": ChartType.SCATTER,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "symbolRotate": symbol_rotate,
                "data": data,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "markArea": markarea_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "encode": encode,
            }
        )
        return self
