from ... import echarts_types
from ...charts.chart import ThreeAxisChart
from ...globals import ChartType
from ...options import InitOpts, RenderOpts


class Scatter3D(ThreeAxisChart):
    """
    <<< 3D Scatter-Chart >>>
    """

    def __init__(
        self,
        init_opts: echarts_types.Init = InitOpts(),
        render_opts: echarts_types.RenderInit = RenderOpts(),
    ):
        super().__init__(init_opts, render_opts)
        self._3d_chart_type = ChartType.SCATTER3D