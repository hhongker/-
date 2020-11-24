from data_get import getData
from xlwt import *
import os
from util import dealWithFile as cf
from util import dealWithFile as dwf

province_name, city_name = getData.getProvinceCity()
rootPath = dwf.rootPath

# 各省份每日疫情数据
def province_trend():
    # province_trend_data = {}
    for p_name in province_name:
        t = getData.getProvinceTrendData(p_name)
        # province_trend_data[p_name] = t
        p_date = list()
        p_confirm = list()
        p_dead = list()
        p_heal = list()
        p_confirm_add = list()
        p_confirm_cuts = list()
        p_dead_cuts = list()
        p_now_confirm_cuts = list()
        p_heal_cuts = list()
        p_newConfirm = list()
        p_newHeal = list()
        p_newDead = list()
        p_description = list()
        for day in t:
            p_date.append(day['date'][:2] + "/" + day['date'][3:])
            p_confirm.append(int(day['confirm']))
            p_dead.append(int(day['dead']))
            p_heal.append(int(day['heal']))
            p_confirm_add.append(day['confirm_add'])
            p_confirm_cuts.append(day['confirm_cuts'])
            p_dead_cuts.append(day['dead_cuts'])
            p_now_confirm_cuts.append(day['now_confirm_cuts'])
            p_heal_cuts.append(day['heal_cuts'])
            p_newConfirm.append(int(day['newConfirm']))
            p_newHeal.append(int(day['newHeal']))
            p_newDead.append(int(day['newDead']))
            p_description.append(day['description'])
        # 指定file以utf-8的格式打开
        file = Workbook(encoding='utf-8')
        # 指定打开的文件名
        table = file.add_sheet('data')
        t1_name = ['date', 'confirm', 'dead', 'heal', 'confirm_add', 'confirm_cuts', 'dead_cuts', 'now_confirm_cuts', 'heal_cuts', 'newConfirm', 'newHeal', 'newDead', 'description']
        for i in range(len(t1_name)):
            table.write(0, i, t1_name[i])
        for i in range(len(p_date)):
            table.write(i + 1, 0, p_date[i])
            table.write(i + 1, 1, p_confirm[i])
            table.write(i + 1, 2, p_dead[i])
            table.write(i + 1, 3, p_heal[i])
            table.write(i + 1, 4, p_confirm_add[i])
            table.write(i + 1, 5, p_confirm_cuts[i])
            table.write(i + 1, 6, p_dead_cuts[i])
            table.write(i + 1, 7, p_now_confirm_cuts[i])
            table.write(i + 1, 8, p_heal_cuts[i])
            table.write(i + 1, 9, p_newConfirm[i])
            table.write(i + 1, 10, p_newHeal[i])
            table.write(i + 1, 11, p_newDead[i])
            table.write(i + 1, 12, p_description[i])
        cf.createFile(rootPath+'/中国各省市历史疫情信息')
        file.save(rootPath+'/中国各省市历史疫情信息/'+p_name+'.xlsx')

    # # 将{'省份':[{'每日疫情数据'}]}字典封存为province_trend_data.json
    # with open('province_trend_data.json', 'w', encoding='utf-8') as f:
    #     json.dump(province_trend_data, f, ensure_ascii=False)
    # return province_trend_data

# 各城市每日疫情数据
def city_trend():
    error_province_city = list()
    # city_trend_data = {}
    file_name = rootPath+'/中国各省的城市历史疫情信息/'
    for p_name in city_name:
        a = city_name[p_name][0].split(';')
        f = file_name + p_name
        if not os.path.exists(f):
            os.makedirs(f)
        # city_data = list()
        for c_name in a:
            t = getData.getCityTrendData(p_name, c_name)
            # city_data[c_name] = t
            c_date = list()
            c_confirm = list()
            c_dead = list()
            c_heal = list()
            c_suspect = list()
            c_confirm_add = list()
            # print(p_name,c_name)
            if t != None:
                for day in t:
                    c_date.append(day['date'][:2] + "/" + day['date'][3:])
                    c_confirm.append(int(day['confirm']))
                    c_dead.append(int(day['dead']))
                    c_heal.append(int(day['heal']))
                    c_suspect.append(int(day['suspect']))
                    c_confirm_add.append(day['confirm_add'])
                    # 指定file以utf-8的格式打开
                file = Workbook(encoding='utf-8')
                # 指定打开的文件名
                table = file.add_sheet('data')
                t2_name = ['date', 'confirm', 'dead', 'heal', 'suspect', 'confirm_add']
                for i in range(len(t2_name)):
                    table.write(0, i, t2_name[i])
                for i in range(len(c_date)):
                    table.write(i + 1, 0, c_date[i])
                    table.write(i + 1, 1, c_confirm[i])
                    table.write(i + 1, 2, c_dead[i])
                    table.write(i + 1, 3, c_heal[i])
                    table.write(i + 1, 4, c_suspect[i])
                    table.write(i + 1, 5, c_confirm_add[i])
                file.save(f + '/' + c_name + '.xlsx')
            else:
                error_province_city.append(p_name+c_name)


    # # 将{'省份':{'城市':[{'每日疫情数据'}]}}字典封存为city_trend_data.json
    # with open('city_trend_data.json', 'w', encoding='utf-8') as f:
    #     json.dump(city_trend_data, f, ensure_ascii=False)
    # return city_trend_data

def main():
    province_trend()
    city_trend()

if __name__ == '__main__':
    main()