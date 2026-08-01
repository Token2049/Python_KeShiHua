from pyecharts.charts import Sankey
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig

# 可选：配置国内CDN，防止网页空白
CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"

nodes = [
    {"name": "消费者"},
    {"name": "老客户"},
    {"name": "新客户"},
    {"name": "衬衫"},
    {"name": "运动鞋"},
    {"name": "连衣裙"},
    {"name": "高跟鞋"},
]

links = [
    {"source": "消费者", "target": "老客户", "value": 30},
    {"source": "消费者", "target": "新客户", "value": 20},

    {"source": "老客户", "target": "衬衫", "value": 10},
    {"source": "老客户", "target": "运动鞋", "value": 20},

    {"source": "新客户", "target": "连衣裙", "value": 10},
    {"source": "新客户", "target": "高跟鞋", "value": 10},
]

sankey_demo = (
    Sankey()
    .add(
        "",
        nodes=nodes,
        links=links,
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="right")
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="桑基图示例")
    )
)

sankey_demo.render("sankey_demo.html")