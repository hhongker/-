from data_get import getForeignData, getChinaData, getProvinceData, getProvinceTrend, getForeignTrend
from util import dealWithFile as cf


def allRun():
    #创建数据目录data
    cf.createFile()
    # 国外疫情数据
    getForeignData.main()
    # 国内疫情数据
    getChinaData.main()
    # 中国各省市(区)疫情数据
    getProvinceData.main()
    # 中国各省市(区)历史疫情数据
    getProvinceTrend.main()
    # 国外历史疫情数据
    getForeignTrend.main()

if __name__ == "__main__":
    allRun()