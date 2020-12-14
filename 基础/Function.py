# 函数的定义
def describe_pet(animal_type , pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type +"'s name is " + pet_name.title() + ".")
# 调用
describe_pet('hamster' , 'harry')

# 通过关键字实参调用
describe_pet(pet_name='tom', animal_type='cat') 

# 传递任意数量的实参 
# 形参*topping 会让python创建一个名为topping的元祖,并将接收的所有值传入这个元组中
def make_pizza(*topping):
    """打印顾客点的所有配料"""
    print(topping)

make_pizza('pepperoni') # output ('pepperoni',)
make_pizza('mushrooms', 'green pepper', 'extra cheese') # output : ('mushrooms', 'green pepper', 'extra cheese')

# 传递任意数量的关键字形参
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', localction = 'princeton', field = 'physics')
print(user_profile) # output: {'first_name': 'albert', 'last_name': 'einstein', 'localction': 'princeton', 'field': 'physics'}

# 输出一个函数
def output(name="hi"):
    return name

print(output()) # output: hi

# 将函数赋值给一个变量
greet = output
# 运行
print(greet()) # output: hi

# 删除 output 函数
del output
print(greet()) # output: hi
print(output()) # output NameError: name 'output' is not defined
