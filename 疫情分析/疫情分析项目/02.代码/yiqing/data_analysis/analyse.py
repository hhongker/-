import pandas as pd
from pyecharts.charts import Line#折线图绘制所需要的库
from pyecharts.charts import Bar#柱形图库
from pyecharts.charts import Pie#饼图
from pyecharts.charts import Page#将所有图像放在同一页所需要的库
import pyecharts.options as opts#设置全局变量
from util import dealWithFile as dwf
###############################################################################
#此文件代码需要用到任务3代码生成的data下的xlsx文件数据，请放在与data同目录
"""
针对部分任务3的代码爬取并保存为.xlsx的信息进行数据可视化，使用了pyecharts的scatter
散点图库，对生成的图像进行了分析，并新建了文件夹analysis用于存放所生成的
所有图像文件。
"""
###############################################################################

readPath = dwf.rootPath #读取数据的地方
savaPath = dwf.savaPathAnalyse #生成结果的地方
flag = dwf.flag #是否将图数据持久化

page=Page()#创建一个分页用于放所有的图像在这一分页上

def analyse_Chinaeveryday():
    Chian_day=pd.DataFrame(pd.read_excel(readPath+'/中国总体历史疫情信息/历史每日新增信息.xlsx'))#读取信息
    CNday_date=list(Chian_day['date'])
    CNday_confirm=list(Chian_day['confirm'])
    CNday_suspect=list(Chian_day['suspect'])
    CNday_dead=list(Chian_day['dead'])
    CNday_heal=list(Chian_day['heal'])
    CNday_importedCase=list(Chian_day['importedCase'])
    CNday_infect=list(Chian_day['infect'])
    CNday_deadRate=list(Chian_day['deadRate'])
    CNday_healRate=list(Chian_day['healRate'])
    line_CNday=\
    (
        Line()
        .add_xaxis(xaxis_data=CNday_date)#xaxis_data为x轴，y_axis为y轴
        .add_yaxis(series_name='确诊病例',y_axis=CNday_confirm,label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis(series_name='疑似病例',y_axis=CNday_suspect,label_opts=opts.LabelOpts(is_show=False))#数据值得不显示
        .add_yaxis(series_name= '死亡病例',y_axis=CNday_dead,label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis(series_name='治愈病例',y_axis=CNday_heal,label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis(series_name='境外输入病例',y_axis=CNday_importedCase,label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis(series_name='Infect',y_axis=CNday_infect,label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title='中国每日新增信息'),
                         tooltip_opts=opts.TooltipOpts(axis_pointer_type= 'cross'),
                         xaxis_opts=opts.AxisOpts(name='日期'),
                         yaxis_opts=opts.AxisOpts(name='人数'))

    )#创建折线图
    line_CNday_rate=\
    (
            Line()
            .add_xaxis(xaxis_data=CNday_date)
            .add_yaxis(series_name='死亡率',y_axis=CNday_deadRate,label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='治愈率',y_axis=CNday_healRate,label_opts=opts.LabelOpts(is_show=False))
             .set_global_opts(title_opts=opts.TitleOpts(title='中国每日治疗率、死亡率'),
                              tooltip_opts=opts.TooltipOpts(axis_pointer_type= 'cross'),
                              xaxis_opts=opts.AxisOpts(name='日期'),
                              yaxis_opts=opts.AxisOpts(name='百分比'))
    )#创建折线图
    # line_CNday_rate.render(savaPath+'\\CNdayrate.html')#将生成的图像保存为html文件并存放在analisis文件夹
    # line_CNday.render(savaPath+'\\Chinaeveryday.html')#将生成的图像保存为html文件并存放在analisis文件夹

    page.add(line_CNday)#将图像加入同一页
    page.add(line_CNday_rate)#将图像加入同一页
    if flag:
        dwf.write_to_file(savaPath+'/中国每日新增信息.txt',str(line_CNday.dump_options_with_quotes()))
        dwf.write_to_file(savaPath+'/中国每日治疗率、死亡率.txt',str(line_CNday_rate.dump_options_with_quotes()))
    return line_CNday,line_CNday_rate
    """
    从中国的历史每日新增数据pyecharts散点图中，在2月12日，中国新增确诊人数(confirm)高达一万五千以上，之所以有这么大的差距，是因为确诊的标准发生了变化，
    由之前的核酸检测，到核磁CT。通过相关部门人员的调查，可以发现新病例全部包括临床诊断病例（临床诊断病例用于治疗大多数临床症状主要表现为发热、乏力、干咳、
    鼻塞、流鼻涕等外感症状，其CT结果显示为肺炎反应，但其核酸检测未被确认为临床确诊病例的疑似患者）。很明显，这是高峰到来的样子这表明冠状病毒隐形载体传播者的大部分问题已经被逐一发现。
    也就是说，这种流行病的预防和控制起到了一定的作用，这种流行病的预防和控制在抗疫战争中取得了显著的成绩。随着高峰期的突出和这一流行病接近尾声，相信恢复正常的社会生活已不远了。
    """

def analyse_province():
    Province=pd.DataFrame(pd.read_excel(readPath+'/中国各省市总体疫情信息/中国各省市总体疫情信息.xlsx'))
    prov_nowConfirm=list(Province['nowConfirm'])
    prov_confirm=list(Province['confirm'])
    prov_suspect=list(Province['suspect'])
    prov_dead=list(Province['dead'])
    prov_deadRate=list(Province['deadRate'])
    prov_showRate=list(Province['showRate'])
    prov_heal=list(Province['heal'])
    prov_healRate=list(Province['healRate'])
    prov_showHeal=list(Province['showHeal'])
    prov_importedCase=list(Province['importedCase'])
    prov_name=list(Province['name'])
    line_prov=\
    (
        Line()
        .add_xaxis(xaxis_data=prov_name)#xaxis_data为x轴，y_axis为y轴
        .add_yaxis(series_name='现有确诊',y_axis=prov_nowConfirm,label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis(series_name='累计确诊',y_axis=prov_confirm,label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis(series_name='疑似病例',y_axis=prov_suspect,label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis(series_name='死亡病例',y_axis=prov_dead,label_opts=opts.LabelOpts(is_show=False))#数据值得不显示
        .add_yaxis(series_name='治愈病例',y_axis=prov_heal,label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis(series_name='showHeal',y_axis=prov_showHeal,label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis(series_name='境外输入病例',y_axis=prov_importedCase,label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title='中国各省市总体疫情信息',pos_left='37%',pos_top='5%'),
                         tooltip_opts=opts.TooltipOpts(axis_pointer_type= 'cross'),
                         xaxis_opts=opts.AxisOpts(name='日期'),
                         yaxis_opts=opts.AxisOpts(name='人数'))

    )#创建折线图
    line_prov_rate=\
    (
            Line()
            .add_xaxis(xaxis_data=prov_name)
            .add_yaxis(series_name='治愈率',y_axis=prov_healRate,label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name= '死亡率',y_axis=prov_deadRate,label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='中国各省市(区)治疗率、死亡率'),
                             tooltip_opts=opts.TooltipOpts(axis_pointer_type= 'cross'),
                             xaxis_opts=opts.AxisOpts(name='日期'),
                             yaxis_opts=opts.AxisOpts(name='百分比'))
            )
    # line_prov_rate.render(savaPath+'\\prov_rate.html')#将生成的图像保存为html文件并存放在analisis文件夹
    # line_prov.render(savaPath+'\\province.html')#将生成的图像保存为html文件并存放在analisis文件夹
    page.add(line_prov)#将图像加入同一页
    page.add(line_prov_rate)#将图像加入同一页
    """利用pyecharts散点图对中国的历史数据做可视化，可以看出新增确诊人数(newConfirm)，累计确诊人数(confirm)，疑似(suspect)人数达到峰值的日期都接近于2月17日前后，
    随后都逐渐下降，，而累计确诊人数也在随后趋于平缓，治愈人数也在不断趋近去确诊人数，明显可以看出中国疫情防控取得了有效的成果。
    """
    if flag:
        dwf.write_to_file(savaPath + '/中国各省市总体疫情信息.txt', str(line_prov.dump_options_with_quotes()))
        dwf.write_to_file(savaPath + '/中国各省市(区)治疗率、死亡率.txt', str(line_prov_rate.dump_options_with_quotes()))
    return line_prov,line_prov_rate

def analyse_worldhistory():
    world=pd.DataFrame(pd.read_excel(readPath+'/世界总体疫情信息/世界总体疫情信息.xlsx'))
    confirmAdd=int(world['confirmAdd'].sum())
    confirm=int(world['confirm'].sum())
    confirmAddCut=int(world['confirmAddCut'].sum())
    suspect=int(world['suspect'].sum())
    dead=int(world['dead'].sum())
    heal=int(world['heal'].sum())
    nowConfirm=int(world['nowConfirm'].sum())
    confirmCompare=int(world['confirmCompare'].sum())
    nowConfirmCompare=int(world['nowConfirmCompare'].sum())
    healCompare=int(world['healCompare'].sum())
    deadCompare=int(world['deadCompare'].sum())
    healRate=round(heal/confirm*100,2)
    deadRate=round(dead/confirm*100,2)
    aliveRate=round(100-healRate-deadRate,2)
    ratedata=[deadRate,healRate,aliveRate]
    ratecolumns=['死亡率/% ','治愈率/% ','存活率/% ']

    bar_world=\
    (
        Bar()
        .add_xaxis(" ")
        .add_yaxis('新增确诊',[confirmAdd],color='pink',label_opts=opts.LabelOpts(is_show=True))
        .add_yaxis('累计确诊',[confirm],color='green',label_opts=opts.LabelOpts(is_show=True))
        .add_yaxis('疑似病例',[suspect],color='black',label_opts=opts.LabelOpts(is_show=True))
        .add_yaxis('死亡病例',[dead],color='orange',label_opts=opts.LabelOpts(is_show=True))
        .add_yaxis('治愈病例',[heal],color='red',label_opts=opts.LabelOpts(is_show=True))
        .add_yaxis('现有确诊',[nowConfirm],color='grey',label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(title_opts=opts.TitleOpts(title='世界疫情信息'),
                         tooltip_opts=opts.TooltipOpts(is_show=False),
                         xaxis_opts=opts.AxisOpts(name='日期',axislabel_opts={"interval":"0"}),
                         yaxis_opts=opts.AxisOpts(name='人数',splitline_opts=opts.SplitLineOpts(is_show=True),)
                        )
    )#柱形图
    bar_worldother=\
    (
        Bar()
        .add_xaxis(" ")
        .add_yaxis('confirmAddCut',[confirmAddCut],color='pink',label_opts=opts.LabelOpts(is_show=True))
        .add_yaxis('confirmCompare',[confirmCompare],color='green',label_opts=opts.LabelOpts(is_show=True))
        .add_yaxis('nowConfirmCompare',[nowConfirmCompare],color='orange',label_opts=opts.LabelOpts(is_show=True))
        .add_yaxis('healCompare',[healCompare],color='black',label_opts=opts.LabelOpts(is_show=True))
        .add_yaxis('deadCompare',[deadCompare],color='red',label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(title_opts=opts.TitleOpts(title='世界疫情其他信息',pos_left='37%',pos_top='5%'),
                         tooltip_opts=opts.TooltipOpts(is_show=False),
                         xaxis_opts=opts.AxisOpts(name='日期',axislabel_opts={"interval":"0"}),
                         yaxis_opts=opts.AxisOpts(name='人数',splitline_opts=opts.SplitLineOpts(is_show=True),)
                        )
    )  #柱形图
    pie_worldrate=\
    (
     Pie()
     .add("", [list(z) for z in zip(ratecolumns,ratedata)],
            radius=["20%", "60%"],
            center=["55%", "50%"],
            rosetype="area"
            )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12,formatter="{b}:{c}", font_style="italic",font_weight="bold", font_family="Microsoft YaHei"),)
    .set_global_opts(title_opts=opts.TitleOpts(title='世界总的死亡率、治疗率、存活率'),
                     tooltip_opts=opts.TooltipOpts(axis_pointer_type= 'cross'),
                     xaxis_opts=opts.AxisOpts(name='日期'),
                     yaxis_opts=opts.AxisOpts(name='百分比'))
    )#饼图
    page.add(bar_world)#添加到同一页面
    page.add(bar_worldother)#添加到同一页面
    page.add(pie_worldrate)#添加到同一页面
    # bar_world.render(savaPath+'\\world.html')#在analysis生成html文件
    # bar_worldother.render(savaPath+'\\worldother.html')#在analysis生成html文件
    # pie_worldrate.render(savaPath+'\\worldrate.html')#在analysis生成html文件
    """
    从图可以看出，国外疫情形势格外严峻，确诊人数高达150多万，死亡人数更是接近16万，存活率为67.86%。
    其中发达国家的新冠确诊患者的人数相较于其他国家和地区会高出很多，伴随着国外疫情形势的加剧，
    国内境外输入确诊的人数也在不断增加，在确保在外公民的安全和国内疫情能够持续稳定的前提下，需要加强对出入境人员的防控。
    """
    if flag:
        dwf.write_to_file(savaPath + '/世界疫情信息.txt', str(bar_world.dump_options_with_quotes()))
        dwf.write_to_file(savaPath + '/世界疫情其他信息.txt', str(bar_worldother.dump_options_with_quotes()))
        dwf.write_to_file(savaPath + '/世界总的死亡率、治疗率、存活率.txt', str(pie_worldrate.dump_options_with_quotes()))
    return bar_world,bar_worldother,pie_worldrate

def analyse_Chinahistory():
    China_history=pd.DataFrame(pd.read_excel(readPath+'/中国总体历史疫情信息/历史总体信息.xlsx'))
    CNhis_date=list(China_history['date'])
    CNhis_confirm=list(China_history['confirm'])
    CNhis_suspect=list(China_history['suspect'])
    CNhis_dead=list(China_history['dead'])
    CNhis_heal=list(China_history['heal'])
    CNhis_nowConfirm=list(China_history['nowConfirm'])
    CNhis_nowSevere=list(China_history['nowSevere'])
    CNhis_importedCase=list(China_history['importedCase'])
    CNhis_deadRate=list(China_history['deadRate'])
    CNhis_healRate=list(China_history['healRate'])
    CNhis_noInfect=list(China_history['noInfect'])
    line_CNhis=\
    (
            Line()
            .add_xaxis(xaxis_data=CNhis_date)#xaxis_data为x轴，y_axis为y轴
            .add_yaxis(series_name='累计确诊',y_axis=CNhis_confirm,label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='疑似病例',y_axis=CNhis_suspect,label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='死亡病例',y_axis=CNhis_dead,label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='治愈病例',y_axis=CNhis_heal,label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='现有确诊',y_axis=CNhis_nowConfirm,label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='现有重症',y_axis=CNhis_nowSevere,label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='境外输入病例',y_axis=CNhis_importedCase,label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='无诊感染者人数',y_axis=CNhis_noInfect,label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='中国疫情走势',pos_left='37%',pos_top='5%'),
                             tooltip_opts=opts.TooltipOpts(axis_pointer_type= 'cross'),
                             xaxis_opts=opts.AxisOpts(name='日期'),
                             yaxis_opts=opts.AxisOpts(name='人数'))

    )#创建折线图
    line_CNhis_rate=\
    (
            Line()
            .add_xaxis(xaxis_data=CNhis_date)#xaxis_data为x轴，y_axis为y轴
            .add_yaxis(series_name='治愈率',y_axis=CNhis_healRate,label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='死亡率',y_axis=CNhis_deadRate,label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='中国累计治疗率、死亡率',pos_left='37%',pos_top='5%'),
                             tooltip_opts=opts.TooltipOpts(axis_pointer_type= 'cross'),
                             xaxis_opts=opts.AxisOpts(name='日期'),
                             yaxis_opts=opts.AxisOpts(name='百分比'))
            )#创建折线图
    # line_CNhis.render(savaPath+'\\Chinahistory.html')#将生成的图像保存为html文件并存放在analisis文件夹
    # line_CNhis_rate.render(savaPath+'\\Chinahistoryrate.html')#将生成的图像保存为html文件并存放在analisis文件夹
    page.add(line_CNhis)#将图像加入同一页
    page.add(line_CNhis_rate)#将图像加入同一页
    """
    很明显，湖北地区的死亡人数，确诊人数相比其他地区要高的多。湖北地区最早爆发疫情，因此很多人也相信新冠肺炎的发源地是来自于武汉的华南海鲜市场，
    而这些病毒是从野生动物身上传到人体身上的。随着事态发展，一些关键的研究出来了，权威的科学杂志Science上发表了一篇文章，
    最早的一批患者有一部分人没有华南海鲜市场接触史。因此他们推断华南海鲜市场可能并不是新冠肺炎的起源地。故疫情当前，我们应该做的不是互相推卸责任，
    而是共同抵抗病毒的入侵，对于了解病毒的真实来源，更应该看数据说话，不应该听信谣言，更不应该散播谣言。
    """
    if flag:
        dwf.write_to_file(savaPath + '/中国疫情走势.txt', str(line_CNhis.dump_options_with_quotes()))
        dwf.write_to_file(savaPath + '/中国累计治疗率、死亡率.txt', str(line_CNhis_rate.dump_options_with_quotes()))
    return line_CNhis,line_CNhis_rate



def main():
    dwf.createFile(readPath)
    dwf.createFile(savaPath)
    analyse_Chinaeveryday()#生成中国每日新增信息的折线图
    analyse_province()#生成中国各省份信息折线图
    analyse_worldhistory()#生成世界总体信息折线图
    analyse_Chinahistory()#生成中国总体信息折线图
    page.render(savaPath+'/analyse_all.html')#生成包含所有图像的html并存放在analysis文件夹
    
if __name__=='__main__':
    main()