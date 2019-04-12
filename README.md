# matplotlib-learning
这个项目用于展示日常的Python中matplotlib的学习
## matplotlib日常学习代码笔记以及注释
#### matplotlib是一个基于Python的非常强大的数据图像展示模块，在我们的科学实验结果分析、数据展示等方面有着非常强大的能力，可以画各种图形，基本可以取代matlib的功能，接下来我们来一步一步由易到难的学习这个强大的库
## matplotlib的初次练习
```
import matplotlib.pyplot as plt
import numpy as np
#在x轴上，-1~1范围内分布50个点
x = np.linspace(-1,1,50)
y = x**2
#创建画布
plt.plot(x,y)
#展示画布
plt.show()

```
图片展示如下：

![image](https://github.com/Gaoshiguo/matplotlib-learning/blob/master/image/1.png)

*接下来，我们依次来展示matplotlib中可支持的各种图形
## 一、散点图（scatter）
散点图需要调用matplotlib中的函数`plt.scatter()`,其中可传入的参数有x,y,s,c,marker,alpha这几个参数
#其中：x,y代标x轴和y轴的数据，s 代标点的面积，c代标点的颜色，marker代标点的形状，alpha代表透明度
代码如下：

```
height = [161, 170, 182, 175, 173, 165]
weight = [50, 58, 80, 70, 69, 55]

# 散点图,marker可取的值有：“.”代标点，“，”代表像素，“o”代表圆，等等
plt.scatter(height, weight,s=150,color='blue',marker='.')
plt.ylabel("height")#代表x坐标轴的名字
plt.xlabel("weight")#代表y坐标轴的名字

# 展示图表
plt.show()

N=100
x_1=np.random.random(N)
y_1=x_1+np.random.random(N)*0.5#显示正相关数据属性的图像
plt.scatter(x_1,y_1,s=100,color="black",marker="o")
plt.show()
```
分别生成的两个图像为：

![image](https://github.com/Gaoshiguo/matplotlib-learning/blob/master/image/2.png)

## 一、折线图（linechart）
折线图只要简单的使用plot（）函数就可以，需要说明的是当缺少x时，系统会默认从0开始以Y的长度来填充，当缺少y时，系统会默认以x作为y轴
#折线图中的一些参数取值说明：
#对折线颜色的控制
#'b'	blue
#'g'	green
#'r'	red
#'c'	cyan 青色
#'m'	magenta平红
#'y'	yellow
#'k'	black
#'w'	white
#对折现类型的控制
#'-o'	实线
#'--o'	虚线
#'-.o'	虚点线
#':o'	点线
#' '	空类型，不显示线

```
x_1=[1,2,3,4,5,6,7,8]
y_1=[25,15,45,56,45,78,88,98]
y_2=[23,13,43,54,42,74,85,95]
y_3=[21,11,41,51,40,71,81,92]
y_4=[18,9,39,51,39,70,82,91]
#当缺少x时，系统会默认从0开始以Y的长度来填充
#当缺少y时，系统会默认以x作为y轴
#折线图中的一些参数取值说明：
#对折线颜色的控制
#'b'	blue
#'g'	green
#'r'	red
#'c'	cyan 青色
#'m'	magenta平红
#'y'	yellow
#'k'	black
#'w'	white
#对折现类型的控制
#'-o'	实线
#'--o'	虚线
#'-.o'	虚点线
#':o'	点线
#' '	空类型，不显示线
plt.figure()
plt.plot(y_1)
plt.show()

plt.figure()
plt.plot(x_1)
plt.show()

plt.figure()
plt.plot(x_1,y_1)
plt.show()

plt.figure()
plt.plot(x_1,y_1,":o",color="red")
plt.show()

plt.figure()
plt.plot(x_1,y_1,":o",color="red")#点线
plt.plot(x_1,y_2,"-o",color="blue")#实线
plt.plot(x_1,y_3,"--o",color="black")#虚线
plt.plot(x_1,y_4,"-.o",color="green")#虚点线
plt.show()
```

生成的个图片展示如下：

![image](https://github.com/Gaoshiguo/matplotlib-learning/blob/master/image/myplot.png)

