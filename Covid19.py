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
days = len(cases)               #获取list长度
#Data Calculation
casess = cases.copy()           #list复制
casess.insert(0,0)              #在casess头插入0
casess.pop()                    #删除list最后一个元素
increase = list(map(lambda x: x[0]-x[1], zip(cases, casess)))   #用lambda表达式计算list对应元素之差
dcasess = dcases.copy()           #list复制
dcasess.insert(0,0)              #在casess头插入0
dcasess.pop()                    #删除list最后一个元素
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
print(enincrease)

#Total cases plot
matplotlib.pyplot.subplot(2,1,1)
matplotlib.pyplot.plot(cases)
matplotlib.pyplot.plot(dcases)
matplotlib.pyplot.grid()
#Daily cases plot
matplotlib.pyplot.subplot(2,1,2)
matplotlib.pyplot.plot(increase)
matplotlib.pyplot.plot(avincrease)
matplotlib.pyplot.plot(dincrease)
matplotlib.pyplot.plot(avdincrease)
figManager = matplotlib.pyplot.get_current_fig_manager()
figManager.resize(*figManager.window.maxsize())
matplotlib.pyplot.grid()
matplotlib.pyplot.show()

