import requests
import json
import collections


# 全国疫情数据
chinatotal_h5_url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
# 国内疫情趋势数据
chinatotal_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
# 省区信息请求网址
province_city_url = "https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_city_list_order"
# 省一级及区一级详细信息请求地址(后面跟省/地级市中文)
provincetotal_url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province='
# 国外疫情数据
foreigntotal_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign'
# 国外疫情趋势数据(后面跟国家中文)
foreigntotal_country_url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country='

# 中国这个国家的疫情数据
def getChinaAbsData():
    response = requests.get(chinatotal_h5_url).json()
    data = json.loads(response['data'])
    return data['chinaTotal']

# 中国各省份总疫情数据
def getProvinceTotalData():
    response = requests.get(chinatotal_h5_url).json()
    data = json.loads(response['data'])
    areaTree = data['areaTree'][0]['children']
    return areaTree

# 中国省份名称，各省份里的地级城市名称
def getProvinceCity():
    response = requests.get(province_city_url).json()  # 发出请求并json化处理
    data = json.loads(response['data'])
    province = list()
    city = collections.defaultdict(list)
    for i in range(len(data)):
        province.append(data[i]['province'])
        city[data[i]['province']].append(data[i]['city'])
    return province, city

# 国内疫情数据
def getChinaTotalData():
    response = requests.get(chinatotal_url).json()
    data = json.loads(response['data'])
    return data

# 国外疫情数据
def getForeignTotalData():
    response = requests.get(foreigntotal_url).json()
    data = json.loads(response['data'])
    foreignList = data['foreignList']
    return foreignList

# 省份每日数据
def getProvinceTrendData(procince_name):
    response = requests.get(provincetotal_url + procince_name).json()
    data = response['data']
    return data

# 城市每日数据
def getCityTrendData(procince_name, city_name):
    response = requests.get(provincetotal_url + procince_name + '&city=' +city_name).json()
    data = response['data']
    return data

# 各国每日数据
def getForeignTrendData(foreign_name):
    response = requests.get(foreigntotal_country_url + foreign_name).json()
    data = response['data']
    return data


