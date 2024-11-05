import base64
import random
from pathlib import Path

from ... import options as opts
from ... import echarts_types
from ...charts.chart import Chart
from ...commons.utils import JsCode
from ...exceptions import WordCloudMaskImageException
from ...globals import ChartType

SHAPES = ("cardioid", "diamond", "triangle-forward", "triangle", "pentagon", "star")


def gen_color():
    """
    generate random color for WordCloud
    """
    return "rgb(%s,%s,%s)" % (
        random.randint(0, 160),
        random.randint(0, 160),
        random.randint(0, 160),
    )


class WordCloud(Chart):
    """
    <<< WordCloud >>>

    Word cloud is to visually highlight the keywords that
    appear frequently in the text.
    """

    def __init__(
        self,
        init_opts: echarts_types.Init = opts.InitOpts(),
        render_opts: echarts_types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.js_dependencies.add("echarts-wordcloud")
        self._mask_image_suffix: echarts_types.Sequence = ["jpg", "jpeg", "png", "ico"]

    def _create_mask_image_variable(self, data: str) -> JsCode:
        image_str = self._encode_image_to_base64(image_or_path=data)
        if image_str is None:
            raise WordCloudMaskImageException(data=data)
        current_chart_id = self.chart_id
        self.add_js_funcs(
            f"""
        var maskImage_{current_chart_id} = new Image();
        maskImage_{current_chart_id}.src = '{image_str}';
        """
        )
        return JsCode(f"maskImage_{current_chart_id}")

    def _encode_image_to_base64(self, image_or_path: str) -> echarts_types.Optional[str]:
        try:
            # 尝试判断是否为图片路径(base64 长度很长会导致 Pathlib 会异常)
            is_image_file = Path(image_or_path).is_file()
            is_image_file_exist = Path(image_or_path).exists()
            if is_image_file and is_image_file_exist:
                ext = Path(image_or_path).suffix[1:]
                if ext in self._mask_image_suffix:
                    with open(Path(image_or_path), "rb") as f:
                        data = base64.b64encode(f.read()).decode()
                        image_str = f"data:image/{ext};base64,{data}"
                    return image_str
        except OSError:
            return image_or_path

    def add(
        self,
        series_name: str,
        data_pair: echarts_types.Sequence,
        *,
        shape: str = "circle",
        mask_image: echarts_types.Optional[str] = None,
        word_gap: echarts_types.Numeric = 20,
        word_size_range: echarts_types.Optional[echarts_types.Sequence] = None,
        rotate_step: echarts_types.Numeric = 45,
        pos_left: echarts_types.Optional[str] = None,
        pos_top: echarts_types.Optional[str] = None,
        pos_right: echarts_types.Optional[str] = None,
        pos_bottom: echarts_types.Optional[str] = None,
        width: echarts_types.Optional[str] = None,
        height: echarts_types.Optional[str] = None,
        is_draw_out_of_bound: bool = False,
        tooltip_opts: echarts_types.Tooltip = None,
        itemstyle_opts: echarts_types.ItemStyle = None,
        textstyle_opts: echarts_types.TextStyle = None,
        emphasis_shadow_blur: echarts_types.Optional[echarts_types.Numeric] = None,
        emphasis_shadow_color: echarts_types.Optional[str] = None,
    ):
        data = []
        for n, v in data_pair:
            data.append({"name": n, "value": v, "textStyle": {"color": gen_color()}})

        word_size_range = word_size_range or (12, 60)

        _rmin, _rmax = -90, 90
        # 确保设置的形状有效，单词的旋转角度应该设置在 [-90, 90]
        if shape in SHAPES:
            _rmin = _rmax = 0
        else:
            shape = "circle"

        if mask_image is not None:
            shape = None
            mask_image = self._create_mask_image_variable(data=mask_image)

        self.options.get("series").append(
            {
                "type": ChartType.WORDCLOUD,
                "name": series_name,
                "shape": shape,
                "maskImage": mask_image,
                "rotationRange": [_rmin, _rmax],
                "rotationStep": rotate_step,
                "girdSize": word_gap,
                "sizeRange": word_size_range,
                "data": data,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "left": pos_left,
                "right": pos_right,
                "top": pos_top,
                "bottom": pos_bottom,
                "width": width,
                "height": height,
                "drawOutOfBound": is_draw_out_of_bound,
                "textStyle": {
                    "normal": textstyle_opts,
                    "emphasis": {
                        "shadowBlur": emphasis_shadow_blur,
                        "shadowColor": emphasis_shadow_color,
                    },
                },
            }
        )
        return self
