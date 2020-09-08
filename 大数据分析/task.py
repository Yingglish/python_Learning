import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    """
    与非门
    """
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    """
    或门
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    return AND(NAND(x1,x2),OR(x1,x2))

if __name__ == '__main__':
    print("异或门测试")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y1 = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y1))

# if __name__ == '__main__':
#     print("与非门测试")
#     for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
#         y1 = NAND(xs[0], xs[1])
#         print(str(xs) + " -> " + str(y1))
#     print("\n或门测试")
#     for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:  
#         y2 = OR(xs[0], xs[1])
#         print(str(xs) + " -> " + str(y2))
"""
    output:

        与非门测试
        (0, 0) -> 1
        (1, 0) -> 1
        (0, 1) -> 1
        (1, 1) -> 0

        或门测试
        (0, 0) -> 0
        (1, 0) -> 1
        (0, 1) -> 1
        (1, 1) -> 1
"""
