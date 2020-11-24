from data_get import getData
from xlwt import *
from util import dealWithFile as cf
from util import dealWithFile as dwf

all_data = getData.getProvinceTotalData()
rootPath = dwf.rootPath

# 中国各省市疫情信息
def province_total_data():
    areaTree = all_data
    print(areaTree)
    print(areaTree[0]['total'])
    print(areaTree[0]['total'].keys())
    province_name = list()
    province_total_nowConfirm = list()
    province_total_confirm = list()
    province_total_suspect = list()
    province_total_dead = list()
    province_total_deadRate = list()
    province_total_showRate = list()
    province_total_heal = list()
    province_total_healRate = list()
    province_total_showHeal = list()
    province_total_importedCase = list()
    for province in areaTree:
        province_name.append(province['name'])
        province_total_nowConfirm.append(int(province['total']['nowConfirm']))
        province_total_confirm.append(int(province['total']['confirm'])) # 累计确诊
        province_total_suspect.append(int(province['total']['suspect'])) # 疑似
        province_total_dead.append(int(province['total']['dead'])) # 累计死亡
        province_total_deadRate.append(province['total']['deadRate'])
        province_total_showRate.append(province['total']['showRate'])
        province_total_heal.append(int(province['total']['heal'])) # 累计治愈
        province_total_healRate.append(province['total']['healRate'])
        province_total_showHeal.append(province['total']['healRate'])
        if 'importedCase'in province['total']:
            province_total_importedCase.append(int(province['total']['importedCase'])) # 境外输入
        else:
            province_total_importedCase.append(0)
    # 指定file以utf-8的格式打开
    file = Workbook(encoding='utf-8')
    # 指定打开的文件名
    table = file.add_sheet('data')
    t1_name = ['name', 'nowConfirm', 'confirm', 'suspect', 'dead', 'deadRate', 'showRate', 'heal', 'healRate', 'showHeal', 'importedCase']
    for i in range(len(t1_name)):
        table.write(0, i, t1_name[i])
    for i in range(len(province_name)):
        table.write(i + 1, 0, province_name[i])
        table.write(i + 1, 1, province_total_nowConfirm[i])
        table.write(i + 1, 2, province_total_confirm[i])
        table.write(i + 1, 3, province_total_suspect[i])
        table.write(i + 1, 4, province_total_dead[i])
        table.write(i + 1, 5, province_total_deadRate[i])
        table.write(i + 1, 6, province_total_showRate[i])
        table.write(i + 1, 7, province_total_heal[i])
        table.write(i + 1, 8, province_total_healRate[i])
        table.write(i + 1, 9, province_total_showHeal[i])
        table.write(i + 1, 10, province_total_importedCase[i])
    cf.createFile(rootPath+'/中国各省市总体疫情信息')
    file.save(rootPath+'/中国各省市总体疫情信息/中国各省市总体疫情信息.xlsx')

    # # 将省份名称和确诊人数对应打包为字典，用于ECharts地图可视化
    # province_total_confirm_dict = {'name': province_name, 'value': province_total_confirm}
    # with open('province_total.json', 'w', encoding='utf-8') as f:
    #     json.dump(province_total_confirm_dict, f, ensure_ascii=False)

    # return province_name, province_total_confirm, province_total_suspect, province_total_dead, province_total_heal, \
    #        province_total_importedCase

