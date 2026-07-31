import pyecharts.options as opts
from pyecharts.charts import Pie
from pyecharts.globals import CurrentConfig

# 国内稳定CDN地址，适配所有pyecharts版本
CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"

pie_demo = (
    Pie()
    .add('', [('小米',150),('苹果',200),('华为',300),
              ('oppo',400),('vivo',500),('魅族',600)],radius = [90,160])
              .set_global_opts(title_opts = opts.TitleOpts(title = '饼图示例'))
)
pie_demo.render('yuanhuantu.html')