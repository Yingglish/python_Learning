name = 'ada lovelace'
print(name.title()) # 将字符串首字母大写
print(name.upper()) # 将所有字符床改为大写
print(name.lower()) 

str1 = ' spun  '
print(str1.rstrip()) #暂时删除字符串尾部空白
print(str1.lstrip()) #暂时删除字符串首部空白
print(str1.strip()) #暂时删除字符串首尾空白

#使用str()将非字符串转换为字符串
str2 = 12
print ('my age is ' + str(str2))

# 关于列表的操作

colors = ['red' , 'orange' , 'blue']
colors.append('black') #向列表末尾添加元素
colors.insert(0,'green') #在第一个位置插入元素
del colors[0] #使用del语句删除第一个元素
print(colors.pop()) #使用pop弹出一个元素，默认为最后一个
colors.remove('red') #根据值删除元素
print(colors)

colors.append('red')
colors.append('green')

colors.sort() # 使用sort()函数跟据字母顺序进行排序(永久改变) sorted()函数为暂时性排序
print(colors)
colors.sort(reverse=True)
print(colors)
print(colors.reverse()) #使用reverse()反转列表
print(len(colors)) #获取列表长度

#列表遍历
for color in colors:
    print(color + '\n')

#创建数值列表
# range()返回的是一个可迭代对象，并不是列表
for value in range(1,5):
    print(value)
print(range(1,5)) # output : range(1,5)
#使用list()将此对象转换为列表
print(list(range(1,5)))
print(list(range(1,5)[::2])) # [1, 3]

# 列表解析
squares = [value**2 for value in range(1,11)]
print(squares)

#切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3]) # 输出前三个元素 ['charles','martina','michael']
print(players[:2]) # 未指定起始索引,默认重首开始
print(players[3:]) # 未指定终止索引,则到列表末尾终止
print(players[::2]) # 间隔取值 每隔2取一次 ['charles', 'michael', 'eli']


#遍历切片
for player in players[-3:]:
    print(player + ' ')

# 列表的复制
people = players[:] #利用切片复制整个列表
temp = players # temp和 players 指向同一列表

#replace()方法
message = ' I like cat'
message.replace('cat','dog') #  ' I like dog'
