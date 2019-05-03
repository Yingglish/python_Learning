import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# 设置图片大小,dpi参数为像素点
fig = plt.figure(figsize=(20,8), dpi =80)

# 生成一个包含 50 个元素的数组，这 50 个元素均匀的分布在 [0, 2pi] 的区间上
x = np.linspace(0, 2 * np.pi, 50) 

#绘图
plt.plot(x,np.sin(x),'r-',label = "sinx")
#plt.plot(x, np.sin(x),color="r" ,linestyle='-',label="sinx",linewidth=5,alpha=0.5)
plt.plot(x,np.cos(x),'b--',label="cosx") 

#设置x,y轴间距
plt.xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi])
plt.yticks([i/2 for i in range(-2,3)])

# 绘制网格
plt.grid(alpha=0.4) # alpha透明度

# 添加图例
plt.legend(loc="upper right") # 显示在右上角 左下-- lower left 中间-- center

# 存储到当前目录下
# plt.savefig('./first.svg') 
plt.show() # 展示
plt.close()
