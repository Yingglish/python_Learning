import random

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 

x1 = range(0,4)
x2 = [ i + 0.2 for i in x1]
x3 = [ i + 0.2 * 2 for i in x1]
y1 = [random.randint(100,200) for i in range(4)]
y2 = [random.randint(12,20) for i in range(4)]
y3 = [random.randint(10,50) for i in range(4)]

plt.bar(x1,y1,width=0.2,label='3月1日')
plt.bar(x2,y2,width=0.2,label='3月2日')
plt.bar(x3,y3,width=0.2,label='3月3日')
# _xtick_label = ["3月{}日".format(i) for i in range(1,11)]
# plt.xticks(x , _xtick_label)

# 设置图例
plt.legend()

plt.show()
