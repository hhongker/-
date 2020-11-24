import pandas as pd
import numpy as np
import os,glob,re,random
from pyecharts.charts import Line,Bar,Pie#折线图绘制所需要的库
import pyecharts.options as opts#设置全局变量

from pyecharts.charts import Page#将所有图像放在同一页所需要的库
from util import dealWithFile as dwf

readPath = dwf.rootPath #读取数据的地方
savaPath = dwf.saveDaliyChangeView #生成结果的地方
flag = dwf.flag #是否生成数据


page=Page()#创建一个分页用于放所有的图像在这一分页上
##################中国历史疫情总体信息##############
def china_history_all():

    China_all = pd.DataFrame(pd.read_excel(readPath+'/中国总体历史疫情信息/历史总体信息.xlsx'))  # 读取信息
    CNday_date = list(China_all['date'])
    CNday_confirm = list(China_all['confirm'])
    CNday_dead = list(China_all['dead'])
    CNday_heal = list(China_all['heal'])
    line_CNday = (
        Line()
            .add_xaxis(xaxis_data=CNday_date)  # xaxis_data为x轴，y_axis为y轴
            .add_yaxis(series_name='确诊', y_axis=CNday_confirm, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='死亡', y_axis=CNday_dead, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='治愈', y_axis=CNday_heal, label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='中国疫情历史总体信息', pos_left='50%', pos_top='10%'),
                             tooltip_opts=opts.TooltipOpts(axis_pointer_type='cross'))
    )
    # 创建折线图
    # line_CNday.render(savaPath + '\\中国疫情历史总体信息.html')  # 将生成的图像保存为html文件并存放在photo文件夹
    page.add(line_CNday)  # 将图像加入同一页
    if flag:
        dwf.write_to_file(savaPath + '/中国疫情历史总体信息.txt', str(line_CNday.dump_options_with_quotes()))
    return line_CNday

####################中国各省境外输入汇总###########################
def china_provinces_imports():

    path1 = readPath + '/中国各省市疫情信息/广东.xlsx'
    a = pd.read_excel(path1, index=False)
    a = a[a['name'].isin(['境外输入'])]
    a['name'] = a['name'].replace('境外输入', '广东')

    path = readPath + '/中国各省市疫情信息'
    Filelist = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            Filelist.append(filename)

    for i in Filelist:
        data1 = pd.read_excel(readPath + '/中国各省市疫情信息/%s' % (i), index=False)
        n = i[:-5]
        data1 = data1[data1['name'].isin(['境外输入'])]
        data1['name'] = data1['name'].replace('境外输入', n)
        a = pd.concat([data1, a], axis=0)

    # 显示所有列
    pd.set_option('display.max_columns', None)

    china_imported = a.drop_duplicates(subset=['name'], keep='first')
    china_imported.index = range(len(china_imported))
    china_imported = china_imported.sort_values(axis=0, ascending=True, by=['confirm'])

    # 将dataframe格式转换成相应的列表格式
    china_imported_name = china_imported['name']
    china_imported_name = list(china_imported_name)

    china_imported_confirm = china_imported['confirm']
    china_imported_confirm = list(china_imported_confirm)

    china_imported_heal = china_imported['heal']
    china_imported_heal = list(china_imported_heal)
    ##############画境外输入xy翻转柱状图###########
    bar = (
        Bar(init_opts=opts.InitOpts(height='1000px'))
            .add_xaxis(china_imported_name)
            .add_yaxis("中国各省境外输入确诊病例", china_imported_confirm)
            .add_yaxis("中国各省境外输入治愈病例", china_imported_heal)
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="中国各省境外输入信息"))
    )
    # bar.render(savaPath+ '\\中国各省境外输入信息.html', index=False)
    page.add(bar)  # 将图像加入同一页
    if flag:
        dwf.write_to_file(savaPath + '/中国各省境外输入信息.txt', str(bar.dump_options_with_quotes()))
    return bar

