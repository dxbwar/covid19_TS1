#Figure of CoVid-19 Case in Middlesbrough(Python version)
#Coded by dxb 05-05-2020
#Update on 05-06-2020

import numpy
import matplotlib.pyplot
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#import datetime

#Data source Need to update by day
#cases data from the UK government
cases = [1, 1, 1, 3, 7, 9, 13, 17, 19, 26, 33, 44, 59, 74, 92, 111, 126, 151, 169, 196, 213,\
    235, 237, 258, 274, 291, 302, 325, 346, 354, 367, 394, 407, 413, 427, 451, 472, 481, 496,\
    509, 509, 541, 554, 559, 566, 582, 588, 589, 600, 615, 619, 624, 626, 628, 630, 631, 632,\
    633, 634, 634]
#deaths data from NHS
dcases = [1, 1, 1, 1, 1, 1, 1, 2, 4, 4, 4, 11, 15, 30, 35, 43, 48, 49, 59, 69, 73, 78, 79, 83,\
    83, 100, 106, 122, 126, 134, 134, 134, 141, 151, 157, 157, 166, 166, 166, 172, 178, 180,\
    185, 189, 189, 189, 196, 199, 199, 204, 204, 204, 204, 210, 213, 214, 215, 216, 216, 216]

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
enincrease.insert(-1,enincrease[-1])
enincrease.insert(-1,enincrease[-1])
endincrease = dincrease.copy()
endincrease.insert(0,endincrease[0])
endincrease.insert(0,endincrease[0])
endincrease.insert(-1,endincrease[-1])
endincrease.insert(-1,endincrease[-1])
avincrease = increase.copy()
avdincrease = dincrease.copy()
for i in range(len(avincrease)):
    avincrease[i] = (enincrease[i]+enincrease[i+1]+enincrease[i+2]+enincrease[i+3]+enincrease[i+4]) / 5.0
    avdincrease[i] = (endincrease[i]+endincrease[i+1]+endincrease[i+2]+endincrease[i+3]+endincrease[i+4]) / 5.0

#Plot
fig = matplotlib.pyplot.figure()
matplotlib.pyplot.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
matplotlib.pyplot.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号
#Total cases plot
ax1 = matplotlib.pyplot.subplot(2,1,1)
ax1.plot(cases, linewidth='1', color='blue', linestyle='-', marker='*', label="总确诊数 Total Cases")
ax1.plot(dcases, linewidth='1', color='red', linestyle='-', marker='o', label="总死亡数 Total Death")
matplotlib.pyplot.title('米德尔斯堡新冠病毒累计确诊及詹姆斯库克大学医院累计死亡病例\n\
    Total Comfirmed Cases of CoVID-19 in Middlesbrough & Total Dead Cases at the James Cook University Hospital')
matplotlib.pyplot.ylabel('病例数 Cases') 
matplotlib.pyplot.xlabel('天数 Days')
ax1.legend(loc = 'upper left')
step1 = 5
while (max(cases)/16)>step1:
    step1 = step1 + 5
matplotlib.pyplot.ylim(0, step1*16)
matplotlib.pyplot.xlim(0, len(cases)-1)
ax1.yaxis.set_major_locator(MultipleLocator(step1*2))
ax1.yaxis.set_minor_locator(MultipleLocator(step1))
ax1.yaxis.grid(True, which='both')
ax1.xaxis.grid(True)

ax2 = matplotlib.pyplot.subplot(2,1,2)
ax2.plot(increase, linewidth='0.5', color='cadetblue', linestyle=':', marker='*', label = "新增确诊    Daily Cases")
ax2.plot(avincrease, linewidth='1', color='blue', linestyle='-', label = '确诊5日均值 Average of 5 days Cases')
ax2.plot(dincrease, linewidth='1', color='pink', linestyle=':', marker='o', label = '新增死亡    Daily Deaths')
ax2.plot(avdincrease, linewidth='1', color='red', linestyle='-', label = '死亡5日均值 Average of 5 days Deaths')
ax2.legend(loc = 'upper left')
matplotlib.pyplot.title('米德尔斯堡新冠病毒日增确诊及詹姆斯库克大学医院日增死亡病例\n\
    Daily Comfirmed Cases of CoVID-19 in Middlesbrough & Daily Dead Cases at the James Cook University Hospital')
matplotlib.pyplot.ylabel('病例数 Cases') 
matplotlib.pyplot.xlabel('天数 Days')
step2 = 2
while ((max(increase)-min(increase))/16)>step2:
    step2 = step2 + 1
    print(step2)
matplotlib.pyplot.ylim(min(0,min(increase)), step2*16)
matplotlib.pyplot.xlim(0, len(increase)-1)
ax2.yaxis.set_major_locator(MultipleLocator(step2*2))
ax2.yaxis.set_minor_locator(MultipleLocator(step2))
ax2.yaxis.grid(True, which='both')
ax2.xaxis.grid(True)
matplotlib.pyplot.grid(True)
figManager = matplotlib.pyplot.get_current_fig_manager()
figManager.resize(*figManager.window.maxsize())
matplotlib.pyplot.subplots_adjust(left=0.05, right=0.99, top=0.9, bottom=0.08, wspace=0, hspace=0.4)
matplotlib.pyplot.show()

# Save figure
print('savefig...')
fig.savefig('COVID19_TS1.pdf')
