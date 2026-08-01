import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Pie, Line, Page
from pyecharts.globals import CurrentConfig

# 可选：配置国内CDN，防止网页空白
CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"

pie_hupu = (
    Pie()
    .add("", [('NBA', 232345), ('CBA', 16976), ('国际足球', 44381),
              ('中国足球', 124), ('步行街', 512266), ('游戏电竞', 129065),
              ('自建板块', 3805), ('运动装备', 35124), ('综合体育', 4454),
              ('虎扑社团', 646), ('站务管理', 34467)],
         center=["50%", "50%"], radius=[100, 160])
    .set_global_opts(title_opts=opts.TitleOpts(title="虎扑社区各板块发帖数"),
                     legend_opts=opts.LegendOpts(pos_left=10,
                                                pos_top=80, orient='vertical'))
)

line_hupu = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
    .add_xaxis(['{}:00'.format(num) for num in range(24) if num%2==0])
    .add_yaxis('NBA', [259, 114, 134, 397, 840, 1577, 1413, 713,
                       647, 448, 462, 514], symbol='diamond', symbol_size=15)
    .add_yaxis('虎扑', [1221, 370, 359, 845, 2270, 3582, 2947, 2215,
                       2106, 1843, 2045, 2178], symbol='triangle', symbol_size=15)
    .set_global_opts(title_opts=opts.TitleOpts(
        title="虎扑社区和NBA板块24小时发帖数"),
        yaxis_opts=opts.AxisOpts(name="发帖数(个)",
                                 name_location="center", name_gap=40))
)

page = Page(page_title="虎扑社区数据分析", interval=2)
page.add(pie_hupu, line_hupu)

page.render("虎扑社区分析.html")