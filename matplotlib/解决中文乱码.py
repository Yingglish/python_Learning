from matplotlib import pyplot as plt
from  matplotlib import font_manager
import random

# 第二种方式正常显示中文
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

my_font = font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttc') #解决中文乱码

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

plt.figure(figsize=(10,8),dpi= 80)
plt.plot(x,y)

# 调整x轴间距,添加字符串到x轴
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]

# 取步长,数字和字符串一一对应
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=90 , fontproperties = my_font) #rotation旋转的度数

#添加描述信息
plt.xlabel('时间',fontproperties = my_font)
plt.ylabel('温度 单位(摄氏度)',fontproperties = my_font)
plt.title('10点到12点的气温变化情况',fontproperties = my_font)

plt.show()
