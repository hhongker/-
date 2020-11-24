import os

rootPath = './data/' #所有数据的根目录
flag = 1 #是否将画图的数据持久化

# savaPath1 ='./data/data_Map_analyse1/' #分析1的目录
# savaPath3 ='./data/data_Map_analyse2/' #分析3的目录


savaPathAnalyse = './data/data_analyse/'
saveDataCnMapView = './data/data_cnMapView/'
saveDaliyChangeView = './data/data_DaliyChangeView/'
saveWorldMapView = './data/data_worldMapView/'
saveDataGridJson = './static/'

saveStatistics = './data/photos/'
def createFile(savePath=rootPath):
    if not os.path.exists(savePath):
        os.mkdir(savePath)

def write_to_file(path=rootPath+'/data1/a.txt',writeData="None"):
    createFile(os.path.dirname(path))
    with open(path,"w+",encoding="utf-8") as f:
        f.write(writeData)

def read_to_file(path=rootPath+'/data1/a.txt'):
    ff = open(path,"r+",encoding="utf-8")
    f = ff.read()
    ff.close()
    return f

def create_data():
    print("任务启动成功了！！！")
    # from data_analysis import analyse1
    # from data_analysis import analyse2
    # analyse1.allRun()
    # analyse2.allRun()

    #爬虫爬取数据
    from data_get import getAllData
    getAllData.allRun()
    #数据的分析处理
    from data_analysis import analyse,cnMapView,daliyChangesView,worldMapView,statistics,dataGridJson
    statistics.new_static()
    analyse.main()
    cnMapView.main()
    daliyChangesView.main()
    worldMapView.main()
    dataGridJson.main()






