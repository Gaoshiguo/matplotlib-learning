import matplotlib.pyplot as plt
import numpy as np
#散点图函数中各参数的含义
#plt.scatter(x, y, s, c ,marker, alpha)。在散点图函数中应当有x,y,s,c,marker,alpha这几个参数
#其中：x,y代标x轴和y轴的数据，s 代标点的面积，c代标点的颜色，marker代标点的形状，alpha代表透明度
# 身高与体重的数据
height = [161, 170, 182, 175, 173, 165]
weight = [50, 58, 80, 70, 69, 55]

# 散点图,marker可取的值有：“.”代标点，“，”代表像素，“o”代表圆，等等
plt.scatter(height, weight,s=150,color='blue',marker='.')
plt.ylabel("height")#代表x坐标轴的名字
plt.xlabel("weight")#代表y坐标轴的名字

# 展示图表
plt.show()

N=100
x= np.random.random(N)
y= -x+np.random.random(N)*0.5
plt.scatter(x,y,s=100,color="red",marker="o")
plt.show()

x_1=np.random.random(N)
y_1=x_1+np.random.random(N)*0.5
plt.scatter(x_1,y_1,s=100,color="black",marker="o")
plt.show()

