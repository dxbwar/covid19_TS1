%Figure of CoVid-19 Case in Middlesbrough
%Coded by dxb 2020.4.1
%Revised on 06-08-2020
%Updated on 06-17-2020

%Data source Need to update by day
%cases data from the UK government
cases = [1 1 1 3 7 9 13 17 19 26 33 44 59 74 92 111 126 151 169 196 213 ...
    235 237 258 274 291 302 325 346 354 367 394 407 413 427 451 472 481 ...
    496 509 509 541 554 559 566 582 588 589 600 615 619 624 626 628 630 ...
    631 632 633 634 634 638 645 652 656 659 665 667 668 670 673 676 676 ...
    676 677 678 678 679 680 683 685 685 687 688 688 689 691 691 691 692 ...
    694];
%deaths data from NHS
dcases = [1 1 1 1 1 1 1 2 4 4 4 11 15 30 35 43 48 49 59 69 73 78 79 83 ...
    83 100 106 122 126 134 134 134 141 151 157 157 166 166 166 172 178 ...
    180 185 189 189 189 196 199 199 204 204 204 204 210 213 214 215 216 ...
    216 216 217 220 221 223 223 223 223 223 226 228 229 231 231 231 237 ...
    238 238 241 241 241 241 245 246 248 248 248 248 248 250 250];

%Initial
%Date config
startDate = datenum('3-20-2020');
days = length(cases);
endDate = startDate + days-1;
xData = linspace(startDate,endDate,days);
%Data Calculation
casess=[0 cases(1:days-1)];     
increase = cases-casess;        %Daily cases calculation
dcasess=[0 dcases(1:days-1)];
dincrease = dcases-dcasess;     %Daily Death calculation
%Average of 5 days calculation
avincrease = zeros(1,length(increase));
enincrease = [increase(1) increase(1) increase increase(end) increase(end)];
avdincrease = zeros(1,length(dincrease));
endincrease = [dincrease(1) dincrease(1) dincrease dincrease(end) dincrease(end)];
for i=1:1:length(increase)
    avincrease(i) = (enincrease(i)+enincrease(i+1)+enincrease(i+2)+enincrease(i+3)+enincrease(i+4))/5.0;
    avdincrease(i) = (endincrease(i)+endincrease(i+1)+endincrease(i+2)+endincrease(i+3)+endincrease(i+4))/5.0;
end

%Maximize the figure window, refer from https://blog.csdn.net/am290333566/java/article/details/84581313
h = figure();				                                        % 创建图形窗口
warning('off','MATLAB:HandleGraphics:ObsoletedProperty:JavaFrame');	% 关闭相关的警告提示（因为调用了非公开接口）
jFrame = get(h,'JavaFrame');	                                    % 获取底层 Java 结构相关句柄吧
pause(0.1);					                                        % 在 Win 10，Matlab 2017b 环境下不加停顿会报 Java 底层错误。各人根据需要可以进行实验验证
set(jFrame,'Maximized',1);	                                        %设置其最大化为真（0 为假）
pause(0.1);					                                        % 个人实践中发现如果不停顿，窗口可能来不及变化，所获取的窗口大小还是原来的尺寸。各人根据需要可以进行实验验证
warning('on','MATLAB:HandleGraphics:ObsoletedProperty:JavaFrame');	% 打开相关警告设置

%Total cases plot
subplot(2,1,1);
plot(xData,cases,'-*b',xData,dcases,'-or')
grid on
%title config
t1 = "米德尔斯堡新冠病毒累计确诊及詹姆斯库克大学医院累计死亡病例";
t2 = t1 + newline + "Total Comfirmed Cases of CoVID-19 in Middlesbrough & Total Dead Cases at the James Cook University Hospital";
title(t2)
xlabel('日期 Date')
ylabel('病例数 Cases')
%X scale config
tick1 = 5;
while (cases(end)/16)>tick1
    tick1 = tick1 + 5;
end 
set(gcf, 'Color', [1,1,1])
set(gca,'ytick',0:tick1:cases(end)+tick1);
set(gca,'xtick',startDate:5:startDate+days);
datetick('x','mm/dd')
set(gca,'xlim',[startDate,endDate]);
set(gca,'ylim',[0,cases(end)+tick1]);
legend('总确诊数 Total Cases','总死亡数 Total Death','Location','NorthWest')

%Daily cases plot
subplot(2,1,2);
plot(xData,increase,':*b',xData,avincrease,'-b',xData,dincrease,':or',xData,avdincrease,'-r')
grid on
%Title config
t3 = "米德尔斯堡新冠病毒日增确诊及詹姆斯库克大学医院日增死亡病例";
t4 = t3 + newline + "Daily Comfirmed Cases of CoVID-19 in Middlesbrough & Daily Dead Cases at the James Cook University Hospital";
title(t4)
xlabel('日期 Date')
ylabel('病例数 Cases')
tick2 = 2;
[mIn0, pIn0] = max(increase);
while (increase(pIn0)/16)>tick2
    tick2 = tick2 + 2;
end  
set(gca,'ytick',0:tick2:increase(pIn0)+tick2);
set(gca,'ylim',[0,increase(pIn0)+tick2]);
set(gca,'xtick',startDate:7:startDate+days);
datetick('x','mm/dd')
set(gca,'xlim',[startDate,endDate]);
legend('新增确诊       Daily Cases','确诊5日均值 Average of 5 days Cases','新增死亡       Daily Deaths','死亡5日均值 Average of 5 days Deaths','Location','NorthEast')

saveas(gcf, 'COVID19_TS1.jpg')
