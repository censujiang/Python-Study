class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def __repr__(self):
        return f"{self.name} 是一只 {self.breed}"
    def bark(self):
        print(f"{self.name} 在叫")
# 静态设置属性
dog1 = Dog("旺财","哈士奇")
dog2 = Dog("小黑","拉布拉多")
print(dog1)
print(dog2)
dog1.name = "大黄"
dog2.breed = "金毛"
print(dog1)
dog1.bark()
dog2.bark()
# 动态设置属性
dog1.color = "黄色"
print(dog1.color)
# 其他操作
print(dir(dog1))
print(dog1.__dict__)
print(dog1.__class__)
print("dog1是否是Dog类的实例:",isinstance(dog1,Dog))