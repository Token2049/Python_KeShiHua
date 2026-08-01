from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import CurrentConfig

# 可选：配置国内CDN，防止网页空白
CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"

tl = Timeline()
tl.add_schema(symbol="diamond", symbol_size=15, is_auto_play=True)

for year in range(2020, 2025):
    bar = (
        Bar()
        .add_xaxis(Faker.clothes)
        .add_yaxis("", Faker.values())
        .set_global_opts(yaxis_opts=opts.AxisOpts(name="销售额(万元)",
                        name_location="center", name_gap=30))
    )
    tl.add(bar, "{}年".format(year))

tl.render("timeline_bar.html")