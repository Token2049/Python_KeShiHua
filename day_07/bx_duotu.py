from pyecharts.charts import Grid, Bar, Line
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig

# 可选：配置国内CDN，防止网页空白
CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"

x = ["小米", "荣耀", "华为", "中兴", "魅族", "vivo", "OPPO"]
A = [107, 36, 102, 91, 51, 113, 45]
B = [104, 60, 33, 138, 105, 111, 91]

bar = Bar().add_xaxis(x).add_yaxis("商家A",A).add_yaxis("商家B",B)\
.set_global_opts(title_opts=opts.TitleOpts(title="组合图表-柱形图"))

line = Line().add_xaxis(x).add_yaxis("商家A",A).add_yaxis("商家B",B)\
.set_global_opts(title_opts=opts.TitleOpts(title="组合图表-折线图"))

grid = (
    Grid()
    .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
    .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
)
grid.render("grid_demo.html")