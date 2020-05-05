#Figure of CoVid-19 Case in Middlesbrough(Python version)
#Coded by dxb 05-05-2020

#import numpy
import matplotlib.pyplot
#import datetime

#Data source Need to update by day
#cases data from the UK government
cases = [1, 1, 1, 3, 7, 9, 13, 17, 19, 26, 33, 44, 59, 74, 92, 111, 126, 151, 169, 196, 213,\
    235, 237, 258, 274, 291, 302, 325, 346, 354, 367, 394, 407, 413, 427, 451, 472, 481, 496,\
    509, 509, 541, 554, 559, 566, 582]
#deaths data from NHS
dcases = [1, 1, 1, 1, 1, 1, 1, 2, 4, 4, 4, 11, 15, 30, 35, 43, 48, 49, 59, 69, 73, 78, 79, 83,\
    83, 100, 106, 122, 126, 134, 134, 134, 141, 151, 157, 157, 166, 166, 166, 172, 178, 180,\
    185, 189, 189, 189]

#Initial
#Date config
days = len(cases)                   #获取list长度
#Data Calculation
casess = cases.copy()               #list复制
casess.insert(0,0)                  #在casess头插入0
casess.pop()                        #删除list最后一元素
increase = list(map(lambda x: x[0]-x[1], zip(cases, casess)))   #用lambda表达式计算list对应元素之差
dcasess = dcases.copy()             #list复制
dcasess.insert(0,0)                 #在casess头插入0
dcasess.pop()                       #删除list最后一元素
dincrease = list(map(lambda x: x[0]-x[1], zip(dcases, dcasess)))   #用lambda表达式计算list对应元素之差
#Average of 5 days calculation
enincrease = increase.copy()
enincrease.insert(0,enincrease[0])
enincrease.insert(0,enincrease[0])
enincrease.insert(len(enincrease)-1,enincrease[len(enincrease)-1])
enincrease.insert(len(enincrease)-1,enincrease[len(enincrease)-1])
endincrease = dincrease.copy()
endincrease.insert(0,endincrease[0])
endincrease.insert(0,endincrease[0])
endincrease.insert(len(endincrease)-1,endincrease[len(endincrease)-1])
endincrease.insert(len(endincrease)-1,endincrease[len(endincrease)-1])
avincrease = increase.copy()
avdincrease = dincrease.copy()
for i in range(len(avincrease)):
    avincrease[i] = (enincrease[i]+enincrease[i+1]+enincrease[i+2]+enincrease[i+3]+enincrease[i+4]) / 5.0
    avdincrease[i] = (endincrease[i]+endincrease[i+1]+endincrease[i+2]+endincrease[i+3]+endincrease[i+4]) / 5.0

#Plot
matplotlib.pyplot.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
matplotlib.pyplot.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号
#Total cases plot
matplotlib.pyplot.subplot(2,1,1)
matplotlib.pyplot.plot(cases, '-*b', label="总确诊数 Total Cases")
matplotlib.pyplot.plot(dcases, '-or', label="总死亡数 Total Death")
matplotlib.pyplot.title('米德尔斯堡新冠病毒累计确诊及詹姆斯库克大学医院累计死亡病例\n\
    Total Comfirmed Cases of CoVID-19 in Middlesbrough & Total Dead Cases at the James Cook University Hospital')
matplotlib.pyplot.ylabel('病例数 Cases') 
matplotlib.pyplot.xlabel('日期 Date')
matplotlib.pyplot.legend(loc = 'upper left')
matplotlib.pyplot.grid()

matplotlib.pyplot.subplot(2,1,2)
matplotlib.pyplot.plot(increase, ':*b', label = "新增确诊    Daily Cases")
matplotlib.pyplot.plot(avincrease, '-b', label = '确诊5日均值 Average of 5 days Cases')
matplotlib.pyplot.plot(dincrease, ':or', label = '新增死亡    Daily Deaths')
matplotlib.pyplot.plot(avdincrease,'-r', label = '死亡5日均值 Average of 5 days Deaths')
matplotlib.pyplot.legend(loc = 'upper left')
matplotlib.pyplot.title('米德尔斯堡新冠病毒日增确诊及詹姆斯库克大学医院日增死亡病例\n\
    Daily Comfirmed Cases of CoVID-19 in Middlesbrough & Daily Dead Cases at the James Cook University Hospital')
matplotlib.pyplot.ylabel('病例数 Cases') 
matplotlib.pyplot.xlabel('日期 Date')
matplotlib.pyplot.grid()
figManager = matplotlib.pyplot.get_current_fig_manager()
figManager.resize(*figManager.window.maxsize())
matplotlib.pyplot.subplots_adjust(left=0.05, right=0.99, top=0.9, bottom=0.08, wspace=0, hspace=0.4)
matplotlib.pyplot.show()

