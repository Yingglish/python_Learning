# python将所有的文本都解读为字符串


# with open('pi_digits.txt') as file_object:
#     contents = file_object.read() # read()读取到文件末尾时返回一个空字符串
#     print(contents.rstrip()) # 删除末尾的字符串
#     print(contents) 

# file_object.close()
# 函数open()返回一个文件对象 如果该文件无法被打开,会抛出 OSError
# read()方法用于从文件读取指定的字节数,如果未给定或为负则读取所有

#逐行读取
# with open('pi_digits.txt') as file_object_2:
#     for line in file_object_2:
#         print(line.rstrip())

#使用关键字 with 时，open返回的文件对象只能在with代码块内有效
