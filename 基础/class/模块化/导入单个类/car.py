"""一个可用于表示汽车的类"""

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