# 获取各省今日数据
def province_today_data():
    areaTree = all_data
    province_name = list()
    province_today_confirm = list()
    province_today_confirmCuts = list()
    province_today_dead = list()
    province_today_heal = list()
    province_today_importedCase = list()
    for province in areaTree:
        province_name.append(province['name'])
        province_today_confirm.append(int(province['today']['confirm']))
        province_today_confirmCuts.append(int(province['today']['confirmCuts']))
        if 'dead' in province['today']:
            province_today_dead.append(int(province['today']['dead']))
        else:
            province_today_dead.append(0)
        if 'heal' in province['today']:
            province_today_heal.append(int(province['today']['heal']))
        else:
            province_today_heal.append(0)
        if 'importedCase'in province['total']:
            province_today_importedCase.append(int(province['total']['importedCase'])) # 境外输入
        else:
            province_today_importedCase.append(0)
    # 指定file以utf-8的格式打开
    file = Workbook(encoding='utf-8')
    # 指定打开的文件名
    table = file.add_sheet('data')
    t2_name = ['name', 'confirm', 'confirmCuts', 'dead', 'heal', 'importedCase']
    for i in range(len(t2_name)):
        table.write(0, i, t2_name[i])
    for i in range(len(province_name)):
        table.write(i + 1, 0, province_name[i])
        table.write(i + 1, 1, province_today_confirm[i])
        table.write(i + 1, 2, province_today_confirmCuts[i])
        table.write(i + 1, 3, province_today_dead[i])
        table.write(i + 1, 4, province_today_heal[i])
        table.write(i + 1, 5, province_today_importedCase[i])
    cf.createFile(rootPath+'/中国各省市总体疫情信息')
    file.save(rootPath+'/中国各省市总体疫情信息/中国各省市(区)今日新增疫情信息.xlsx')
    # return province_name, province_today_confirm, province_today_importedCase, province_today_dead, \
    #        province_today_heal

# 每个省份的地区疫情数据
def province_children_data():
    areaTree = all_data
    for province in areaTree:
        children_name = list()
        children_total_nowConfirm = list()
        children_total_confirm = list()
        children_total_suspect = list()
        children_total_dead = list()
        children_total_deadRate = list()
        children_total_showRate = list()
        children_total_heal = list()
        children_total_healRate = list()
        children_total_showHeal = list()
        children_total_importedCase = list()
        for children in province['children']:
            children_name.append(children['name'])
            children_total_nowConfirm.append(int(children['total']['nowConfirm']))
            children_total_confirm.append(int(children['total']['confirm']))  # 累计确诊
            children_total_suspect.append(int(children['total']['suspect']))  # 疑似
            children_total_dead.append(int(children['total']['dead']))  # 累计死亡
            children_total_deadRate.append(children['total']['deadRate'])
            children_total_showRate.append(children['total']['showRate'])
            children_total_heal.append(int(children['total']['heal']))  # 累计治愈
            children_total_healRate.append(children['total']['healRate'])
            children_total_showHeal.append(children['total']['healRate'])
            if 'importedCase' in children['total']:
                children_total_importedCase.append(int(children['total']['importedCase']))  # 境外输入
            else:
                children_total_importedCase.append(0)
        # 指定file以utf-8的格式打开
        file = Workbook(encoding='utf-8')
        # 指定打开的文件名
        table = file.add_sheet('data')
        t3_name = ['name', 'nowConfirm', 'confirm', 'suspect', 'dead', 'deadRate', 'showRate', 'heal', 'healRate',
                   'showHeal', 'importedCase']
        for i in range(len(t3_name)):
            table.write(0, i, t3_name[i])
        for i in range(len(children_name)):
            table.write(i + 1, 0, children_name[i])
            table.write(i + 1, 1, children_total_nowConfirm[i])
            table.write(i + 1, 2, children_total_confirm[i])
            table.write(i + 1, 3, children_total_suspect[i])
            table.write(i + 1, 4, children_total_dead[i])
            table.write(i + 1, 5, children_total_deadRate[i])
            table.write(i + 1, 6, children_total_showRate[i])
            table.write(i + 1, 7, children_total_heal[i])
            table.write(i + 1, 8, children_total_healRate[i])
            table.write(i + 1, 9, children_total_showHeal[i])
            table.write(i + 1, 10, children_total_importedCase[i])
        cf.createFile(rootPath+'/中国各省市疫情信息')
        file.save(rootPath+'/中国各省市疫情信息/' + province['name'] + '.xlsx')


def main():
    province_total_data()
    province_today_data()
    province_children_data()

if __name__ == '__main__':
    main()
