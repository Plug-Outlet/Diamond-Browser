from ... import options as opts
from ... import echarts_types
from ...charts.chart import Chart
from ...globals import ChartType


class TreeMap(Chart):
    """
    <<< TreeMap >>>

    TreeMap are a common visual representation of "hierarchical data" and "tree data".
    It mainly uses area to highlight the important nodes in the hierarchy of "tree".
    """

    def add(
        self,
        series_name: str,
        data: echarts_types.Sequence[echarts_types.Union[opts.TreeItem, dict]],
        *,
        leaf_depth: echarts_types.Optional[echarts_types.Numeric] = None,
        pos_left: echarts_types.Optional[str] = None,
        pos_right: echarts_types.Optional[str] = None,
        pos_top: echarts_types.Optional[str] = None,
        pos_bottom: echarts_types.Optional[str] = None,
        width: echarts_types.Union[str, echarts_types.Numeric] = "80%",
        height: echarts_types.Union[str, echarts_types.Numeric] = "80%",
        square_ratio: echarts_types.Optional[echarts_types.JSFunc] = None,
        drilldown_icon: str = "▶",
        roam: echarts_types.Union[bool, str] = True,
        node_click: echarts_types.Union[bool, str] = "zoomToNode",
        zoom_to_node_ratio: echarts_types.Numeric = 0.32 * 0.32,
        levels: echarts_types.TreeMapLevel = None,
        visual_min: echarts_types.Optional[echarts_types.Numeric] = None,
        visual_max: echarts_types.Optional[echarts_types.Numeric] = None,
        visual_dimension: echarts_types.Optional[echarts_types.Numeric] = None,
        color_alpha: echarts_types.Union[echarts_types.Numeric, echarts_types.Sequence] = None,
        color_saturation: echarts_types.Union[echarts_types.Numeric, echarts_types.Sequence] = None,
        color_mapping_by: str = "index",
        visible_min: echarts_types.Numeric = 10,
        children_visible_min: echarts_types.Optional[echarts_types.Numeric] = None,
        label_opts: echarts_types.Label = opts.LabelOpts(position="inside"),
        upper_label_opts: echarts_types.Label = opts.LabelOpts(position="inside"),
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
        breadcrumb_opts: echarts_types.TreeMapBreadcrumb = None,
    ):
        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": ChartType.TREEMAP,
                "name": series_name,
                "data": data,
                "left": pos_left,
                "right": pos_right,
                "top": pos_top,
                "width": width,
                "height": height,
                "bottom": pos_bottom,
                "squareRatio": square_ratio,
                "label": label_opts,
                "upperLabel": upper_label_opts,
                "leafDepth": leaf_depth,
                "drillDownIcon": drilldown_icon,
                "roam": roam,
                "nodeClick": node_click,
                "zoomToNodeRatio": zoom_to_node_ratio,
                "levels": levels,
                "visualMin": visual_min,
                "visualMax": visual_max,
                "visualDimension": visual_dimension,
                "colorAlpha": color_alpha,
                "colorSaturation": color_saturation,
                "colorMappingBy": color_mapping_by,
                "visibleMin": visible_min,
                "childrenVisibleMin": children_visible_min,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "breadcrumb": breadcrumb_opts,
            }
        )
        return self
