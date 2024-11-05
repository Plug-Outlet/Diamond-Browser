from ... import options as opts
from ... import echarts_types
from ...charts.chart import Chart
from ...globals import ChartType


class Sankey(Chart):
    """
    <<< Sankey >>>

    Sankey diagram is a special flow diagram, which is mainly used to
    express how raw materials, energy and so on from the initial form through
    the intermediate process of processing, transformation to the final form.
    """

    def add(
        self,
        series_name: str,
        nodes: echarts_types.Sequence,
        links: echarts_types.Sequence,
        *,
        pos_left: echarts_types.Union[str, echarts_types.Numeric] = "5%",
        pos_top: echarts_types.Union[str, echarts_types.Numeric] = "5%",
        pos_right: echarts_types.Union[str, echarts_types.Numeric] = "20%",
        pos_bottom: echarts_types.Union[str, echarts_types.Numeric] = "5%",
        node_width: echarts_types.Numeric = 20,
        node_gap: echarts_types.Numeric = 8,
        node_align: str = "justify",
        layout_iterations: echarts_types.Numeric = 32,
        orient: str = "horizontal",
        is_draggable: bool = True,
        edge_label_opt: echarts_types.Label = None,
        focus_node_mode: str = "none",
        levels: echarts_types.SankeyLevel = None,
        label_opts: echarts_types.Label = opts.LabelOpts(),
        linestyle_opt: echarts_types.LineStyle = opts.LineStyleOpts(),
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
    ):
        if layout_iterations < 32:
            layout_iterations = 32

        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": ChartType.SANKEY,
                "name": series_name,
                "data": nodes,
                "links": links,
                "left": pos_left,
                "top": pos_top,
                "right": pos_right,
                "bottom": pos_bottom,
                "nodeWidth": node_width,
                "nodeGap": node_gap,
                "nodeAlign": node_align,
                "layoutIteration": layout_iterations,
                "orient": orient,
                "draggable": is_draggable,
                "edgeLabel": edge_label_opt,
                "emphasis": {
                    "focus": focus_node_mode,
                },
                "levels": levels,
                "label": label_opts,
                "lineStyle": linestyle_opt,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
