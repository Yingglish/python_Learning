# 键(key)不可变,所以可以用数字、字符串或元组充当,列表不可以 ,值可为任意数值类型

dict = {'a':1,'b':2} #创建
print(dict['a']) #访问
dict['a'] = 3 #修改
print(dict['a'])
dict['c'] = 3 #增添
print(dict)
del dict['c'] # 删除键未 'c'的条目
print(dict)
dict.clear() # 清空所有条目
print(dict) # output : {}

# 关于字典的操作
dict = {'a':1,'b':2,'c':3}
print(dict.items()) #以列表 返回可遍历的(键, 值) 元组数组 output: dict_items([('a', 1), ('b', 2), ('c', 3)])
print(dict.keys()) #以列表返回一个字典所有的键 output : dict_keys(['a', 'b', 'c'])
print(dict.values()) #以列表返回字典中的所有值
#遍历
for key,value in dict.items():
    print('\nKey :' + str(key) + '\nValue :' + str(value))

# 判断键(key) 是否存在
print('a' in dict) # output: True
print('c' not in dict) # output: False

# dict.get(key, default=None) key -- 字典中要查找的键 default -- 如果指定键的值不存在时，返回该默认值值
dict.get('a') # 1
dict.get('d') # 无输出
dict.get('d','nnnnnn') # 'nnnnnn'
 