import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Scatter
from pyecharts.globals import CurrentConfig

CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"

scatter_demo = (
    Scatter()
    .add_xaxis(np.arange(1,21).tolist())
    .add_yaxis('',np.random.randint(10,40,20).tolist())
    .set_global_opts(title_opts = opts.TitleOpts(title = '散点图示例'),
                     yaxis_opts = opts.AxisOpts(name = 'y轴',name_location = 'center',name_gap = 30),
                     xaxis_opts = opts.AxisOpts(name = 'x轴',name_location = 'center',name_gap = 30))
)
scatter_demo.render('scatter.html')