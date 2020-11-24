import xlrd
from collections import OrderedDict
import json
import codecs

from util import dealWithFile as dwf

readPath = dwf.rootPath
savePath = dwf.saveDataGridJson

def xlsx_to_json(getname,savename):
    # wb = xlrd.open_workbook('../data/中国各省市总体疫情信息/中国各省市总体疫情信息.xlsx')
    wb = xlrd.open_workbook(readPath+getname)
    convert_list = []
    sh = wb.sheet_by_index(0)
    title = sh.row_values(0)
    for rownum in range(1, sh.nrows):
        rowvalue = sh.row_values(rownum)
        single = OrderedDict()
        for colnum in range(0, len(rowvalue)):
            single[title[colnum]] = rowvalue[colnum]
        convert_list.append(single)

    j = json.dumps(convert_list)
    # with codecs.open('../static/json/data1.txt', "w", "utf-8") as f:
    #     f.write(j)
    with codecs.open(savePath+'json/'+savename, "w", "utf-8") as f:
        f.write(j)
def main():
    xlsx_to_json('中国各省市总体疫情信息/中国各省市总体疫情信息.xlsx','中国各省市总体疫情信息.txt')
    xlsx_to_json('世界总体疫情信息/世界总体疫情信息.xlsx', '世界总体疫情信息.txt')
    xlsx_to_json('中国各省市疫情信息/广东.xlsx','广东.txt')
    xlsx_to_json('各国各地区疫情信息/美国.xlsx', '美国.txt')

if __name__=='__main__':
    main()