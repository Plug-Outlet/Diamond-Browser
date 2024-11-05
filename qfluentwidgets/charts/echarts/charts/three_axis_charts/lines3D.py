from ... import options as opts
from ... import echarts_types
from ...charts.chart import Chart3D
from ...globals import ChartType
from ...options import InitOpts, RenderOpts


class Lines3D(Chart3D):
    """
    Lines 3D
    """

    def __init__(
        self,
        init_opts: echarts_types.Init = InitOpts(),
        render_opts: echarts_types.RenderInit = RenderOpts(),
    ):
        super().__init__(init_opts, render_opts)
        self._3d_chart_type = ChartType.LINES3D

    def add(
        self,
        series_name: str,
        data_pair: echarts_types.Sequence,
        coordinate_system: str,
        *,
        geo_3d_index: echarts_types.Numeric = 0,
        globe_index: echarts_types.Numeric = 0,
        is_polyline: bool = False,
        is_show_lines_effect: bool = False,
        lines_effect_period: echarts_types.Numeric = 4,
        lines_effect_constant_speed: echarts_types.Optional[echarts_types.Numeric] = None,
        lines_effect_trail_width: echarts_types.Numeric = 4,
        lines_effect_trail_length: echarts_types.Numeric = 0.1,
        lines_effect_trail_color: echarts_types.Optional[str] = None,
        lines_effect_trail_opacity: echarts_types.Optional[echarts_types.Numeric] = None,
        blend_mode: str = "source-over",
        linestyle_opts: echarts_types.Optional[echarts_types.LineStyle] = None,
        z_level: echarts_types.Numeric = -10,
        is_silent: bool = False,
    ):
        self.options.get("series").append(
            {
                "type": ChartType.LINES3D,
                "name": series_name,
                "data": data_pair,
                "coordinateSystem": coordinate_system,
                "geo3DIndex": geo_3d_index,
                "globeIndex": globe_index,
                "polyline": is_polyline,
                "effect": {
                    "show": is_show_lines_effect,
                    "period": lines_effect_period,
                    "constantSpeed": lines_effect_constant_speed,
                    "trailWidth": lines_effect_trail_width,
                    "trailLength": lines_effect_trail_length,
                    "trailColor": lines_effect_trail_color,
                    "trailOpacity": lines_effect_trail_opacity,
                },
                "lineStyle": linestyle_opts,
                "blendMode": blend_mode,
                "zlevel": z_level,
                "silent": is_silent,
            }
        )
        return self
