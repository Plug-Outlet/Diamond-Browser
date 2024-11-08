from ... import options as opts
from ... import echarts_types
from ...charts.chart import Chart
from ...globals import ChartType


class Gauge(Chart):
    """
    <<< Gauge >>>

    The gauge displays a single key business measure.
    """

    def add(
        self,
        series_name: str,
        data_pair: echarts_types.Sequence,
        *,
        min_: echarts_types.Numeric = 0,
        max_: echarts_types.Numeric = 100,
        split_number: echarts_types.Numeric = 10,
        center: echarts_types.Sequence = None,
        radius: echarts_types.Union[echarts_types.Numeric, str] = "75%",
        start_angle: echarts_types.Numeric = 225,
        end_angle: echarts_types.Numeric = -45,
        is_clock_wise: bool = True,
        title_label_opts: echarts_types.GaugeTitle = opts.GaugeTitleOpts(
            offset_center=["0%", "20%"],
        ),
        detail_label_opts: echarts_types.GaugeDetail = opts.GaugeDetailOpts(
            formatter="{value}%",
            offset_center=["0%", "40%"],
        ),
        progress: echarts_types.GaugeProgress = opts.GaugeProgressOpts(),
        pointer: echarts_types.GaugePointer = opts.GaugePointerOpts(),
        anchor: echarts_types.GaugeAnchor = opts.GaugeAnchorOpts(),
        tooltip_opts: echarts_types.Tooltip = None,
        axisline_opts: echarts_types.AxisLine = None,
        axistick_opts: echarts_types.AxisTick = None,
        axislabel_opts: echarts_types.AxisLabel = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
    ):
        if center is None:
            center = ["50%", "50%"]

        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": ChartType.GAUGE,
                "title": title_label_opts,
                "detail": detail_label_opts,
                "name": series_name,
                "min": min_,
                "max": max_,
                "splitNumber": split_number,
                "center": center,
                "radius": radius,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "clockwise": is_clock_wise,
                "data": [{"name": n, "value": v} for n, v in data_pair],
                "tooltip": tooltip_opts,
                "axisLine": axisline_opts,
                "axisTick": axistick_opts,
                "axisLabel": axislabel_opts,
                "progress": progress,
                "anchor": anchor,
                "pointer": pointer,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
