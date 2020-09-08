import numpy as np
from matplotlib import pyplot as plt
# from matplotlib.image import imread

# array = np.array([
#     [51,55],
#     [14,19],
#     [0,4]
# ])

# y = array.flatten()
# print(y)
# print(type(y))

# print(y[y > 12])

# plt.plot(np.arange(0,6,0.1),np.sin(np.arange(0,6,0.1)), )
# plt.show()

# # 读取图片

# x = np.arange(0,6,0.1)
# y = np.sin(x)
# z = np.cos(x)

# plt.plot(x,y,label='$\\sin$',color='blue')
# plt.plot(x,z,'r--',label='$\\cos$')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('sin & cos')
# # plt.ylim(0,1)
# # plt.xlim(0,6)
# plt.legend(loc='best')
# plt.show()

# axis----为0代表列方向，为1代表行方向

a = np.array([[2,4,6,1],[1,5,2,9]])
print(a)
np.argmax(a) # 返回array中数值最大数的下标，默认将输入array视作一维，出现相同的最大，返回第一次出现的
np.argmax(a, axis=0)    # 返回列方向上数值最大值下标，2>1, 4<5, 6>2, 1<9所以结果为0, 1, 0, 1
np.argmax(a, axis=1)     # 返回行方向上数值最大值下标，同理axis = 0情况 [2, 3]
