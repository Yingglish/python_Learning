import numpy as np
from matplotlib import pyplot as plt
import math

def calc_e_small(x):
    n = 10
    f = np.arange(1,n+1).cumprod()
    #x x^2 ... x^10
    b = np.array([x]*n).cumprod()
    return np.sum(b / f) + 1

'''
e^x = ln2 + (e^ln2)/1!*(x-ln2) + (e^ln2)/2!*(x-ln2)^2+...
x = a*ln2 + b   k<= z  |b| <= 1/2ln2
a = ln( int( x/ln2 + 0.5 ) )
b = x-a*ln2
e^x = 2^a + e^b
'''
def calc_e(x):
    reverse = False
    if x < 0 : # 处理负数
        x = -x
        reverse = True
    ln2 = 0.69314718055994530941723212145818
    c = x / ln2
    a = int(c + 0.5)
    b = x - a*ln2
    # 2的a次方乘以e的b次幂
    y = (2 ** a) * calc_e_small(b)
    if reverse:
        return 1/y
    return y


if __name__ == "__main__":
    np.set_printoptions(suppress=False)
    #-2到0 十个数
    t1 = np.linspace(-2,0,10,endpoint=False)
    t2 = np.linspace(0,4,20)
    t = np.concatenate((t1,t2))
    print(t) # 横轴数据
    y = np.empty_like(t)
    for i,x in enumerate(t):
        y[i] = calc_e(x)
        print("e^",x," = ",y[i],"(近似值)\t", math.exp(x),"(真实值)" )
    plt.figure(facecolor='w')
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签 
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    plt.plot(t,y,'r-',t,y,'go',linewidth=2)
    plt.title("泰勒展开式" ,fontsize=18)
    plt.xlabel('X',fontsize=15)
    plt.ylabel('exp(X)',fontsize=15)
    plt.grid(True,ls=":")
    plt.show()
