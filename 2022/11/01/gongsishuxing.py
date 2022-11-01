class Employee:
  __company = "腾讯"
  def __init__(self, name, age):
    self.name = name
    self.__age = age
  def info(self):
    print("姓名：", self.name)
    print("年龄：", self.__age)
    print("公司：", Employee.__company)
    self.__work()
  def __work(self):
    print("员工正在工作")
p1 = Employee("张三", 18)
print(p1.name)
# print(p1.__age)
# print(p1.__company)
# p1.__work()
print("=====================================")
p1.info()
print(p1._Employee__age)