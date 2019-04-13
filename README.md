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

## 二、折线图（linechart）
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

![image](https://github.com/Gaoshiguo/matplotlib-learning/blob/master/image/myplot1.png)

![image](https://github.com/Gaoshiguo/matplotlib-learning/blob/master/image/myplot2.png)

![image](https://github.com/Gaoshiguo/matplotlib-learning/blob/master/image/myplot3.png)

![image](https://github.com/Gaoshiguo/matplotlib-learning/blob/master/image/myplot4.png)

## 三、条形图（bar）
#条形图也叫直方图，在matplotlib中需要调用plt.bar（）函数，bar(x, height, width=0.8, bottom=None, ***, align='center', data=None, **kwargs)
#以上是bar()函数中各参数的定义，官方文档中对其说明是：
#x

#x坐标

#int,float

#height

#条形的高度

#int,float

#width

#宽度

#0~1，默认0.8

#botton

#条形的起始位置

#也是y轴的起始坐标

#align

#条形的中心位置

#“center”,"lege"边缘

#color

#条形的颜色

#“r","b","g","#123465"，默认“b"

#edgecolor

#边框的颜色

#同上

#linewidth

#边框的宽度

#像素，默认无，int

#tick_label

#下标的标签

#可以是元组类型的字符组合

#log

#y轴使用科学计算法表示

#bool

#orientation

#是竖直条还是水平条

#竖直："vertical"，水平条："horizontal"

#闲话少数，show the code

```
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 将全局的字体设置为黑体
matplotlib.rcParams['font.family'] = 'SimHei'

# 数据
x = [12,14,16,18,20,22]
y = [100, 140, 170, 175, 178, 176]


# 绘图 x x轴， height 高度, 默认：color="red", width=0.8
p1 = plt.bar(x, height=y, width=0.5,color= "red", edgecolor = "black", log = False)
plt.xlabel("age")#设置x轴标签
plt.ylabel("height:CM")#设置y轴标签
plt.title("age-height")#设置图表标题
# 展示图形
plt.show()

```
生成的图片效果如下图所示：

![image](https://github.com/Gaoshiguo/matplotlib-learning/blob/master/image/myplot-bar.png)

## 四、饼状图（pie）
**饼状图，绘制饼状图，需要使用plot.pie()函数，说明文档中各参数的属性取值及其所代表的意思是：
`#x
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
`

我们先来展示一个最简单的饼状图，代码如下：

```
plt.rcParams['font.family'] = 'SimHei'
Label = ["看电影","睡觉","吃饭","打游戏","刷微博","刷小视频","其他"]
Frac = [5,40,5,10,20,10,10]
plt.pie(x=Frac,labels=Label)
plt.title(u"当代大学生每天花费时间比例图")
plt.show()
```

图片展示如下：






