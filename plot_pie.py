import matplotlib.pyplot as plt
import numpy as np
#饼状图
#绘制饼状图，需要使用plot.pie()函数，说明文档中各参数的属性取值及其所代表的意思是：
#x
#数据
#list(代表可传入的参数对象是list类型)

#labels
#标签
#list(代表可传入的参数对象是list类型)

#autopct
#数据标签
#%0.1%% 保留一位小数

#explode
#突出的部分
#list(代表可传入的参数对象是list类型)


#shadow
#是否显示阴影
#bool(代表可取的参数对象是布尔类型)


#pctdistance
#数据标签的距离圆心位置
#0~1(代表可取的参数对象是0-1)


#labeldistance
#标签的比例
#float(代表可传入的参数对象是float类型)


#startangle
#开始绘图的角度
#float(代表可传入的参数对象是float类型)


#radius
#半径长
#默认是1
plt.rcParams['font.family'] = 'SimHei'
Label = ["看电影","睡觉","吃饭","打游戏","刷微博","刷小视频","其他"]
Frac = [5,40,5,10,20,10,10]
plt.pie(x=Frac,labels=Label)
plt.title(u"当代大学生每天花费时间比例图")
plt.show()


#为饼状图添加更多样式
#1.想突出饼状图中的某一块，可以在原来的基础上添加“explode=exp, shadow=True”
#属性来着重突出某一块
Label = ["看电影","睡觉","吃饭","打游戏","刷微博","刷小视频","其他"]
Frac = [5,40,5,10,20,10,10]
exp =[0.01,0.1,0.01,0.02,0.05,0.02,0.02]
plt.pie(x=Frac,labels=Label,explode=exp,shadow=True)
plt.title(u"当代大学生每天花费时间比例图")
plt.show()

#2.想将数据直接显示在饼状图之中，可以在原来的基础上添加“autopct="%0.2f%%"”属性
Label = ["看电影","睡觉","吃饭","打游戏","刷微博","刷小视频","其他"]
Frac = [5,40,5,10,20,10,10]
exp =[0.01,0.1,0.01,0.02,0.05,0.02,0.02]
plt.pie(x=Frac,labels=Label,explode=exp,shadow=True,autopct="%0.2f%%")
plt.title(u"当代大学生每天花费时间比例图")
plt.show()
