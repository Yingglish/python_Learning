import numpy as np
import matplotlib.pylab as plt
from gradient_2d import numerical_gradient
from mpl_toolkits.mplot3d import Axes3D

# 新增
def f(x,y):
    return x**2 + y**2

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_history = []

    for i in range(step_num):
        x_history.append( x.copy() )

        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, np.array(x_history)


def function_2(x):
    # return x[0]**2 + x[1]**2
    return np.sum(x**2)

init_x = np.array([-3.0, 4.0])
# x = np.linspace(-3,3,30)
# y = np.linspace(-3,3,30)
# X, Y = np.meshgrid(x, y)
# Z = f(X,Y) 

fig = plt.figure()
ax = Axes3D(fig)
#ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none') #曲面图
#ax.plot_wireframe(X, Y, Z, color='c') #线框图
# ax.contour3D(X, Y, Z, 50, cmap='binary')#等高线图



lr = 0.1
step_num = 20
x, x_history = gradient_descent(function_2, init_x, lr=lr, step_num=step_num)
ax.scatter3D(x_history[:,1],x_history[:,0], np.array(x_history[:,0]**2 + x_history[:,1]**2), c='r',marker = 'o')
# plt.plot( [-5, 5], [0,0], '--b')
# plt.plot( [0,0], [-5, 5], '--b')
# plt.plot(x_history[:,0], x_history[:,1], 'o')
# z = np.array(x_history[:,0]**2 + x_history[:,1]**2)

plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 4.5)
plt.xlabel("X0")
plt.ylabel("X1")
plt.show()
