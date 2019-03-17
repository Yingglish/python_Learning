# 父类(superclass)
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, milegae):
        if milegae >= self.odometer_reading:
            self.odometer_reading = milegae
        else:
            print("不能回调里程")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        pass


class Battery():
    """电瓶类"""
    def __init__(self, battery_size=70):
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

# 子类 类的继承必须写在同一文件中
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """先初始化父类的属性"""
        super().__init__(make, model, year) #通过super()调用父类的方法
        """再初始化子类属性"""
        self.battery= Battery() #将实例用作属性

    def whistle(self):
        """给子类定义方法"""
        print("di di di")

    def fill_gas_tank(self): 
        """对父类方法进行重写"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s' , 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank() #子类实例将调用重写后的方法
my_tesla.whistle()
my_tesla.battery.get_range()
