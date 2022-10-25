class Student:
    school = "重电"
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def say_score(self):
        print(f"{self.name}的学校是{Student.school},成绩是{self.score}")
stu1 = Student("张三", 90)
stu1.say_score()
stu2 = Student("李四", 80)
stu2.say_score()
print("查看类的文档字符串:", Student.__doc__)
print("查看类的名称:", Student.__name__)
print("查看类的模块:", Student.__module__)
print("查看类的基类:", Student.__bases__)
print("查看类的字典:", Student.__dict__)
print("查看类的所有属性:", dir(Student))
print("访问对象stu1的属性和方法:", stu1.school)
print("访问对象stu1的属性和方法:", stu1.name)
print("访问对象stu1的属性和方法:", stu1.score)
print("访问对象stu1的属性和方法:", stu1.say_score())
print("访问对象stu1的属性和方法:", stu1.__dict__)
print("访问对象stu1的属性和方法:", dir(stu1))