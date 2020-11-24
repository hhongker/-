'''
任务6中国疫情地图可视化
从地理纬度上可视化分析全国疫情情况，例如从新增确诊，累计确诊，今日治愈，累计治愈，今日死亡，累计死亡，现有重诊，境外输入等指标分析。
'''
import pyecharts.options as opts
from pyecharts.charts import Line, Bar, Map
import pandas as pd

class View():
    
    def __init__(self):

        self.data_pro_tota = pd.DataFrame(pd.read_excel('data\中国各省市(区)总体疫情信息\中国各省市(区)总体疫情信息.xlsx'))
        self.data_pro_newly = pd.DataFrame(pd.read_excel('data\中国各省市(区)总体疫情信息\中国各省市(区)今日新增疫情信息.xlsx'))
        self.data_tota = pd.DataFrame(pd.read_excel('data\中国总体历史疫情信息\历史总体信息.xlsx'))
    #绘制中国累计确诊人数地图
    def china_map_confirm(self):
        map_confirm = (
            Map()
            .add("", [list(z) for z in zip(self.data_pro_tota.name, self.data_pro_tota.confirm)], "china")
            .set_global_opts(title_opts=opts.TitleOpts(title="中国疫情地图（累计确诊人数）"),
                visualmap_opts = opts.VisualMapOpts(is_piecewise = True, pieces=[
                    {"min":10000, "color" : "#4F070D"},
                    {"min": 1000,"max":9999, "color": "#780707"}, # 数据范围分段，分颜色，可以根据数据大小具体分配大小
                    {"min": 500, "max": 999, "color": "#B40404"},
                    {"min": 100, "max": 499, "color": "#CD1111"},
                    {"min": 10, "max": 99,"color": "#F68181"},
                    {"min":1,"max": 9, "color": "#F5A9A9"},
                    {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
                ]))
        )
        return map_confirm

    #新增确诊
    def china_map_NewAddConfirm(self):
        map_NewAddConfirm = (
            Map()
            .add("", [list(z) for z in zip(self.data_pro_newly.name, self.data_pro_newly.confirm)], "china")
            .set_global_opts(title_opts=opts.TitleOpts(title="中国疫情地图（新增确诊人数）"),
                visualmap_opts = opts.VisualMapOpts(is_piecewise = True, pieces=[
                    {"min": 500, "color": "#4F070D"},
                    {"min": 300, "max": 499, "color": "#780707"},  # 数据范围分段，分颜色，可以根据数据大小具体分配大小
                    {"min": 200, "max": 299, "color": "#B40404"},
                    {"min": 100, "max": 199, "color": "#CD1111"},
                    {"min": 1, "max": 99, "color": "#F68181"},
                    {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
                ]))
        )
        return map_NewAddConfirm



    #绘制中国累计治愈人数地图
    def china_map_heal(self):
        map_heal = (
            Map()
            .add("", [list(z) for z in zip(self.data_pro_tota.name, self.data_pro_tota.heal)], "china")
            .set_global_opts(title_opts=opts.TitleOpts(title="中国疫情地图（累计治愈人数）"),
                visualmap_opts = opts.VisualMapOpts(is_piecewise = True, pieces=[
                    {"min": 10000, "color": "#006400"},
                    {"min": 1000, "max": 9999, "color": "#008B00"},  # 数据范围分段，分颜色，可以根据数据大小具体分配大小
                    {"min": 500, "max": 999, "color": "#00CD66"},
                    {"min": 100, "max": 499, "color": "#00EE76"},
                    {"min": 10, "max": 99, "color": "#00FF00"},
                    {"min": 1, "max": 9, "color": "#00FA9A"},
                    {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
                ]))
        )
        return map_heal

    #绘制中国累计死亡人数地图
    def china_map_dead(self):
        map_dead = (
            Map()
            .add("", [list(z) for z in zip(self.data_pro_tota.name, self.data_pro_tota.dead)], "china")
            .set_global_opts(title_opts=opts.TitleOpts(title="中国疫情地图（累计死亡人数）"),
                visualmap_opts = opts.VisualMapOpts(is_piecewise = True, pieces=[
                    {"min": 4000, "color": "#4F070D"},
                    {"min": 2000, "max": 3999, "color": "#780707"},  # 数据范围分段，分颜色，可以根据数据大小具体分配大小
                    {"min": 1000, "max": 1999, "color": "#B40404"},
                    {"min": 500, "max": 999, "color": "#CD1111"},
                    {"min": 100, "max": 499, "color": "#F68181"},
                    {"min": 1, "max": 99, "color": "#F5A9A9"},
                    {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
            
                ]))
        )
        return map_dead

    #绘制中国现存确诊人数地图
    def china_map_nowConfirm(self):
        map_nowConfirm = (
            Map()
            .add("", [list(z) for z in zip(self.data_pro_tota.name, self.data_pro_tota.nowConfirm)], "china")
            .set_global_opts(title_opts=opts.TitleOpts(title="中国疫情地图（现存确诊人数）"),
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=[
                    {"min":10000, "color" : "#4F070D"},
                    {"min": 1000,"max":9999, "color": "#780707"}, # 数据范围分段，分颜色，可以根据数据大小具体分配大小
                    {"min": 500, "max": 999, "color": "#B40404"},
                    {"min": 100, "max": 499, "color": "#CD1111"},
                    {"min": 10, "max": 99,"color": "#F68181"},
                    {"min":1,"max": 9, "color": "#F5A9A9"},
                    {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
                ]))
        )
        return map_nowConfirm


    #绘制中国各省今日新增情况柱状图
    def bar_now(self):
        bar = (
            Bar()
                .add_xaxis(list(self.data_pro_newly.name))
                .add_yaxis("中国各省今日新增疫情情况", list(self.data_pro_newly.confirm))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="中国各省今日新增疫情情况"),
            )
        )
        return bar

    def china_line(self):
        lines = (
            Line()  # 生成line类型图表
                .add_xaxis(list(self.data_tota.date))  # 添加x轴
                .add_yaxis('确诊人数', list(self.data_tota.confirm), label_opts=opts.LabelOpts(is_show=True),is_smooth=True)
                .add_yaxis('死亡人数', list(self.data_tota.dead), label_opts=opts.LabelOpts(is_show=True),is_smooth=True)
                .add_yaxis('治愈人数', list(self.data_tota.heal), label_opts=opts.LabelOpts(is_show=True),is_smooth=True)
                .set_global_opts(title_opts=opts.TitleOpts(title='中国累计确诊人数线形图'))
        )
        return lines

    #调用函数
    def get_china_map_confirm(self):
        m = self.china_map_confirm()
        return m.render("cn_map_view\中国疫情地图（累计确诊人数）.html")

    def get_china_map_NewAddConfirm(self):
        m = self.china_map_NewAddConfirm()
        return m.render("cn_map_view\中国疫情地图（新增确诊人数）.html")

    def get_china_map_nowConfirm(self):
        m = self.china_map_nowConfirm()
        return m.render("cn_map_view\中国疫情地图（现存确诊人数）.html")


    def get_china_map_heal(self):
        m = self.china_map_heal()
        return m.render("cn_map_view\中国疫情地图（累计治愈人数）.html")

    def get_china_map_dead(self):
        m = self.china_map_dead()
        return m.render("cn_map_view\中国疫情地图（累计死亡人数）.html")

    def get_bar_now(self):
        b = self.bar_now()
        return b.render("cn_map_view\中国各省今日新增疫情情况.html")

    def get_china_line(self):
        l = self.china_line()
        return l.render("cn_map_view\中国累计确诊人数线形图.html")


    def main(self):
        self.get_china_map_confirm()
        self.get_china_map_nowConfirm()
        self.get_china_map_NewAddConfirm()
        self.get_china_map_heal()
        self.get_china_map_dead()
        self.get_bar_now()
        self.get_china_line()


if __name__ == '__main__':
    map = View()
    map.main()