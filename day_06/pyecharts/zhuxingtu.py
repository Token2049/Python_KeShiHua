from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig

# 国内稳定CDN地址，适配所有pyecharts版本
CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"

bar = Bar(init_opts=opts.InitOpts(width='600px', height='300px'))

bar.add_xaxis(Faker.clothes)
bar.add_yaxis('商家A', [5,20,36,10,75,90,50])

bar.set_global_opts(
    title_opts=opts.TitleOpts(title='柱形图'),
    yaxis_opts=opts.AxisOpts(
        name='销售额',
        name_location='center',
        name_gap=30
    )
)

bar.set_series_opts(label_opts=opts.LabelOpts(position='top'))

bar.render("bar.html")