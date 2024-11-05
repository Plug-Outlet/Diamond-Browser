from ... import options as opts
from ... import echarts_types
from ...charts.chart import Chart
from ...globals import ChartType


class Radar(Chart):
    """
    <<< Radar >>>

    Radar maps are mainly used to represent multivariable data.
    """

    def add_schema(
        self,
        schema: echarts_types.Sequence[echarts_types.Union[opts.RadarIndicatorItem, dict]],
        shape: echarts_types.Optional[str] = None,
        center: echarts_types.Optional[echarts_types.Sequence] = None,
        radius: echarts_types.Optional[echarts_types.Union[echarts_types.Sequence, str]] = None,
        start_angle: echarts_types.Numeric = 90,
        textstyle_opts: echarts_types.TextStyle = opts.TextStyleOpts(),
        splitline_opt: echarts_types.SplitLine = opts.SplitLineOpts(is_show=True),
        splitarea_opt: echarts_types.SplitArea = opts.SplitAreaOpts(),
        axisline_opt: echarts_types.AxisLine = opts.AxisLineOpts(),
        radiusaxis_opts: echarts_types.RadiusAxis = None,
        angleaxis_opts: echarts_types.AngleAxis = None,
        polar_opts: echarts_types.Polar = None,
    ):
        self.options.update(
            radiusAxis=radiusaxis_opts, angleAxis=angleaxis_opts, polar=polar_opts
        )

        indicators = []
        for s in schema:
            if isinstance(s, opts.RadarIndicatorItem):
                s = s.opts
            indicators.append(s)

        if self.options.get("radar") is None:
            self.options.update(radar=[])

        self.options.get("radar").append(
            {
                "indicator": indicators,
                "shape": shape,
                "center": center,
                "radius": radius,
                "startAngle": start_angle,
                "name": {"textStyle": textstyle_opts},
                "splitLine": splitline_opt,
                "splitArea": splitarea_opt,
                "axisLine": axisline_opt,
            }
        )
        return self

    def add(
        self,
        series_name: str,
        data: echarts_types.Sequence[echarts_types.Union[opts.RadarItem, dict]],
        *,
        symbol: echarts_types.Optional[str] = None,
        color: echarts_types.Optional[str] = None,
        label_opts: opts.LabelOpts = opts.LabelOpts(),
        radar_index: echarts_types.Numeric = None,
        linestyle_opts: opts.LineStyleOpts = opts.LineStyleOpts(),
        areastyle_opts: opts.AreaStyleOpts = opts.AreaStyleOpts(),
        tooltip_opts: echarts_types.Tooltip = None,
    ):
        if all([isinstance(d, opts.RadarItem) for d in data]):
            for a in data:
                self._append_legend(a.get("name"))
        else:
            self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": ChartType.RADAR,
                "name": series_name,
                "data": data,
                "symbol": symbol,
                "label": label_opts,
                "radarIndex": radar_index,
                "itemStyle": {"normal": {"color": color}},
                "lineStyle": linestyle_opts,
                "areaStyle": areastyle_opts,
                "tooltip": tooltip_opts,
            }
        )
        return self
