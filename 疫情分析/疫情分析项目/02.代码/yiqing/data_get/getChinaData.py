from data_get import getData
from xlwt import *

from util import dealWithFile as cf
from util import dealWithFile as dwf

all_data = getData.getChinaTotalData()
abs_data = getData.getChinaAbsData()
rootPath = dwf.rootPath

# 获取从1月13日起的一系列累计数据
def china_total_data():
    chinaDayList = all_data["chinaDayList"]
    date_list1 = list()
    total_confirm = list()
    total_suspect = list()
    total_dead = list()
    total_heal = list()
    total_nowConfirm = list()
    total_nowSevere = list()
    total_importedCase = list()
    total_deadRate = list()
    total_healRate = list()
    total_noInfect = list()
    for total in chinaDayList:
        date_list1.append(total['date'][:2] + "/" + total['date'][3:])
        total_confirm.append(int(total['confirm'])) # 累计确诊
        total_suspect.append(int(total['suspect'])) # 疑似
        total_dead.append(int(total['dead'])) # 累计死亡
        total_heal.append(int(total['heal'])) # 累计治愈
        total_nowConfirm.append(int(total['nowConfirm']))
        total_nowSevere.append(int(total['nowSevere']))
        total_importedCase.append(int(total['importedCase'])) # 境外输入
        total_deadRate.append(float(total['deadRate']))
        total_healRate.append(float(total['healRate']))
        total_noInfect.append(int(total['noInfect']))
    # 指定file以utf-8的格式打开
    file = Workbook(encoding='utf-8')
    # 指定打开的文件名
    table = file.add_sheet('data')
    t1_name = ['date', 'confirm', 'suspect', 'dead', 'heal', 'nowConfirm', 'nowSevere',
               'importedCase', 'deadRate', 'healRate', 'noInfect']
    for i in range(len(t1_name)):
        table.write(0,i,t1_name[i])
    for i in range(len(date_list1)):
        table.write(i+1, 0, date_list1[i])
        table.write(i+1, 1, total_confirm[i])
        table.write(i+1, 2, total_suspect[i])
        table.write(i+1, 3, total_dead[i])
        table.write(i+1, 4, total_heal[i])
        table.write(i+1, 5, total_nowConfirm[i])
        table.write(i+1, 6, total_nowSevere[i])
        table.write(i+1, 7, total_importedCase[i])
        table.write(i+1, 8, total_deadRate[i])
        table.write(i+1, 9, total_healRate[i])
        table.write(i+1, 10, total_noInfect[i])
        cf.createFile(rootPath+'/中国总体历史疫情信息')
    file.save(rootPath+'中国总体历史疫情信息/历史总体信息.xlsx')

    # return date_list1, total_confirm, total_suspect, total_dead, total_heal, total_nowConfirm,\
    #        total_nowSevere, total_importedCase, total_deadRate, total_healRate, total_noInfect

# 获取从1月20日起的一系列每日数据
def china_everyday_data():
    chinaDayAddList = all_data["chinaDayAddList"]
    date_list2 = list()
    everyday_confirm = list()
    everyday_suspect = list()
    everyday_dead = list()
    everyday_heal = list()
    everyday_importedCase = list()
    everyday_infect = list()
    everyday_deadRate = list()
    everyday_healRate = list()
    for everyday in chinaDayAddList:
        date_list2.append(everyday['date'][:2] + "/" + everyday['date'][3:])
        everyday_confirm.append(int(everyday['confirm']))  # 累计确诊
        everyday_suspect.append(int(everyday['suspect']))  # 疑似
        everyday_dead.append(int(everyday['dead']))  # 累计死亡
        everyday_heal.append(int(everyday['heal']))  # 累计治愈
        everyday_importedCase.append(int(everyday['importedCase']))  # 境外输入
        everyday_infect.append(int(everyday['infect']))
        everyday_deadRate.append(float(everyday['deadRate']))
        everyday_healRate.append(float(everyday['healRate']))
    # 指定file以utf-8的格式打开
    file = Workbook(encoding='utf-8')
    # 指定打开的文件名
    table = file.add_sheet('data')
    t2_name = ['date',  'confirm',  'suspect',  'dead',  'heal',  'importedCase',
               'infect',  'deadRate',  'healRate']
    for i in range(len(t2_name)):
        table.write(0,i,t2_name[i])
    for i in range(len(date_list2)):
        table.write(i + 1, 0, date_list2[i])
        table.write(i + 1, 1, everyday_confirm[i])
        table.write(i + 1, 2, everyday_suspect[i])
        table.write(i + 1, 3, everyday_dead[i])
        table.write(i + 1, 4, everyday_heal[i])
        table.write(i + 1, 5, everyday_importedCase[i])
        table.write(i + 1, 6, everyday_infect[i])
        table.write(i + 1, 7, everyday_deadRate[i])
        table.write(i + 1, 8, everyday_healRate[i])
    cf.createFile(rootPath+'/中国总体历史疫情信息')
    file.save(rootPath+'/中国总体历史疫情信息/历史每日新增信息.xlsx')
    # return date_list2, everyday_confirm, everyday_suspect, everyday_dead, everyday_heal, \
    #        everyday_importedCase, everyday_infect, everyday_deadRate, everyday_healRate

def china_abstract_data():
    chinaAbsInfo = abs_data
    absInfo = list()
    absInfo.append(('治愈', int(chinaAbsInfo['heal'])))
    absInfo.append(('死亡', int(chinaAbsInfo['dead'])))
    absInfo.append(('现存确诊', int(chinaAbsInfo['nowConfirm'])))
    return absInfo

def main():
    china_total_data()
    china_everyday_data()
    # china_abstract_data()


if __name__ == '__main__':
    main()