"""相当于java中的注解"""
def hello(func):
    def wrapper():
        print("hello,%s"%func.__name__)
        func()
        print("goodby,%s"%func.__name__)
    return wrapper

@hello
def foo():
    print("i am foo")

foo()
