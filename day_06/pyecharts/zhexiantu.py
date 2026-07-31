import pyecharts.options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Line
from pyecharts.globals import CurrentConfig

# 国内稳定CDN地址，适配所有pyecharts版本
CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"

Line_demo = (
    Line()
    .add_xaxis(Faker.clothes)
    .add_yaxis("商家A", [102,132,105,52,90,111,95],
               symbol='diamond',symbol_size = 15)
    .add_yaxis("商家B", [86,108,128,66,136,122,105],
               symbol='triangle',symbol_size = 15)
    .set_global_opts(title_opts=opts.TitleOpts(title="折线图示例"),
                     yaxis_opts=opts.AxisOpts(
                         name='销售额',
                         name_location='center',
                         name_gap=30
                     )
))
Line_demo.render("line.html")