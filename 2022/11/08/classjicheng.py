class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def say_age(self):
    print(self.name, '有', self.age, '岁')
  def say_name(self):
    return self.name

class Student(Person):
  def __init__(self, name, age, score):
    self.score = score
    Person.__init__(self, name, age)
  def say_score(self):
    print(self.name, '的成绩是', self.score)
  def say_name(self):
    return "学生的名字是：" + super().say_name()

s1 = Student('张三', 18, 100)
s1.say_age()
s1.say_score()
print(s1.say_name())

