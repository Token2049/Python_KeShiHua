from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.globals import CurrentConfig

# 可选：配置国内CDN，防止网页空白
CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"

x_data = ["小米", "荣耀", "华为", "中兴", "魅族", "vivo", "OPPO"]
y_a = [107, 36, 102, 91, 51, 113, 45]
y_b = [104, 60, 33, 138, 105, 111, 91]
bar = (
    # 创建Bar类的对象，修改图表的主题
    Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
    .add_xaxis(x_data)
    .add_yaxis("商家A", y_a)
    .add_yaxis("商家B", y_b)
    .set_global_opts(title_opts=opts.TitleOpts(title="柱形图-ROMA主题"),
                     yaxis_opts=opts.AxisOpts(name="销售额(万元)",
                     name_location="center", name_gap=30))
)
bar.render('bar_theme.html')