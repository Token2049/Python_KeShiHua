from pyecharts.charts import Page, Bar, Line
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig

# 可选：配置国内CDN，防止网页空白
CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"

x_data = ["小米", "荣耀", "华为", "中兴", "魅族", "vivo", "OPPO"]
sellerA = [107, 36, 102, 91, 51, 113, 45]
sellerB = [104, 60, 33, 138, 105, 111, 91]

bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis("商家A", sellerA)
    .add_yaxis("商家B", sellerB)
    .set_global_opts(title_opts=opts.TitleOpts(title="组合图表-柱形图"))
)
line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis("商家A", sellerA)
    .add_yaxis("商家B", sellerB)
    .set_global_opts(title_opts=opts.TitleOpts(title="组合图表-折线图"))
)

page = Page(page_title="顺序多图", interval=2)
page.add(bar, line)

page.render("page顺序多图.html")