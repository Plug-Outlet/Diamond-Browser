from ... import options as opts
from ... import echarts_types
from ...charts.chart import Chart3D
from ...globals import ChartType
from ...options import InitOpts, RenderOpts


class Map3D(Chart3D):
    """
    3D map
    """

    def __init__(
        self,
        init_opts: echarts_types.Init = InitOpts(),
        render_opts: echarts_types.RenderInit = RenderOpts(),
    ):
        super().__init__(init_opts, render_opts)
        self._3d_chart_type = ChartType.MAP3D

    def add(
        self,
        series_name: str,
        data_pair: echarts_types.Sequence,
        *,
        type_: ChartType = None,
        maptype: str = "china",
        is_map_symbol_show: bool = True,
        grid_3d_index: echarts_types.Numeric = 0,
        geo_3d_index: echarts_types.Numeric = 0,
        globe_index: echarts_types.Numeric = 0,
        bar_size: echarts_types.Optional[echarts_types.Numeric] = None,
        bevel_size: echarts_types.Numeric = 0,
        bevel_smoothness: echarts_types.Numeric = 2,
        stack: echarts_types.Optional[str] = None,
        min_height: echarts_types.Numeric = 2,
        symbol: str = "circle",
        symbol_size: echarts_types.Union[echarts_types.Numeric, echarts_types.Sequence, echarts_types.JSFunc] = 10,
        blend_mode: str = "source-over",
        is_polyline: bool = False,
        effect: echarts_types.Lines3DEffect = None,
        linestyle_opts: echarts_types.LineStyle = opts.LineStyleOpts(),
        label_opts: echarts_types.Label = opts.LabelOpts(),
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
        emphasis_label_opts: echarts_types.Label = None,
        emphasis_itemstyle_opts: echarts_types.ItemStyle = None,
        shading: echarts_types.Optional[str] = None,
        realistic_material_opts: echarts_types.Optional[echarts_types.Map3DRealisticMaterial] = None,
        lambert_material_opts: echarts_types.Optional[echarts_types.Map3DLambertMaterial] = None,
        color_material_opts: echarts_types.Optional[echarts_types.Map3DColorMaterial] = None,
        zlevel: echarts_types.Numeric = -10,
        is_silent: bool = False,
        is_animation: bool = True,
        animation_duration_update: echarts_types.Numeric = 100,
        animation_easing_update: echarts_types.Numeric = "cubicOut",
    ):
        if type_ != ChartType.LINES3D:
            data = [{"name": n, "value": v} for n, v in data_pair]
        else:
            data = data_pair
        self._append_legend(series_name)
        if type_ is None or type_ == ChartType.MAP3D:
            self.options.get("series").append(
                {
                    "type": ChartType.MAP3D,
                    "name": series_name,
                    "map": maptype,
                    "coordinateSystem": "geo3D",
                    "label": label_opts,
                    "data": data,
                    "itemStyle": itemstyle_opts,
                    "showLegendSymbol": is_map_symbol_show,
                    "tooltip": tooltip_opts,
                    "emphasis": {
                        "label": emphasis_label_opts,
                        "itemStyle": emphasis_itemstyle_opts,
                    },
                }
            )
        elif type_ == ChartType.BAR3D:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": "geo3D",
                    "grid3DIndex": grid_3d_index,
                    "geo3DIndex": geo_3d_index,
                    "globeIndex": globe_index,
                    "barSize": bar_size,
                    "bevelSize": bevel_size,
                    "bevelSmoothness": bevel_smoothness,
                    "stack": stack,
                    "minHeight": min_height,
                    "label": label_opts,
                    "itemStyle": itemstyle_opts,
                    "emphasis": {
                        "label": emphasis_label_opts,
                        "itemStyle": emphasis_itemstyle_opts,
                    },
                    "data": data,
                    "shading": shading,
                    "realisticMaterial": realistic_material_opts,
                    "lambertMaterial": lambert_material_opts,
                    "colorMaterial": color_material_opts,
                    "zlevel": zlevel,
                    "silent": is_silent,
                    "animation": is_animation,
                    "animationDurationUpdate": animation_duration_update,
                    "animationEasingUpdate": animation_easing_update,
                }
            )
        elif type_ == ChartType.SCATTER3D:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": "geo3D",
                    "grid3DIndex": grid_3d_index,
                    "geo3DIndex": geo_3d_index,
                    "globeIndex": globe_index,
                    "symbol": symbol,
                    "symbolSize": symbol_size,
                    "label": label_opts,
                    "itemStyle": itemstyle_opts,
                    "emphasis": {
                        "label": emphasis_label_opts,
                        "itemStyle": emphasis_itemstyle_opts,
                    },
                    "data": data,
                    "blendMode": blend_mode,
                    "zlevel": zlevel,
                    "silent": is_silent,
                    "animation": is_animation,
                    "animationDurationUpdate": animation_duration_update,
                    "animationEasingUpdate": animation_easing_update,
                }
            )
        elif type_ == ChartType.LINE3D:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": "geo3D",
                    "grid3DIndex": grid_3d_index,
                    "lineStyle": linestyle_opts,
                    "data": data,
                    "zlevel": zlevel,
                    "silent": is_silent,
                    "animation": is_animation,
                    "animationDurationUpdate": animation_duration_update,
                    "animationEasingUpdate": animation_easing_update,
                }
            )
        elif type_ == ChartType.LINES3D:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": "geo3D",
                    "geo3DIndex": geo_3d_index,
                    "globeIndex": globe_index,
                    "polyline": is_polyline,
                    "effect": effect,
                    "lineStyle": linestyle_opts,
                    "data": data,
                    "blendMode": blend_mode,
                    "zlevel": zlevel,
                    "silent": is_silent,
                }
            )
        return self

    def add_schema(
        self,
        maptype: str = "china",
        name: echarts_types.Optional[str] = None,
        *,
        box_width: echarts_types.Optional[echarts_types.Numeric] = 100,
        box_height: echarts_types.Optional[echarts_types.Numeric] = 10,
        box_depth: echarts_types.Optional[echarts_types.Numeric] = None,
        region_height: echarts_types.Optional[echarts_types.Numeric] = 3,
        environment: echarts_types.Optional[echarts_types.JSFunc] = None,
        is_show_ground: bool = False,
        ground_color: str = "#aaa",
        is_instancing: bool = False,
        map3d_label: echarts_types.Map3DLabel = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
        emphasis_label_opts: echarts_types.Label = None,
        emphasis_itemstyle_opts: echarts_types.ItemStyle = None,
        shading: echarts_types.Optional[str] = None,
        realistic_material_opts: echarts_types.Optional[echarts_types.Map3DRealisticMaterial] = None,
        lambert_material_opts: echarts_types.Optional[echarts_types.Map3DLambertMaterial] = None,
        color_material_opts: echarts_types.Optional[echarts_types.Map3DColorMaterial] = None,
        light_opts: echarts_types.Optional[echarts_types.Map3DLight] = None,
        post_effect_opts: echarts_types.Optional[echarts_types.Map3DPostEffect] = None,
        is_enable_super_sampling: echarts_types.Union[str, bool] = "auto",
        view_control_opts: echarts_types.Optional[echarts_types.Map3DViewControl] = None,
        zlevel: echarts_types.Optional[echarts_types.Numeric] = -10,
        pos_left: echarts_types.Union[echarts_types.Numeric, str] = "auto",
        pos_top: echarts_types.Union[echarts_types.Numeric, str] = "auto",
        pos_right: echarts_types.Union[echarts_types.Numeric, str] = "auto",
        pos_bottom: echarts_types.Union[echarts_types.Numeric, str] = "auto",
        pos_width: echarts_types.Union[echarts_types.Numeric, str] = "auto",
        pos_height: echarts_types.Union[echarts_types.Numeric, str] = "auto",
    ):
        self.js_dependencies.add(maptype)
        self.options.update(
            geo3D={
                "map": maptype,
                "name": name,
                "boxWidth": box_width,
                "boxHeight": box_height,
                "boxDepth": box_depth,
                "regionHeight": region_height,
                "environment": environment,
                "groundPlane": {"show": is_show_ground, "color": ground_color},
                "instancing": is_instancing,
                "itemStyle": itemstyle_opts,
                "label": map3d_label,
                "emphasis": {
                    "label": emphasis_label_opts,
                    "itemStyle": emphasis_itemstyle_opts,
                },
                "shading": shading,
                "realisticMaterial": realistic_material_opts,
                "lambertMaterial": lambert_material_opts,
                "colorMaterial": color_material_opts,
                "light": light_opts,
                "postEffect": post_effect_opts,
                "temporalSuperSampling": {"enable": is_enable_super_sampling},
                "viewControl": view_control_opts,
                "zlevel": zlevel,
                "left": pos_left,
                "top": pos_top,
                "right": pos_right,
                "bottom": pos_bottom,
                "width": pos_width,
                "height": pos_height,
            }
        )
        return self
