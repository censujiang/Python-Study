class Car:
    def __del__(self):
        print(f"销毁对象:{self.name}")
    def __init__(self, name):
        self.name = name
        print(f"创建对象:{self.name}")
    
car1 = Car("奔驰")
car2 = Car("宝马")
car3 = Car("奥迪")
del car1
del car3
print("逻辑结束")