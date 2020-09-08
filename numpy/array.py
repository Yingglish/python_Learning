import numpy as np

a1 = np.array([ 1 , 2 ,3]) # 一维数组
a2 = np.array([[1,2,3],[4,5,6]]) # 二维
a3 = np.array([range(i,i+3) for i in [1,2,3]])

# 创建3x5的全0矩阵
myZero = np.zeros([3, 5])
# 创建3x5的全1矩阵
myOnes = np.ones([3, 5])
# 3x3的单位矩阵
myEye = np.eye(3)

print(np.sum(myEye))#矩阵所有元素求和

print(a1)
print(a2)
print(a3)
print(type(a1))
print(a3.shape) # 返回一个代表n*m矩阵的大小的元组(n,m)
