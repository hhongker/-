from data_get import getData
from xlwt import *

from util import dealWithFile as cf
from util import dealWithFile as dwf

all_data = getData.getForeignTotalData()
rootPath = dwf.rootPath

# 世界总体历史疫情信息
def foreign_total_data():
    foreign_data = all_data
    foreign_name = list()
    foreign_total_continent = list()
    foreign_total_isUpdated = list()
    foreign_total_confirmAdd = list()
    foreign_total_confirmAddCut = list()
    foreign_total_confirm = list()
    foreign_total_suspect = list()
    foreign_total_dead = list()
    foreign_total_heal = list()
    foreign_total_nowConfirm = list()
    foreign_total_confirmCompare = list()
    foreign_total_nowConfirmCompare = list()
    foreign_total_healCompare = list()
    foreign_total_deadCompare = list()
    # foreign_total_children = list()
    for country in foreign_data:
        foreign_name.append(country['name']) # 国家名字
        foreign_total_continent.append(country['continent'])
        foreign_total_isUpdated.append(country['isUpdated'])
        foreign_total_confirmAdd.append(int(country['confirmAdd']))
        foreign_total_confirmAddCut.append(int(country['confirmAddCut']))
        foreign_total_confirm.append(int(country['confirm']))
        foreign_total_suspect.append(int(country['suspect']))
        foreign_total_dead.append(int(country['dead']))
        foreign_total_heal.append(int(country['heal']))
        foreign_total_nowConfirm.append(int(country['nowConfirm']))
        foreign_total_confirmCompare.append(int(country['confirmCompare']))
        foreign_total_nowConfirmCompare.append(int(country['nowConfirmCompare']))
        foreign_total_healCompare.append(int(country['healCompare']))
        foreign_total_deadCompare.append(int(country['deadCompare']))
        # foreign_total_children.append(country['children'])
    # 指定file以utf-8的格式打开
    file = Workbook(encoding='utf-8')
    # 指定打开的文件名
    table = file.add_sheet('data')
    t1_name = ['name', 'continent', 'isUpdated','confirmAdd', 'confirmAddCut', 'confirm','suspect', 'dead',
               'heal', 'nowConfirm', 'confirmCompare', 'nowConfirmCompare', 'healCompare', 'deadCompare']
    for i in range(len(t1_name)):
        table.write(0, i, t1_name[i])
    for i in range(len(foreign_name)):
        table.write(i + 1, 0, foreign_name[i])
        table.write(i + 1, 1, foreign_total_continent[i])
        table.write(i + 1, 2, foreign_total_isUpdated[i])
        table.write(i + 1, 3, foreign_total_confirmAdd[i])
        table.write(i + 1, 4, foreign_total_confirmAddCut[i])
        table.write(i + 1, 5, foreign_total_confirm[i])
        table.write(i + 1, 6, foreign_total_suspect[i])
        table.write(i + 1, 7, foreign_total_dead[i])
        table.write(i + 1, 8, foreign_total_heal[i])
        table.write(i + 1, 9, foreign_total_nowConfirm[i])
        table.write(i + 1, 10, foreign_total_confirmCompare[i])
        table.write(i + 1, 11, foreign_total_nowConfirmCompare[i])
        table.write(i + 1, 12, foreign_total_healCompare[i])
        table.write(i + 1, 13, foreign_total_deadCompare[i])
    cf.createFile(rootPath+'/世界总体疫情信息')
    file.save(rootPath+'/世界总体疫情信息/世界总体疫情信息.xlsx')

    # return foreign_name, foreign_total_confirm, foreign_total_nowConfirm, foreign_total_dead, \
    #        foreign_total_heal

# 各国各地区疫情信息
def foreign_children_data():
    foreign_data = all_data
    for country in foreign_data:
        country_name = list()
        country_date = list()
        country_nameMap = list()
        country_isUpdated = list()
        country_confirmAdd = list()
        country_confirmAddCut = list()
        country_confirm = list()
        country_suspect = list()
        country_dead = list()
        country_heal = list()
        if 'children' in country:
            for children in country['children']:
                country_name.append(children['name'])
                country_date.append(children['date'])
                country_nameMap.append(children['nameMap'])
                country_isUpdated.append(children['isUpdated'])
                country_confirmAdd.append(int(children['confirmAdd']))
                country_confirmAddCut.append(int(children['confirmAddCut']))
                country_confirm.append(int(children['confirm']))
                country_suspect.append(int(children['suspect']))
                country_dead.append(int(children['dead']))
                country_heal.append(int(children['heal']))
            # 指定file以utf-8的格式打开
            file = Workbook(encoding='utf-8')
            # 指定打开的文件名
            table = file.add_sheet('data')
            t2_name = ['name', 'date', 'nameMap', 'isUpdated', 'confirmAdd',
                       'confirmAddCut', 'confirm', 'suspect', 'dead', 'heal']
            for i in range(len(t2_name)):
                table.write(0, i, t2_name[i])
            for i in range(len(country_name)):
                table.write(i + 1, 0, country_name[i])
                table.write(i + 1, 1, country_date[i])
                table.write(i + 1, 2, country_nameMap[i])
                table.write(i + 1, 3, country_isUpdated[i])
                table.write(i + 1, 4, country_confirmAdd[i])
                table.write(i + 1, 5, country_confirmAddCut[i])
                table.write(i + 1, 6, country_confirm[i])
                table.write(i + 1, 7, country_suspect[i])
                table.write(i + 1, 8, country_dead[i])
                table.write(i + 1, 9, country_heal[i])
            cf.createFile(rootPath+'/各国各地区疫情信息')
            file.save(rootPath+'/各国各地区疫情信息/' + country['name'] + '.xlsx')

def main():
    foreign_total_data()
    foreign_children_data()

if __name__ == '__main__':
    main()
