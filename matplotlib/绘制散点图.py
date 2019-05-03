import random

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
x1 = range(0,20)
x2 = range(34,54)
y1 = [random.randint(20,35) for i in range(20)]
y2 = [random.randint(11,35) for i in range(20)]

plt.scatter(x1, y1, label = "三月份")
plt.scatter(x2, y2, label="十月份")

# 调整x轴的刻度
_x = list(x1) + list(x2)
print(_x[::4])
_xtick_label = ["3月{}日".format(i + 1) for i in x1]
_xtick_label += ["5月{}日".format(i- 33) for i in x2]
plt.xticks(_x[::4],_xtick_label[::4],rotation = 45)

# 添加描述信息
plt.xlabel('时间')
plt.ylabel('工资')
plt.title('标题')
#添加图例
plt.legend()

plt.show()
