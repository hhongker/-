from flask import Flask,render_template
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor
import json as  jo

from util import dealWithFile as dwf

app = Flask(__name__)


# 1.定义执行器
exeutors = {
    "default":ProcessPoolExecutor(max_workers=10)
}
# 2.创建调度器
app.scheduler = BackgroundScheduler(exeutors=exeutors)
# 启动定时任务(定时爬虫)
app.scheduler.add_job(dwf.create_data, 'interval', days=1, id="1")
app.scheduler.start()

#初始化
# dwf.create_data()


# 数据准备
data = jo.loads(dwf.read_to_file('data/photos/今日新增数据.json'))

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route("/index")
def index():
    return render_template("index.html",data=data)
# ===================================chinaMap=======================================
@app.route("/")
@app.route("/chinaMap")
def chinaMap():
    return render_template("chinaMap.html",data=data)

@app.route("/analyse1_1")
def analyse1_1(): #新增确诊人数
    return dwf.read_to_file("data/data_worldMapView/时间轴图像/中国总体疫情变化.txt")
    # return dwf.read_to_file("data/data_cnMapView/绘制中国累计确诊人数地图.txt")
@app.route("/analyse1_2")
def analyse1_2(): #新增确诊人数
    return dwf.read_to_file("data/data_cnMapView/中国疫情地图（新增确诊人数）.txt")
@app.route("/analyse1_3")
def analyse1_3(): #现存确诊人数
    return dwf.read_to_file("data/data_cnMapView/中国疫情地图（现存确诊人数）.txt")
@app.route("/analyse1_4")
def analyse1_4(): #累计确诊人数
    return dwf.read_to_file("data/data_cnMapView/中国疫情地图（累计确诊人数）.txt")
@app.route("/analyse1_5")
def analyse1_5(): #累计治愈人数
    return dwf.read_to_file("data/data_cnMapView/中国疫情地图（累计治愈人数）.txt")
@app.route("/analyse1_6")
def analyse1_6(): #累计死亡人数
    return dwf.read_to_file("data/data_cnMapView/中国疫情地图（累计死亡人数）.txt")
@app.route("/analyse1_7")
def analyse1_7(): #每日新增信息
    return dwf.read_to_file("data/data_DaliyChangeView/中国每日新增信息.txt")
@app.route("/analyse1_8")
def analyse1_8():#中国疫情历史总体信息
    return dwf.read_to_file("data/data_analyse/中国每日治疗率、死亡率.txt")
@app.route("/analyse1_9")
def analyse1_9():#每日治疗率、死亡率
    return dwf.read_to_file("data/data_DaliyChangeView/中国各省境外输入信息.txt")
@app.route("/analyse1_10")
def analyse1_10():#各省境外输入信息
    return dwf.read_to_file("data/data_DaliyChangeView/中国每日新增信息.txt")
@app.route("/analyse1_11")
def analyse1_11():#每日新增信息
    return dwf.read_to_file("data/data_DaliyChangeView/中国每日治疗率.txt")
@app.route("/analyse1_12")
def analyse1_12():#每日治疗率
    return dwf.read_to_file("data/data_DaliyChangeView/中国疫情历史总体信息.txt")

# ===================================chinaCitysAnalyse=======================================
@app.route("/chinaCitysAnalyse")
def analyse2():
    return render_template("chinaCitysAnalyse.html",data=data)

@app.route("/analyse2_2")
def analyse2_2(): #中国各省市总体疫情信息
    return dwf.read_to_file("data/data_analyse/中国各省市总体疫情信息.txt")
@app.route("/analyse2_3")
def analyse2_3(): #中国各省市(区)治疗率、死亡率
    return dwf.read_to_file("data/data_analyse/中国各省市(区)治疗率、死亡率.txt")
@app.route("/analyse2_4")
def analyse2_4(): #中国各省市(区)今日新增疫情信息
    return dwf.read_to_file("data/data_worldMapView/中国各省市总体疫情信息/中国各省市(区)今日新增疫情信息.txt")
@app.route("/analyse2_5")
def analyse2_5(): #中国各省市总体疫情信息
    return dwf.read_to_file("data/data_worldMapView/中国各省市总体疫情信息/中国各省市总体疫情信息.txt")

# ===================================worldChange=======================================
@app.route("/worldChange")
def worldChange():
    return render_template("worldChange.html",data=data)

@app.route("/analyse3_2")
def analyse3_2(): #世界总体疫情变化
    return dwf.read_to_file("data/data_worldMapView/时间轴图像/世界总体疫情变化.txt")
@app.route("/analyse3_3")
def analyse3_3(): #世界疫情信息
    return dwf.read_to_file("data/data_analyse/世界疫情信息.txt")
@app.route("/analyse3_4")
def analyse3_4(): #世界疫情其他信息
    return dwf.read_to_file("data/data_analyse/世界疫情其他信息.txt")
@app.route("/analyse3_5")
def analyse3_5(): #世界总的死亡率、治疗率、存活率
    return dwf.read_to_file("data/data_analyse/世界总的死亡率、治疗率、存活率.txt")

# ===================================OtherMessage=======================================
@app.route("/OtherMessage")
def OtherMessage():
    return render_template("OtherMessage.html",data=data)

@app.route("/analyse4_3")
def analyse4_3(): #各大洲总信息
    return dwf.read_to_file("data/data_DaliyChangeView/各大洲总信息.txt")
@app.route("/analyse4_4")
def analyse4_4(): #各大洲治愈信息
    return dwf.read_to_file("data/data_DaliyChangeView/各大洲治愈信息.txt")
@app.route("/analyse4_5")
def analyse4_5(): #各大洲现存确诊信息
    return dwf.read_to_file("data/data_DaliyChangeView/各大洲现存确诊信息.txt")
@app.route("/analyse4_6")
def analyse4_6(): #各大洲确诊信息
    return dwf.read_to_file("data/data_DaliyChangeView/各大洲确诊信息.txt")

@app.route("/analyse4_7")
def analyse4_7(): #疫情严重程度排名前十国家（折线图）
    return dwf.read_to_file("data/data_DaliyChangeView/疫情严重程度排名前十国家（折线图）.txt")
@app.route("/analyse4_8")
def analyse4_8(): #疫情严重程度排名前十国家（柱状图）
    return dwf.read_to_file("data/data_DaliyChangeView/疫情严重程度排名前十国家（柱状图）.txt")


if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0',port= 80, debug=True)