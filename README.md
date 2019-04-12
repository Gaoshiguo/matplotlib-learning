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

