from pyecharts.charts import Bar3D
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig
import numpy as np

# 国内CDN
CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"

data = [(i, j, np.random.randint(0, 20)) for i in range(7) for j in range(5)]

bar_3d = (
    Bar3D()
    .add(
        series_name="",
        data=[[d[1], d[0], d[2]] for d in data], 
        xaxis3d_opts=opts.Axis3DOpts(["A组", "B组", "C组", "D组", "E组"]),
        yaxis3d_opts=opts.Axis3DOpts(["周一", "周二", "周三", "周四", "周五", "周六", "周日"]),
        zaxis3d_opts=opts.Axis3DOpts(name="数值")
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=20),
        title_opts=opts.TitleOpts(title="3D 柱状图示例")
    )
)
bar_3d.render("bar_3d.html")