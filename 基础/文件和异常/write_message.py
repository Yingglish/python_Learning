with open('programming.txt','w') as file_object:
    file_object.write("I love programming")
    print(file_object.writable()) 

# 文件不存在,自动创建 ,文件存在将清空原文件内容进行写入,若要在源文件的内容下继续写入,将mode参数改为`a`,eg: open('fileName', 'a' )
