#-*- coding=utf-8 -*-
"""
感知机
    二类分类的线性分类模型，其输入为实例的特征向量，输出为实例的类别
"""
import numpy as np


def step_function(x):
    """
    阶跃函数
    :param x:
    :return:
    """
    if x <= 0:
        return 0
    else:
        return 1


def and_operate(x1, x2):
    """
    与门
    :param x1:
    :param x2:
    :return:
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    return step_function(np.sum(w * x) + b)


def nand_operate(x1, x2):
    """
    与非门
    :param x1:
    :param x2:
    :return:
    """
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    return step_function(np.sum(w * x) + b)


def or_operate(x1, x2):
    """
    或门
    :param x1:
    :param x2:
    :return:
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3
    return step_function(np.sum(w * x) + b)

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))
