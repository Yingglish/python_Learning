import random

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 

x = range(0,30)
y = [random.randint(100,200) for i in range(30)]

plt.barh(x,y,height=0.3,color='orange')

_ytick_label = ["3月{}日".format(i) for i in range(1,31)]
plt.yticks(x , _ytick_label)

plt.show()
