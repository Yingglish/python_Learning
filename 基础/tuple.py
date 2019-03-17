# 元祖与列表相似,但元祖中的的元素不可修改

tuple_1 = (10 , 20 , 30)
print(tuple_1[1])
for value in tuple_1:
    print(value)

tuple_2 = () #创建空元组
tuple_3 = (2,) #只有一个元素是需要在元素后 + ','
