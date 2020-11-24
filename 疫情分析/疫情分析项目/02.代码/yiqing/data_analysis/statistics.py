import pandas as pd
from util import dealWithFile as dwf

readPath = dwf.rootPath
savePath = dwf.saveStatistics


def new_static():
    dwf.createFile(savePath)
    data1 = pd.read_excel(readPath+'/中国总体历史疫情信息/历史每日新增信息.xlsx')
    data2 = pd.read_excel(readPath+'/中国总体历史疫情信息/历史总体信息.xlsx')
    data3 = pd.read_excel(readPath+'/世界总体疫情信息/世界总体疫情信息.xlsx')
    a = data3.sum()
    a['name'] = '世界'
    a['continent'] = '世界'
    data1.iloc[-1, :].to_json(savePath+'/今日历史数据.json')
    data2.iloc[-1, :].to_json(savePath+'/今日新增数据.json')
    a.to_json(savePath+'/世界最新数据.josn')


if __name__ == '__main__':
    new_static()