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
plt.xlabel("age")
plt.ylabel("height:CM")
plt.title("age-height")
# 展示图形
plt.show()


