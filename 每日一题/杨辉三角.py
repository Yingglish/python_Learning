# print("输入需要打印的杨辉三角行数", end='')
# row = int(input())
# if row < 1:
#     print("输入有误，请重新输入")
# #初始化一个杨辉列表
# yh_arr = [[1],[1,1]]
# if 1<= row < 3:
#     #分片截取
#     yh_arr = yh_arr[:row]
# else:
#     #逐行遍历
#     for i in range(2,row):
#         #获取上一行在列表数据  数组下标从 0 开始
#         temp = yh_arr[i-1]
#         #新定义一个列表
#         arr = [1]
#         #从第二个元素开始添加值
#         for j in range(i-1):
#             #左上 + 右上
#             arr.append(temp[j] + temp[j+1])
#         #最后一个元素补一
#         arr.append(1)
#         yh_arr.append(arr)
# #输出
# [print(i) for i in yh_arr]
print("输入需要打印的杨辉三角行数 :", end='')
row = int(input())
if row < 1:
    print('输入有误，请重新输入')
# 初始化一个杨辉列表，只存储第一行的元素
yh_arr = [[1]]
for i in range(1,row):
    # 在上一行列表后面补 0
    swap = yh_arr[-1]+[0]
    # 初始化一个列表 代表当前行
    arr = [1]
    for j in range(len(swap)-1):
        arr.append(swap[j]+swap[j+1])
    yh_arr.append(arr)

[print(i) for i in yh_arr]
