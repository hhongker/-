# encoding: utf-8
from translate import Translator
import pyecharts.options as opts
from pyecharts.charts import Map, Timeline
import os
import pandas as pd

class Time():
    def __init__(self):
        self.file = os.getcwd()  # 读取当前文件路径
        self.path = self.file + '\\world_map_view'
        isExists = os.path.exists(self.path)  # 判断当前目录是否有文件夹world_map_view，如果没有则创建
        if not isExists:
            os.mkdir(self.path)  # 在当前路径创建新文件夹world_map_view,用于存放生成的图像数据

    def Countrytotalsynthesis(self):
        path = self.file + '\\data\\各国历史疫情信息'
        Filelist = []
        for home, dirs, files in os.walk(path):
            for filename in files:
                Filelist.append(filename)
        data_total = pd.read_excel('data/各国历史疫情信息/%s' % (Filelist[0]), index=False)
        translator = Translator(from_lang="chinese", to_lang="english")
        j = Filelist[0][:-5]   # 载入第一张表作为总表，并翻译
        if j == '美国':
            j = 'United States'
        elif j == '英国':
            j = 'United Kingdom'
        elif j == '智利':
            j = 'Chile'
        elif j == '韩国':
            j = 'Korea'
        elif j == '哥伦比亚':
            j = 'Colombia'
        elif j == '叙利亚':
            j = 'Syria'
        elif j == '刚果（金）':
            j = 'Dem. Rep. Congo'
        elif j == '瑞典':
            j = 'Sweden'
        elif j == '刚果（布）':
            j = 'Congo'
        elif j == '中非共和国':
            j = 'Central African Rep.'
        elif j == '苏丹':
            j = 'S. Sudan'
        else:  # 利用translator库进行翻译
            translator = Translator(from_lang="chinese", to_lang="english")
            j = translator.translate(j)
        data_total['country'] = j

        for i in Filelist:  # 遍历所有表格，并加入第一张表，翻译
            if i == Filelist[0]:
                continue
            else:
                data = pd.read_excel('data/各国历史疫情信息/%s' % (i), index=False)
                j = i[:-5]
                if j == '美国':
                    j = 'United States'
                elif j == '英国':
                    j = 'United Kingdom'
                elif j == '智利':
                    j = 'Chile'
                elif j == '韩国':
                    j = 'Korea'
                elif j == '哥伦比亚':
                    j = 'Colombia'
                elif j == '叙利亚':
                    j = 'Syria'
                elif j == '刚果（金）':
                    j = 'Dem. Rep. Congo'
                elif j == '瑞典':
                    j = 'Sweden'
                elif j == '刚果（布）':
                    j = 'Congo'
                elif j == '中非共和国':
                    j = 'Central African Rep.'
                elif j == '苏丹':
                    j = 'S. Sudan'
                else:  # 利用translator库进行翻译
                    translator = Translator(from_lang="chinese", to_lang="english")
                    j = translator.translate(j)
                data['country'] = j
                data_total = data_total.append(data)
        data_total.to_excel('world_map_view/世界各国合成表.xlsx', index=False)

    def Chinaprovince(self):
        path = self.file + '\\data\\中国各省市(区)历史疫情信息'
        Filelist = []
        for home, dirs, files in os.walk(path):
            for filename in files:
                Filelist.append(filename)
        data_total = pd.read_excel('data/中国各省市(区)历史疫情信息/%s' % (Filelist[0]), index=False)
        j = Filelist[0][:-5]
        data_total['country'] = j

        for i in Filelist:
            if i == Filelist[0]:
                continue
            else:
                data = pd.read_excel('data/中国各省市(区)历史疫情信息/%s' % (i), index=False)
                j = i[:-5]
                data['country'] = j
                data_total = data_total.append(data)
        data_total.to_excel('world_map_view/中国各省市(区)合成表.xlsx', index=False)

    def Worldtime(self):
        data = pd.read_excel('world_map_view/世界各国合成表.xlsx', index_col=False)
        data['date'] = str('2020/') + data['date']
        data['date'] = pd.to_datetime(data['date'])
        data['date'] = pd.PeriodIndex(data['date'], freq='D')  # 转换为时间
        class_list = list(data['date'].drop_duplicates())
        self.path = self.file + '\\world_map_view\\世界各国时间轴'
        isExists = os.path.exists(self.path)  # 判断当前目录是否有世界各国时间轴文件夹，如果没有则创建
        if not isExists:
            os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
        for i in class_list:
            data1 = data[data['date'] == i]
            data1.to_excel('world_map_view/世界各国时间轴/%s.xlsx' % (i), index=False)  # 根据时间拆分数据，并写出

    def Chinatime(self):
        data = pd.read_excel('world_map_view/中国各省市(区)合成表.xlsx', index_col=False)
        data['date'] = str('2020/') + data['date']
        data['date'] = pd.to_datetime(data['date'])
        data['date'] = pd.PeriodIndex(data['date'], freq='D')  # 转换为时间
        class_list = list(data['date'].drop_duplicates())
        self.path = self.file + '\\world_map_view\\中国时间轴'
        isExists = os.path.exists(self.path)  # 判断当前目录是否有中国时间轴文件夹，如果没有则创建
        if not isExists:
            os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
        for i in class_list:
            data1 = data[data['date'] == i]
            data1.to_excel('world_map_view/中国时间轴/%s.xlsx' % (i), index=False)  # 根据时间拆分数据，并写出

    def WorldMaptime(self):
        data = pd.read_excel('world_map_view/世界各国合成表.xlsx', index_col=False)
        data['date'] = str('2020/') + data['date']
        data['date'] = pd.to_datetime(data['date'])
        data['date'] = pd.PeriodIndex(data['date'], freq='D')  # 转换为时间
        class_list = list(data['date'].drop_duplicates())
        class_list = sorted(class_list)
        t1 = Timeline()
        for i in class_list:
            data1 = pd.read_excel('world_map_view/世界各国时间轴/%s.xlsx' % (i), index=False)
            data_name = data1['country']
            data_confirm = data1['confirm']
            chinaMap = (
                Map()
                    .add("累计确诊", [list(z) for z in zip(data_name, data_confirm)], maptype="world")
                    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title="{}世界累计确诊数据".format(i)),
                    visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                      pieces=[{"max": 0, "label": '0人', "color": "#FFFAFA"},
                                                              {"min": 1, "max": 9, "label": '1-9人', "color": "#F08080"},
                                                              {"min": 10, "max": 99, "label": '10-99人', "color": "#BC8F8F"},
                                                              {"min": 100, "max": 499, "label": '100-499人', "color": "#A52A2A"},
                                                              {"min": 500, "max": 999, "label": '500-999人', "color": "#B22222"},
                                                              {"min": 1000, "max": 9999, "label": '1000-9999人', "color": "#8B0000"},
                                                              {"min": 10000, "label": '10000人及以上', "color": "#800000"}]),
                )
            )
            t1.add(chinaMap, "".format(i))
        self.path = self.file + '\\world_map_view\\时间轴图像'
        isExists = os.path.exists(self.path)  # 判断当前目录是否有时间轴图像文件夹，如果没有则创建
        if not isExists:
            os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
        t1.render('world_map_view/时间轴图像/世界总体疫情变化.html')

    def ChinaMaptime(self):
        data = pd.read_excel('world_map_view/中国各省市(区)合成表.xlsx', index_col=False)
        data['date'] = str('2020/') + data['date']
        data['date'] = pd.to_datetime(data['date'])
        data['date'] = pd.PeriodIndex(data['date'], freq='D')  # 转换为时间
        class_list = list(data['date'].drop_duplicates())
        class_list = sorted(class_list)
        t1 = Timeline()
        for i in class_list:
            data1 = pd.read_excel('world_map_view/中国时间轴/%s.xlsx' % (i), index=False)
            data_name = data1['country']
            data_confirm = data1['confirm']
            chinaMap = (
                Map()
                    .add("累计确诊", [list(z) for z in zip(data_name, data_confirm)], maptype="china")
                    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title="{}世界累计确诊数据".format(i)),
                    visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                      pieces=[{"max": 0, "label": '0人', "color": "#FFFAFA"},
                                                              {"min": 1, "max": 9, "label": '1-9人', "color": "#F08080"},
                                                              {"min": 10, "max": 99, "label": '10-99人', "color": "#BC8F8F"},
                                                              {"min": 100, "max": 499, "label": '100-499人', "color": "#A52A2A"},
                                                              {"min": 500, "max": 999, "label": '500-999人', "color": "#B22222"},
                                                              {"min": 1000, "max": 9999, "label": '1000-9999人', "color": "#8B0000"},
                                                              {"min": 10000, "label": '10000人及以上', "color": "#800000"}]),
                )
            )
            t1.add(chinaMap, "".format(i))
        self.path = self.file + '\\world_map_view\\时间轴图像'
        isExists = os.path.exists(self.path)  # 判断当前目录是否有时间轴图像文件夹，如果没有则创建
        if not isExists:
            os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
        t1.render('world_map_view/时间轴图像/中国总体疫情变化.html')
        
    def ChinatotalMap(self):  # 中国总体地理图
        data = pd.read_excel('data/中国各省市(区)总体疫情信息/中国各省市(区)总体疫情信息.xlsx', index_col=False)
        data_name = data['name']
        data_confirm = data['confirm']
        chinaMap = (
            Map()
                .add('', [list(z) for z in zip(data_name, data_confirm)], maptype='china')
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="中国各省市(区)总体累计确诊数据"),
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                  pieces=[{"max": 0, "label": '0人', "color": "#FFFAFA"},
                                                          {"min": 1, "max": 9, "label": '1-9人', "color": "#F08080"},
                                                          {"min": 10, "max": 99, "label": '10-99人', "color": "#BC8F8F"},
                                                          {"min": 100, "max": 499, "label": '100-499人', "color": "#A52A2A"},
                                                          {"min": 500, "max": 999, "label": '500-999人', "color": "#B22222"},
                                                          {"min": 1000, "max": 9999, "label": '1000-9999人',
                                                           "color": "#8B0000"},
                                                          {"min": 10000, "label": '10000人及以上', "color": "#800000"}]),
            )
        )
        self.path = self.file + '\\world_map_view\\中国各省市(区)总体疫情信息'
        isExists = os.path.exists(self.path)  # 判断当前目录是否有中国各省市(区)总体疫情信息文件夹，如果没有则创建
        if not isExists:
            os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
        chinaMap.render('world_map_view/中国各省市(区)总体疫情信息/中国各省市(区)总体疫情信息.html')
    
    def ChinanowdayMap(self):  # 中国今日地理图
        data = pd.read_excel('data/中国各省市(区)总体疫情信息/中国各省市(区)今日新增疫情信息.xlsx', index_col=False)
        data_name = data['name']
        data_confirm = data['confirm']
        chinaMap = (
            Map()
                .add('', [list(z) for z in zip(data_name, data_confirm)], maptype='china')
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_series_opts()
                .set_global_opts(
                title_opts=opts.TitleOpts(title="中国各省市(区)今日新增疫情信息"),
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                  pieces=[{"max": 0, "label": '0人', "color": "#FFFAFA"},
                                                          {"min": 1, "max": 9, "label": '1-9人', "color": "#F08080"},
                                                          {"min": 10, "max": 99, "label": '10-99人', "color": "#BC8F8F"},
                                                          {"min": 100, "max": 499, "label": '100-499人', "color": "#A52A2A"},
                                                          {"min": 500, "max": 999, "label": '500-999人', "color": "#B22222"},
                                                          {"min": 1000, "max": 9999, "label": '1000-9999人',
                                                           "color": "#8B0000"},
                                                          {"min": 10000, "label": '10000人及以上', "color": "#800000"}]),
            )
        )
        self.path = self.file + '\\world_map_view\\中国各省市(区)总体疫情信息'
        isExists = os.path.exists(self.path)  # 判断当前目录是否有中国各省市(区)总体疫情信息文件夹，如果没有则创建
        if not isExists:
            os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
        chinaMap.render('world_map_view/中国各省市(区)总体疫情信息/中国各省市(区)今日新增疫情信息.html')
    
    def ProvincecityMap(self):  # 画出所有地区的累计确诊、疑似病例、新增确诊等6个特征的地理图(其实我也不想画那么多的，555)。
        path = self.file+'\\data\\中国各省市(区)疫情信息'
        self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息'
        isExists = os.path.exists(self.path)  # 判断当前目录是否有中国各省市(区)疫情信息文件夹，如果没有则创建
        if not isExists:
            os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
        Filelist = []
        for home, dirs, files in os.walk(path):
            for filename in files:
                Filelist.append(filename)
        print(Filelist)
        for i in Filelist:
                if i == '北京' or i == '上海' or i == '重庆' or i == '天津' or i == '澳门'or i == '香港':
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['confirm']
                    for z in data_name1:
                        z = z + str('区')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"累计确诊数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\累计确诊'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/累计确诊/%s' % (j)+'.html')
                else:
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['confirm']
                    for z in data_name1:
                        z = z + str('市')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"确诊数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\累计确诊'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/累计确诊/%s' % (j)+'.html')

        for i in Filelist:
                if i == '北京' or i == '上海' or i == '重庆' or i == '天津' or i == '澳门'or i == '香港':
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['nowConfirm']
                    for z in data_name1:
                        z = z + str('区')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"新增确诊数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\新增确诊'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/新增确诊/%s' % (j)+'.html')
                else:
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['nowConfirm']
                    for z in data_name1:
                        z = z + str('市')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"新增确诊数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\新增确诊'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/新增确诊/%s' % (j)+'.html')

        for i in Filelist:
                if i == '北京' or i == '上海' or i == '重庆' or i == '天津' or i == '澳门'or i == '香港':
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['suspect']
                    for z in data_name1:
                        z = z + str('区')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"疑似病例数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\疑似病例'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/疑是病例/%s' % (j)+'.html')
                else:
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['suspect']
                    for z in data_name1:
                        z = z + str('市')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"疑似病例数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\疑是病例'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/疑是病例/%s' % (j)+'.html')
        for i in Filelist:
                if i == '北京' or i == '上海' or i == '重庆' or i == '天津' or i == '澳门'or i == '香港':
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['dead']
                    for z in data_name1:
                        z = z + str('区')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"累计死亡数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\累计死亡'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/累计死亡/%s' % (j)+'.html')
                else:
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['dead']
                    for z in data_name1:
                        z = z + str('市')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"累计死亡数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\累计死亡'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/累计死亡/%s' % (j)+'.html')

        for i in Filelist:
                if i == '北京' or i == '上海' or i == '重庆' or i == '天津' or i == '澳门'or i == '香港':
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['heal']
                    for z in data_name1:
                        z = z + str('区')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"累计治愈数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\累计治愈'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/累计治愈/%s' % (j)+'.html')
                else:
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['heal']
                    for z in data_name1:
                        z = z + str('市')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"累计治愈数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\累计治愈'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/累计治愈/%s' % (j)+'.html')

        for i in Filelist:
                if i == '北京' or i == '上海' or i == '重庆' or i == '天津' or i == '澳门'or i == '香港':
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['importedCase']
                    for z in data_name1:
                        z = z + str('区')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"境外输入数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\境外输入'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/境外输入/%s' % (j)+'.html')
                else:
                    data = pd.read_excel('data/中国各省市(区)疫情信息/%s' % (i), index_col=False)
                    data.columns

                    data_name1 = data['name']
                    data_name = []
                    data_confirm = data['importedCase']
                    for z in data_name1:
                        z = z + str('市')
                        data_name.append(z)
                        print(z)
                    j = i[:-5]
                    chinaMap = (
                        Map()
                            .add("", [list(z) for z in zip(data_name, data_confirm)], maptype=j)
                            .set_global_opts(
                            title_opts=opts.TitleOpts(title="%s" % (j)+"境外输入数据"),
                            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                              pieces=[{"max": 0, "label": '0人'},
                                                                      {"min": 1, "max": 9, "label": '1-9人'},
                                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                                      {"min": 10000, "label": '10000人及以上'}]),
                        )
                    )
                    self.path = self.file + '\\world_map_view\\中国各省市(区)疫情信息\\境外输入'
                    isExists = os.path.exists(self.path)  # 判断当前目录是否有各国历史信息文件夹，如果没有则创建
                    if not isExists:
                        os.mkdir(self.path)  # 在当前路径创建新文件夹analisis,用于存放生成的图像数据
                    chinaMap.render('world_map_view/中国各省市(区)疫情信息/境外输入/%s' % (j)+'.html')
    def main(self):
        self.Countrytotalsynthesis()
        self.Chinaprovince()
        self.Worldtime()
        self.Chinatime()
        self.WorldMaptime()
        self.ChinaMaptime()
        self.ChinatotalMap()
        self.ChinanowdayMap()
        self.ProvincecityMap()

if __name__=='__main__':
    time = Time()
    time.main()

