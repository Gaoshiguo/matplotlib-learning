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
## 一、散点图（）