##############中国各省市历史疫情信息############
def china_provinces_history():

    page1 = Page()

    path2 = savaPath + '/中国各省市历史疫情信息'
    dwf.createFile(path2)

    path = readPath + '/中国各省市历史疫情信息'
    Filelist = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            Filelist.append(filename)

    # print(Filelist)
    def checknan(name):
        if np.any(pd.isnull(name)) == True:
            name.fillna(value="0", inplace=True)

    for i in Filelist:
        data = pd.read_excel(readPath + '/中国各省市历史疫情信息/%s' % (i), index=False)
        n = i[:-5]

        checknan(data['confirm'])
        checknan(data['confirm_add'])
        checknan(data['heal'])
        checknan(data['dead'])

        y1_confirm = data['confirm']
        y1_confirm = list(y1_confirm)
        y1_confirm = [int(i) for i in y1_confirm]

        y2_confirm_add = data['confirm_add']
        y2_confirm_add = list(y2_confirm_add)
        y2_confirm_add = [int(i) for i in y2_confirm_add]

        y3_heal = data['heal']
        y3_heal = list(y3_heal)
        y3_heal = [int(i) for i in y3_heal]

        y4_dead = data['dead']
        y4_dead = list(y4_dead)
        y4_dead = [int(i) for i in y4_dead]

        date_list = []
        for j in data['date']:
            date_list.append(j)

        x = date_list

        linse12 = (
            Line()
                .add_xaxis(xaxis_data=x)
                .add_yaxis(series_name='确诊人数', y_axis=y1_confirm, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                .add_yaxis(series_name='增加确诊人数', y_axis=y2_confirm_add, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                .add_yaxis(series_name='治愈人数', y_axis=y3_heal, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                .add_yaxis(series_name='死亡人数', y_axis=y4_dead, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False),

                           markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                .set_global_opts(title_opts=opts.TitleOpts(title="%s" % (n) + "疫情走势", subtitle="数据来源：腾讯新闻"),
                                 yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=10, interval=3)))
        )

        # lines.render(savaPath + '\\daliy_changes_view\\中国各省市历史疫情信息\\%s.html' % (n), index=False)
        page1.add(linse12)  # 将图像加入同一页
        if flag:
            dwf.write_to_file(savaPath + '/中国各省市历史疫情信息/%s.txt' % (n), str(linse12.dump_options_with_quotes()))
    page.render(savaPath + '/中国各省市历史疫情信息/analyse_all.html')


##############中国各省的城市历史疫情信息#############
def china_citys_history():

    page1 = Page()
    dwf.createFile(savaPath+'/中国各省的城市历史疫情信息')
    path = readPath + '中国各省的城市历史疫情信息'
    floder = glob.glob(os.path.join(path, "*"))


    # 判断数据是否存在
    def checknan(name):
        if np.any(pd.isnull(name)) == True:
            name.fillna(value="0", inplace=True)

    for name in floder:
        for root, dirs, files in os.walk(name, topdown=False):

            for filename in files:
                name = ''.join('%s' % id for id in name)
                # print(type(filename))
                # print(type(name))
                filepath = name + '/' + filename
                filepath = filepath.replace('\\','/')
                data = pd.read_excel(filepath, index=False)
                province_name = re.findall('([\u4e00-\u9fa5]*)\\\\[\u4e00-\u9fa5]*\.xlsx', filepath)
                province_name = ''.join('%s' % id for id in province_name)
                city_name = re.findall('([\u4e00-\u9fa5]*)\.xlsx', filepath)
                city_name = ''.join('%s' % id for id in city_name)
                # print(province_name+'and'+city_name)
                checknan(data['confirm'])
                checknan(data['confirm_add'])
                checknan(data['heal'])
                checknan(data['dead'])

                y1_confirm = data['confirm']
                y1_confirm = list(y1_confirm)
                y1_confirm = [int(i) for i in y1_confirm]

                y2_confirm_add = data['confirm_add']
                y2_confirm_add = list(y2_confirm_add)
                y2_confirm_add = [int(i) for i in y2_confirm_add]

                y3_heal = data['heal']
                y3_heal = list(y3_heal)
                y3_heal = [int(i) for i in y3_heal]

                y4_dead = data['dead']
                y4_dead = list(y4_dead)
                y4_dead = [int(i) for i in y4_dead]

                date_list = []
                for j in data['date']:
                    date_list.append(j)

                x = date_list

                lines = (
                    Line()
                        .add_xaxis(xaxis_data=x)
                        .add_yaxis(series_name='确诊人数', y_axis=y1_confirm, is_symbol_show=True,
                                   label_opts=opts.LabelOpts(is_show=False),
                                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                        .add_yaxis(series_name='增加确诊人数', y_axis=y2_confirm_add, is_symbol_show=True,
                                   label_opts=opts.LabelOpts(is_show=False),
                                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                        .add_yaxis(series_name='治愈人数', y_axis=y3_heal, is_symbol_show=True,
                                   label_opts=opts.LabelOpts(is_show=False),
                                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                        .add_yaxis(series_name='死亡人数', y_axis=y4_dead, is_symbol_show=True,
                                   label_opts=opts.LabelOpts(is_show=False),
                                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                        .set_global_opts(
                        title_opts=opts.TitleOpts(title="%s" % (city_name) + "疫情走势", subtitle="数据来源：腾讯新闻"),
                        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=10, interval=3)))
                )

                name1 = name.replace('data/中国各省的城市历史疫情信息\\', 'data/data_DaliyChangeView/中国各省的城市历史疫情信息/')
                dwf.createFile(name1)

                save_path = name1 + '%s.txt'

                # lines.render(save_path % (city_name), index=False)
                page1.add(lines)  # 将图像加入同一页
                if flag:
                    dwf.write_to_file(save_path % (city_name),
                                      str(lines.dump_options_with_quotes()))
            page.render(savaPath + '/中国各省的城市历史疫情信息/analyse_all.html')



############中国总体疫情数据###############
def china_data_all():


    Chian_day = pd.DataFrame(pd.read_excel(readPath+'/中国总体历史疫情信息/历史每日新增信息.xlsx'))  # 读取信息
    CNday_date = list(Chian_day['date'])
    CNday_confirm = list(Chian_day['confirm'])
    CNday_suspect = list(Chian_day['suspect'])
    CNday_dead = list(Chian_day['dead'])
    CNday_heal = list(Chian_day['heal'])
    CNday_importedCase = list(Chian_day['importedCase'])
    CNday_infect = list(Chian_day['infect'])
    CNday_deadRate = list(Chian_day['deadRate'])
    CNday_healRate = list(Chian_day['healRate'])
    line_CNday = (
        Line()
            .add_xaxis(xaxis_data=CNday_date)  # xaxis_data为x轴，y_axis为y轴
            .add_yaxis(series_name='确诊', y_axis=CNday_confirm, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='疑似', y_axis=CNday_suspect, label_opts=opts.LabelOpts(is_show=False))  # 数据值得不显示
            .add_yaxis(series_name='死亡', y_axis=CNday_dead, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='治愈', y_axis=CNday_heal, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='境外输入', y_axis=CNday_importedCase, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='infect', y_axis=CNday_infect, label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='中国每日新增信息', pos_left='50%', pos_top='10%'),
                             tooltip_opts=opts.TooltipOpts(axis_pointer_type='cross'))
    )  # 创建折线图
    line_CNday_rate = (
        Line()
            .add_xaxis(xaxis_data=CNday_date)
            .add_yaxis(series_name='治愈率', y_axis=CNday_healRate, label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='中国每日治疗率', pos_left='50%', pos_top='10%'),
                             tooltip_opts=opts.TooltipOpts(axis_pointer_type='cross'))
    )  # 创建折线图
    # line_CNday_rate.render(savaPath + '\\中国每日治疗率.html')  # 将生成的图像保存为html文件并存放在photo文件夹
    # line_CNday.render(savaPath + '\\中国每日新增信息.html')  # 将生成的图像保存为html文件并存放在photo文件夹
    if flag:
        dwf.write_to_file(savaPath + '/中国每日治疗率.txt',str(line_CNday_rate.dump_options_with_quotes()))
        dwf.write_to_file(savaPath + '/中国每日新增信息.txt',str(line_CNday.dump_options_with_quotes()))
    page.add(line_CNday_rate)
    page.add(line_CNday)

#############各国历史疫情信息#######
def foregin_history_all():


    path = readPath + '/各国历史疫情信息'

    path2 = savaPath + '/各国历史疫情信息'
    dwf.createFile(path2)

    Filelist = []  # 将当前文件夹内的所有表名存放此列表
    for home, dirs, files in os.walk(path):
        for filename in files:
            Filelist.append(filename)

    for i in Filelist:
        data = pd.read_excel(readPath + '/各国历史疫情信息/%s' % (i), index=False)
        n = i[:-5]  # 只提取国家名，不要后缀（.xlsx）
        y1_confirm = data['confirm']
        y2_confirm_add = data['confirm_add']
        y3_heal = data['heal']
        y4_dead = data['dead']

        date_list = []
        for j in data['date']:
            date_list.append(j)

        x = date_list

        lines = (
            Line()
                .add_xaxis(xaxis_data=x)
                .add_yaxis(series_name='确诊人数', y_axis=y1_confirm, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                .add_yaxis(series_name='增加确诊人数', y_axis=y2_confirm_add, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                .add_yaxis(series_name='治愈人数', y_axis=y3_heal, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                .add_yaxis(series_name='死亡人数', y_axis=y4_dead, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False),
                           markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
                .set_global_opts(title_opts=opts.TitleOpts(title="%s" % (n) + "疫情走势", subtitle="数据来源：腾讯新闻"),
                                 yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=10, interval=3)))
        )
        # lines.render(savaPath + '\\daliy_changes_view\\各国历史疫情信息\\%s.html' % (n), index=False)
        if flag:
            dwf.write_to_file(savaPath + '/各国历史疫情信息/%s.txt' % (n),str(lines.dump_options_with_quotes()))
        page.add(lines)


#############各国各地区疫情信息#############
def foregin_city_all():
    path = readPath + '/各国各地区疫情信息'

    path2 = savaPath + '/各国疫情严重程度排名前十地区信息'
    dwf.createFile(path2)

    Filelist = []  # 将当前文件夹内的所有表名存放此列表
    for home, dirs, files in os.walk(path):
        for filename in files:
            Filelist.append(filename)

    # 判断数据是否存在
    def checknan(name):
        if np.any(pd.isnull(name)) == True:
            name.fillna(value="0", inplace=True)

    # 随机颜色生成用于制作南丁格尔玫瑰图
    def randomcolor(kind):

        colors = []
        for i in range(kind):
            colArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            color = ""
            for i in range(6):
                color += colArr[random.randint(0, 14)]
            colors.append("#" + color)
        return colors

    for i in Filelist:
        page1 = Page()
        data = pd.read_excel(readPath + '/各国各地区疫情信息/%s' % (i), index=False)
        data_sort = data.sort_values(axis=0, ascending=False, by=['confirm'])
        data_message = data_sort.head(10)  # 提取疫情严重程度排名前十地区的信息
        n = i[:-5]  # 只提取国家名，不要后缀（.xlsx）

        checknan(data_message['confirm'])
        checknan(data_message['heal'])
        checknan(data_message['dead'])

        y1_confirm = data_message['confirm']
        y1_confirm = list(y1_confirm)
        y1_confirm = [int(i) for i in y1_confirm]

        y2_dead = data_message['dead']
        y2_dead = list(y2_dead)
        y2_dead = [int(i) for i in y2_dead]

        y3_heal = data_message['heal']
        y3_heal = list(y3_heal)
        y3_heal = [int(i) for i in y3_heal]

        name_list = []
        for j in data_message['name']:
            name_list.append(j)

        x = name_list
        color_series = randomcolor(len(x))
        # Bars = (
        #     Bar(init_opts=opts.InitOpts(width='1080px',height='700px'))
        #         .add_xaxis(xaxis_data=x)
        #         .add_yaxis(series_name='确诊人数', yaxis_data=y1_confirm)
        # )


        #####画南丁格尔玫瑰图##########
        # 画出确诊人数的图
        fig = Pie(init_opts=opts.InitOpts(width='500px', height='700px'))
        fig.add("", [list(z) for z in zip(x, y1_confirm)],
                radius=['30%', '135%'],
                center=['50%', '65%'],
                rosetype='area')
        fig.set_global_opts(title_opts=opts.TitleOpts(title=n + '疫情严重程度排名前十地区的确诊人数'),
                            legend_opts=opts.LegendOpts(is_show=False))
        fig.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12,
                                                      formatter='{b}:{c}例', font_style='italic', font_weight='bold',
                                                      font_family='Microsoft YaHei'))  # b:province;c:num
        fig.set_colors(color_series)
        # 画出死亡人数的图
        fig1 = Pie(init_opts=opts.InitOpts(width='500px', height='700px'))
        fig1.add("", [list(z) for z in zip(x, y2_dead)],
                 radius=['30%', '135%'],
                 center=['50%', '65%'],
                 rosetype='area')
        fig1.set_global_opts(title_opts=opts.TitleOpts(title=n + '疫情严重程度排名前十地区的死亡人数'),
                             legend_opts=opts.LegendOpts(is_show=False))
        fig1.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12,
                                                       formatter='{b}:{c}例', font_style='italic', font_weight='bold',
                                                       font_family='Microsoft YaHei'))  # b:province;c:num
        # 画出治愈人数的图
        fig2 = Pie(init_opts=opts.InitOpts(width='500px', height='700px'))
        fig2.add("", [list(z) for z in zip(x, y3_heal)],
                 radius=['30%', '135%'],
                 center=['50%', '65%'],
                 rosetype='area')
        fig2.set_global_opts(title_opts=opts.TitleOpts(title=n + '疫情严重程度排名前十地区的治愈人数'),
                             legend_opts=opts.LegendOpts(is_show=False))
        fig2.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12,
                                                       formatter='{b}:{c}例', font_style='italic', font_weight='bold',
                                                       font_family='Microsoft YaHei'))  # b:province;c:num
        page1.add(fig)  # 将图像加入同一页
        page1.add(fig1)  # 将图像加入同一页
        page1.add(fig2)  # 将图像加入同一页
        page1.render(savaPath + '/各国疫情严重程度排名前十地区信息/%s.html' % (n), index=False)
        if flag:
            dwf.write_to_file(savaPath + '/各国疫情严重程度排名前十地区信息/（确诊）%s.txt' % (n),str(fig.dump_options_with_quotes()))
            dwf.write_to_file(savaPath + '/各国疫情严重程度排名前十地区信息/（死亡）%s.txt' % (n),str(fig1.dump_options_with_quotes()))
            dwf.write_to_file(savaPath + '/各国疫情严重程度排名前十地区信息/（治愈）%s.txt' % (n),str(fig2.dump_options_with_quotes()))

