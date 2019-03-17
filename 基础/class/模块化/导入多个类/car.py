"""用于表示燃油汽车和电动汽车的类"""

class Car():
    """汽车类"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """打印出汽车行驶的里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, milegae):
        """设置里程,禁止里程回调"""
        if milegae >= self.odometer_reading:
            self.odometer_reading = milegae
        else:
            print("不能回调里程")    
    
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

class Battery():
    """电瓶类"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery")

    def get_range(self):
        """显出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 230
        elif self.battery_size == 85:
            range == 270

        message = "This car can go approximately " + str(range) + "miles on a full charge."
        print(message)

class ElectricCar(Car):
    """电瓶车类"""
    def __init__(self, make, model, year):
        """先初始化父类的属性"""
        super().__init__(make, model, year) #通过super()调用父类的方法
        """再初始化子类属性"""
        self.battery= Battery() #将实例用作属性
