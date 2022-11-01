class Fish:
    legs =0
    @classmethod
    def swim(cls):
        print("鱼会游泳")
        print("鱼有%d条腿"%cls.legs)
        print("鱼有%d条腿"%Fish.legs)
      
    def __init__(self,classification='淡水鱼'):
        self.classification=classification
        print("鱼是%s"%self.classification)
        print("鱼有%d条腿"%self.legs)
        print("鱼有%d条腿"%Fish.legs)
    def isinsea(self):
        if self.classification=='淡水鱼':
            return False
        else:
            return True
Fish.swim()
print('=====================')
fish=Fish()
print(fish.legs)
fish.swim()
print(fish.isinsea())
print('=====================')
fish1=Fish('海水鱼')
print(fish1.legs)
fish1.swim()
print(fish1.isinsea())
print('=====================')
# 静态方法例子
class arithmetic:
    @staticmethod
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
print("10+5=",arithmetic.add(10,5))
print("10-5=",arithmetic.sub(10,5))
