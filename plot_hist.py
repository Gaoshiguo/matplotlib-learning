import matplotlib.pyplot as plt
import numpy as np
#直方图有频率分布直方图、频数分布直方图，反应的主要是数据分布状况的图形，在matplotlib中支持一维和二维的直方图
#分别调用plt.hist(x=x, bins=10) 与plt.hist2D(x=x, y=y)这两个函数，具体使用方法如下

#属性       说明         类型
#x          数据         数值类型
#bins      条形数         int
#color     颜色          "r","g","y","c"
#density 是否以密度的形式显示 bool
#range     x轴的范围    数值元组（起，终）
#bottom    y轴的起始位置   数值类型
#histtype   线条的类型     "bar":方形，"barstacked":柱形,<br />"step":"未填充线条"<br />"stepfilled":"填充线条"
#align      对齐方式       "left":左，"mid":中间，"right":右
#orientation orientation    "horizontal":水平，"vertical":垂直
#log       单位是否以科学计术法 bool

#1.这段代码我们使用一个函数来生成2000个数据，形如y= k*x+b的形式，其中b我们可以将其看作为均值，K为系数，影响因子，也可以理解为方差，
#我们将方差选取为20，代表所生成的数据会在均值100左右以20的方差波动，服从一个正态分布
const = 100#均值
sigma = 20#方差
x= const+sigma*np.random.randn(2000)#生成2000个数据
plt.hist(x=x,bins=10)
plt.show()

#2.同样，我们也可以将频数分布直方图改为频率分布直方图，只需要将Y轴的频数改为频率即可，在hist()
#函数中提供了这样的属性，只需要将density=True，代表以密度显示
const = 100#均值
sigma = 20#方差
x= const+sigma*np.random.randn(2000)#生成2000个数据
plt.hist(x=x,bins=10,density=True)
plt.show()

#3.同样，matplotlib可以实现二维图像展示，只需调用hist2d(),用法与hist基本一致，只是添加了一个y属性
const = 100#均值
sigma = 20#方差
x = const+sigma*np.random.randn(2000)#生成2000个数据
y = const+sigma*np.random.randn(2000)
plt.hist2d(x=x,y=y,bins=10)
plt.show()


