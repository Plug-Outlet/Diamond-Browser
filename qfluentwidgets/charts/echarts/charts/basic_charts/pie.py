from ... import options as opts
from ... import echarts_types
from ...charts.chart import Chart
from ...globals import ChartType


class Pie(Chart):
    """
    <<< Pie >>>

    The pie chart is mainly used to represent the proportion of data of
    different categories in the total. Each radian represents the ratio of
    the number of data points.
    """

    def add(
        self,
        series_name: str,
        data_pair: echarts_types.Sequence[echarts_types.Union[echarts_types.Sequence, opts.PieItem, dict]],
        *,
        color: echarts_types.Optional[str] = None,
        color_by: echarts_types.Optional[str] = "data",
        is_legend_hover_link: bool = True,
        selected_mode: echarts_types.Union[str, bool] = False,
        selected_offset: echarts_types.Numeric = 10,
        radius: echarts_types.Optional[echarts_types.Sequence] = None,
        center: echarts_types.Optional[echarts_types.Sequence] = None,
        rosetype: echarts_types.Optional[str] = None,
        is_clockwise: bool = True,
        start_angle: echarts_types.Numeric = 90,
        min_angle: echarts_types.Numeric = 0,
        min_show_label_angle: echarts_types.Numeric = 0,
        is_avoid_label_overlap: bool = True,
        is_still_show_zero_sum: bool = True,
        percent_precision: echarts_types.Numeric = 2,
        is_show_empty_circle: bool = True,
        empty_circle_style_opts: echarts_types.PieEmptyCircle = opts.PieEmptyCircleStyle(),
        label_opts: echarts_types.Label = opts.LabelOpts(),
        label_line_opts: echarts_types.PieLabelLine = opts.PieLabelLineOpts(),
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
        encode: echarts_types.Union[echarts_types.JSFunc, dict, None] = None,
    ):
        if self.options.get("dataset") is not None:
            data = None
            self.options.get("legend")[0].update(
                data=[d[0] for d in self.options.get("dataset")[0].get("source")][1:]
            )
        elif isinstance(data_pair[0], opts.PieItem):
            data = data_pair
        else:
            data = [{"name": n, "value": v} for n, v in data_pair]

            for a, _ in data_pair:
                self.options.get("legend")[0].get("data").append(a)

            _dlst = self.options.get("legend")[0].get("data")
            _dset = list(set(_dlst))
            _dset.sort(key=_dlst.index)
            self.options.get("legend")[0].update(data=list(_dset))

        if not radius:
            radius = ["0%", "75%"]
        if not center:
            center = ["50%", "50%"]

        self._append_color(color)
        self.options.get("series").append(
            {
                "type": ChartType.PIE,
                "name": series_name,
                "colorBy": color_by,
                "legendHoverLink": is_legend_hover_link,
                "selectedMode": selected_mode,
                "selectedOffset": selected_offset,
                "clockwise": is_clockwise,
                "startAngle": start_angle,
                "minAngle": min_angle,
                "minShowLabelAngle": min_show_label_angle,
                "avoidLabelOverlap": is_avoid_label_overlap,
                "stillShowZeroSum": is_still_show_zero_sum,
                "percentPrecision": percent_precision,
                "showEmptyCircle": is_show_empty_circle,
                "emptyCircleStyle": empty_circle_style_opts,
                "data": data,
                "radius": radius,
                "center": center,
                "roseType": rosetype,
                "label": label_opts,
                "labelLine": label_line_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "encode": encode,
            }
        )
        return self