#################整体疫情信息#################
def world_data_all():
    ###############################################


    world_message = pd.DataFrame(pd.read_excel(readPath+'/世界总体疫情信息/世界总体疫情信息.xlsx'))  # 获取当前工作路径下的data数据
    data_gb = world_message.groupby(by='continent')  ####将世界总体的信息以不同的洲进行分组
    world_gb = data_gb.agg(np.sum)
    world_gb
    continent = ['亚洲', '其他', '北美洲', '南美洲', '大洋洲', '欧洲', '非洲']
    world_continent = continent
    continent_isUpdated = list(world_gb['isUpdated'])
    continent_confirmAdd = list(world_gb['confirmAdd'])
    continent_confirm = list(world_gb['confirm'])
    continent_dead = list(world_gb['dead'])
    continent_heal = list(world_gb['heal'])
    continent_nowConfirm = list(world_gb['nowConfirm'])
    continent_nowConfirmCompare = list(world_gb['nowConfirmCompare'])
    continent_ConfirmCompare = list(world_gb['confirmCompare'])
    continent_healCompare = list(world_gb['healCompare'])
    continent_deadCompare = list(world_gb['deadCompare'])
    Line_World = (
        Line()
            .add_xaxis(xaxis_data=world_continent)
            # .add_yaxis(series_name='新增确诊',yaxis_data=world_confirmAdd)
            .add_yaxis(series_name='确诊', y_axis=continent_confirm, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='死亡', y_axis=continent_dead, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='治愈', y_axis=continent_heal, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='现存确诊', y_axis=continent_nowConfirm, label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='各大洲总信息', pos_left='50%', pos_top='10%'),
                             tooltip_opts=opts.TooltipOpts(axis_pointer_type='cross'))

    )
    Pie_continent_confirm = (
        Pie()
            .add(series_name='死亡', data_pair=[(i, j) for i, j in zip(world_continent, continent_dead)],
                 rosetype='radius')
        # .add(series_name='确诊',data_pair=[(i,j) for i,j in zip(continent_continent,continent_confirm)])

    )
    Pie_continent_heal = (
        Pie()
            .add(series_name='治愈', data_pair=[(i, j) for i, j in zip(world_continent, continent_heal)],
                 rosetype='radius')

    )
    Pie_continent_nowconfirm = (
        Pie()
            .add(series_name='现存确诊', data_pair=[(i, j) for i, j in zip(world_continent, continent_nowConfirm)],
                 rosetype='radius')
    )
    # Pie_continent_confirm.render(savaPath + '\\daliy_changes_view\\各大洲确诊信息.html')
    # Pie_continent_heal.render(savaPath + '\\daliy_changes_view\\各大洲治愈信息.html')
    # Pie_continent_nowconfirm.render(savaPath + '\\daliy_changes_view\\各大洲现存确诊信息.html')
    # Line_World.render(savaPath + '\\daliy_changes_view\\各大洲总信息.html')
    if flag:
        dwf.write_to_file(savaPath + '/各大洲确诊信息.txt',str(Pie_continent_confirm.dump_options_with_quotes()))
        dwf.write_to_file(savaPath + '/各大洲治愈信息.txt',str(Pie_continent_heal.dump_options_with_quotes()))
        dwf.write_to_file(savaPath + '/各大洲现存确诊信息.txt',str(Pie_continent_nowconfirm.dump_options_with_quotes()))
        dwf.write_to_file(savaPath + '/各大洲总信息.txt',str(Line_World.dump_options_with_quotes()))
    page.add(Pie_continent_confirm)
    page.add(Pie_continent_heal)
    page.add(Pie_continent_nowconfirm)
    page.add(Line_World)

