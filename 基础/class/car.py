class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 给属性指定默认值

    def get_descriptive_name(self):
        """获取汽车信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, milegae):
        if milegae >= self.odometer_reading:
            self.odometer_reading = milegae
        else:
            print("不能回调里程")
    
my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())
my_car.read_odometer()

# 修改属性的值
my_car.odometer_reading = 100 #直接修改
my_car.read_odometer()
my_car.update_odometer(0) #通过方法修改
my_car.read_odometer()
