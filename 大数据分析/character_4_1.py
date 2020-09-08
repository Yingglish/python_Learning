import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# x0 = np.arange(-2,2.5,0.25)
# x1 = np.arange(-2,2.5,0.25)
# X, Y = np.meshgrid(x0,x1) # 把两个数组的笛卡尔积内的元素的第一二个坐标分别放入两个矩阵中
# Z = np.array(X ** 3 + Y **3)

# # 绘制x^3 + y^3 3维图像
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot_surface(X,Y,Z,alpha=0.5,cmap="winter")
# ax.set_xlabel('x0')
# ax.set_ylabel('x1')
# ax.set_zlabel("z")
# ax.set_title('函数图形')
# plt.show()

# 绘制梯度分析走向
def _numerical_gradient_no_batch(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)  # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val  
        
    return grad


def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        print(111)
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        return grad

def function_2(x):
    if x.ndim == 1:
        # print(x.ndim)
        return np.sum(x**3)
    else:
        # print(x.ndim)
        return np.sum(x**3, axis=1)


def tangent_line(f, x):
    d = numerical_gradient(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

x0 = np.arange(-2, 2.5, 0.25)
x1 = np.arange(-2, 2.5, 0.25)
X, Y = np.meshgrid(x0, x1)
    
X = X.flatten()
Y = Y.flatten()

grad = numerical_gradient(function_2, np.array([X, Y]))

plt.figure()
plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666")
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('x0')
plt.ylabel('x1')
plt.grid()
plt.draw()
plt.show()