############疫情严重程度排名前十国家############
def Top10_confirm_country():


    message = pd.DataFrame(pd.read_excel(readPath+'/世界总体疫情信息/世界总体疫情信息.xlsx'))  # 获取当前工作路径下的data数据
    message_sort = message.sort_values(axis=0, ascending=False, by=['confirm'])
    world_message = message_sort.head(10)
    country_name = list(world_message['name'])
    country_isUpdated = list(world_message['isUpdated'])
    country_confirmAdd = list(world_message['confirmAdd'])
    country_confirm = list(world_message['confirm'])
    country_dead = list(world_message['dead'])
    country_heal = list(world_message['heal'])
    country_nowConfirm = list(world_message['nowConfirm'])
    country_nowConfirmCompare = list(world_message['nowConfirmCompare'])
    country_ConfirmCompare = list(world_message['confirmCompare'])
    country_healCompare = list(world_message['healCompare'])
    country_deadCompare = list(world_message['deadCompare'])

    ##生成国外疫情严重程度排名前十国家疫情相关信息折线图
    Line_World = (
        Line()
            .add_xaxis(xaxis_data=country_name)
            # .add_yaxis(series_name='新增确诊',yaxis_data=world_confirmAdd)
            .add_yaxis(series_name='确诊', y_axis=country_confirm, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='死亡', y_axis=country_dead, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='治愈', y_axis=country_heal, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='现存确诊', y_axis=country_nowConfirm, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='新增', y_axis=country_confirmAdd, label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='疫情严重程度排名前十国家', pos_left='50%', pos_top='10%'),
                             tooltip_opts=opts.TooltipOpts(axis_pointer_type='cross'))

    )

    ##生成国外疫情严重程度排名前十国家疫情相关信息柱形图
    Bar_World = (
        Bar()
            .add_xaxis(xaxis_data=country_name)
            # .add_yaxis(series_name='新增确诊',yaxis_data=world_confirmAdd)
            .add_yaxis(series_name='确诊', yaxis_data=country_confirm, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='死亡', yaxis_data=country_dead, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='治愈', yaxis_data=country_heal, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='现存确诊', yaxis_data=country_nowConfirm, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='新增', yaxis_data=country_confirmAdd, label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='国外疫情严重程度排名前十国家', pos_left='50%', pos_top='10%'),
                             tooltip_opts=opts.TooltipOpts(axis_pointer_type='cross'))

    )
    # Line_World.render(savaPath + '\\疫情严重程度排名前十国家（折线图）.html')
    # Bar_World.render(savaPath + '\\疫情严重程度排名前十国家（柱状图）.html')
    if flag:
        dwf.write_to_file(savaPath + '/疫情严重程度排名前十国家（折线图）.txt', str(Line_World.dump_options_with_quotes()))
        dwf.write_to_file(savaPath + '/疫情严重程度排名前十国家（柱状图）.txt', str(Bar_World.dump_options_with_quotes()))


def main():
    dwf.createFile(readPath)  # 创建不存在的文件夹data
    dwf.createFile(savaPath)  # 创建不存在的文件夹../data/data_Map_analyse1

    china_history_all()
    china_provinces_imports()
    china_provinces_history()
    china_citys_history()
    china_data_all()
    foregin_history_all()
    foregin_city_all()
    world_data_all()
    Top10_confirm_country()
    return page.render(savaPath + '/analyse_all1.html')  # 生成包含所有图像的网页并存放在analyse_all.html

if __name__=='__main__':
    main()