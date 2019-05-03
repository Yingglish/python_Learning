import random

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 

x = range(0,10)
y = [random.randint(100,200) for i in range(10)]

plt.bar(x,y,width=0.4)

_xtick_label = ["3月{}日".format(i) for i in range(1,11)]
plt.xticks(x , _xtick_label)

plt.show()
