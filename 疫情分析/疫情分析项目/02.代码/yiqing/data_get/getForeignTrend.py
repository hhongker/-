from data_get import getData, getForeignData
from xlwt import *
from util import dealWithFile as cf
from util import dealWithFile as dwf

all_data = getData.getForeignTotalData()
rootPath = dwf.rootPath


# 各国每日数据
def foreign_trend():
    # 获取国家名字
    foreign_data = all_data
    foreign_name = list()
    for country in foreign_data:
        foreign_name.append(country['name'])  # 国家名字

    # 获取各国每日数据
    # foreign_trend_data = {}
    for name in foreign_name:
        t = getData.getForeignTrendData(name)
        # foreign_trend_data[name] = t
        foreign_every_date = list()
        foreign_every_confirm_add = list()
        foreign_every_confirm = list()
        foreign_every_heal = list()
        foreign_every_dead = list()
        for day in t:
            foreign_every_date.append(day['date'][:2] + "/" + day['date'][3:])
            foreign_every_confirm_add.append(int(day['confirm_add']))
            foreign_every_confirm.append(int(day['confirm']))
            foreign_every_heal.append(int(day['heal']))
            foreign_every_dead.append(int(day['dead']))
        # 指定file以utf-8的格式打开
        file = Workbook(encoding='utf-8')
        # 指定打开的文件名
        table = file.add_sheet('data')
        t1_name = ['date', 'confirm_add', 'confirm', 'heal', 'dead']
        for i in range(len(t1_name)):
            table.write(0, i, t1_name[i])
        for i in range(len(foreign_every_date)):
            table.write(i + 1, 0, foreign_every_date[i])
            table.write(i + 1, 1, foreign_every_confirm_add[i])
            table.write(i + 1, 2, foreign_every_confirm[i])
            table.write(i + 1, 3, foreign_every_heal[i])
            table.write(i + 1, 4, foreign_every_dead[i])
        cf.createFile(rootPath+'/各国历史疫情信息')
        file.save(rootPath+'/各国历史疫情信息/'+name+'.xlsx')

    # # 将{'国家':[{'每日疫情数据'}]}字典封存为foreign_trend_data.json
    # with open('foreign_trend_data.json', 'w', encoding='utf-8') as f:
    #     json.dump(foreign_trend_data, f, ensure_ascii=False)
    # return foreign_trend_data

def main():
    foreign_trend()


if __name__ == '__main__':

    main()