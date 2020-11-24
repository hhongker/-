'''
任务6中国疫情地图可视化
从地理纬度上可视化分析全国疫情情况，例如从新增确诊，累计确诊，今日治愈，累计治愈，今日死亡，累计死亡，现有重诊，境外输入等指标分析。
'''
import pyecharts.options as opts
from pyecharts.charts import Line, Bar, Map
import pandas as pd
from pyecharts.charts import Page#将所有图像放在同一页所需要的库
from util import dealWithFile as dwf

readPath = dwf.rootPath #读取数据的地方
savaPath = dwf.saveDataCnMapView #生成结果的地方
flag = dwf.flag #是否生成的数据



data_pro_tota = pd.DataFrame(pd.read_excel(readPath+'/中国各省市总体疫情信息/中国各省市总体疫情信息.xlsx'))
data_pro_newly = pd.DataFrame(pd.read_excel(readPath+'/中国各省市总体疫情信息/中国各省市(区)今日新增疫情信息.xlsx'))
data_tota = pd.DataFrame(pd.read_excel(readPath+'/中国总体历史疫情信息/历史总体信息.xlsx'))
page=Page()#创建一个分页用于放所有的图像在这一分页上
#绘制中国累计确诊人数地图
def china_map_confirm():

    map_confirm = (
        Map()
        .add("", [list(z) for z in zip(data_pro_tota.name, data_pro_tota.confirm)], "china")
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
    page.add(map_confirm)  # 将图像加入同一页
    if flag: dwf.write_to_file(savaPath+'/中国疫情地图（累计确诊人数）.txt',str(map_confirm.dump_options_with_quotes()))
    return map_confirm

#新增确诊
def china_map_NewAddConfirm():

    map_NewAddConfirm = (
        Map()
        .add("", [list(z) for z in zip(data_pro_newly.name, data_pro_newly.confirm)], "china")
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
    page.add(map_NewAddConfirm)  # 将图像加入同一页
    if flag: dwf.write_to_file(savaPath + '/中国疫情地图（新增确诊人数）.txt', str(map_NewAddConfirm.dump_options_with_quotes()))
    return map_NewAddConfirm



#绘制中国累计治愈人数地图
def china_map_heal():

    map_heal = (
        Map()
        .add("", [list(z) for z in zip(data_pro_tota.name, data_pro_tota.heal)], "china")
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
    page.add(map_heal)  # 将图像加入同一页
    if flag: dwf.write_to_file(savaPath + '/中国疫情地图（累计治愈人数）.txt', str(map_heal.dump_options_with_quotes()))
    return map_heal

#绘制中国累计死亡人数地图
def china_map_dead():
    map_dead = (
        Map()
        .add("", [list(z) for z in zip(data_pro_tota.name, data_pro_tota.dead)], "china")
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
    page.add(map_dead)  # 将图像加入同一页
    if flag: dwf.write_to_file(savaPath + '/中国疫情地图（累计死亡人数）.txt', str(map_dead.dump_options_with_quotes()))
    return map_dead

#绘制中国现存确诊人数地图
def china_map_nowConfirm():
    map_nowConfirm = (
        Map()
        .add("", [list(z) for z in zip(data_pro_tota.name, data_pro_tota.nowConfirm)], "china")
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
    page.add(map_nowConfirm)  # 将图像加入同一页
    if flag: dwf.write_to_file(savaPath + '/中国疫情地图（现存确诊人数）.txt', str(map_nowConfirm.dump_options_with_quotes()))
    return map_nowConfirm


#绘制中国各省今日新增情况柱状图
def bar_now():
    bar = (
        Bar()
            .add_xaxis(list(data_pro_newly.name))
            .add_yaxis("中国各省今日新增疫情情况", list(data_pro_newly.confirm))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="中国各省今日新增疫情情况"),
        )
    )
    page.add(bar)  # 将图像加入同一页
    if flag: dwf.write_to_file(savaPath + '/中国各省今日新增疫情情况.txt', str(bar.dump_options_with_quotes()))
    return bar

def china_line():
    lines = (
        Line()  # 生成line类型图表
            .add_xaxis(list(data_tota.date))  # 添加x轴
            .add_yaxis('确诊人数', list(data_tota.confirm), label_opts=opts.LabelOpts(is_show=True),is_smooth=True)
            .add_yaxis('死亡人数', list(data_tota.dead), label_opts=opts.LabelOpts(is_show=True),is_smooth=True)
            .add_yaxis('治愈人数', list(data_tota.heal), label_opts=opts.LabelOpts(is_show=True),is_smooth=True)
            .set_global_opts(title_opts=opts.TitleOpts(title='中国累计确诊人数线形图'))
    )
    page.add(lines)  # 将图像加入同一页
    if flag: dwf.write_to_file(savaPath + '/中国累计确诊人数线形图.txt', str(lines.dump_options_with_quotes()))
    return lines




def main():
    dwf.createFile(readPath)
    dwf.createFile(savaPath)
    china_map_confirm()
    china_map_NewAddConfirm()
    china_map_heal()
    china_map_dead()
    china_map_nowConfirm()
    bar_now()
    china_line()
    return page.render(savaPath + '/analyse_all.html')  # 生成包含所有图像的网页并存放在analyse_all.html


if __name__ == '__main__':
    main()