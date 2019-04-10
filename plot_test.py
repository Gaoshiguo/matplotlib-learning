import matplotlib.pyplot as plt
import numpy as np
#在x轴上，-1~1范围内分布50个点
x = np.linspace(-1,1,50)
y = x**2
#创建画布
plt.plot(x,y)
#展示画布
plt.show()

