from ... import options as opts
from ... import echarts_types
from ...charts.chart import Chart
from ...globals import ChartType


class Tree(Chart):
    """
    <<< Tree diagrams >>>

    Tree diagrams are used primarily to visualize tree data structures,
    which are special hierarchical types with unique root nodes, left subtrees,
    and right subtrees.
    """

    @staticmethod
    def _set_collapse_interval(data, interval):
        """
        间隔折叠节点，当节点过多时可以解决节点显示过杂间隔。

        :param data: 节点数据
        :param interval: 指定间隔
        """
        if interval <= 0:
            return data
        if data and isinstance(data, list):
            for d in data:
                children = d.get("children", None)
                if children and interval > 0:
                    for index, value in enumerate(children):
                        if index % interval == 0:
                            value.update(collapsed="false")
            return data

    def add(
        self,
        series_name: str,
        data: echarts_types.Sequence[echarts_types.Union[opts.TreeItem, dict]],
        *,
        layout: str = "orthogonal",
        symbol: echarts_types.JSFunc = "emptyCircle",
        symbol_size: echarts_types.Union[echarts_types.JSFunc, echarts_types.Numeric, echarts_types.Sequence] = 7,
        orient: str = "LR",
        pos_top: echarts_types.Optional[str] = None,
        pos_left: echarts_types.Optional[str] = None,
        pos_bottom: echarts_types.Optional[str] = None,
        pos_right: echarts_types.Optional[str] = None,
        collapse_interval: echarts_types.Numeric = 0,
        edge_shape: str = "curve",
        edge_fork_position: str = "50%",
        is_roam: bool = False,
        is_expand_and_collapse: bool = True,
        initial_tree_depth: echarts_types.Optional[echarts_types.Numeric] = None,
        label_opts: echarts_types.Label = opts.LabelOpts(),
        leaves_label_opts: echarts_types.Label = opts.LabelOpts(),
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
    ):
        _data = self._set_collapse_interval(data, collapse_interval)
        self.options.get("series").append(
            {
                "type": ChartType.TREE,
                "name": series_name,
                "data": _data,
                "left": pos_left,
                "right": pos_right,
                "top": pos_top,
                "bottom": pos_bottom,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "edgeShape": edge_shape,
                "edgeForkPosition": edge_fork_position,
                "roam": is_roam,
                "expandAndCollapse": is_expand_and_collapse,
                "initialTreeDepth": initial_tree_depth,
                "layout": layout,
                "orient": orient,
                "label": label_opts,
                "leaves": {"label": leaves_label_opts},
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
