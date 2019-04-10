import matplotlib.pyplot as plt
import numpy as np
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





