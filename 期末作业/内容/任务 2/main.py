import csv
from functools import reduce
from operator import attrgetter

# 读取csv文件
def read_csv(filename):
    with open(filename, "r", newline="" , encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        students = []
        # 跳过第一行
        next(reader)
        for row in reader:
            # 将成绩内容转换为整数或浮点数
            regular_grade = int(row[2])
            final_grade = int(row[3])
            grade = float(row[4])
            student = {
                "id": row[0],
                "name": row[1],
                "regular_grade": regular_grade,
                "final_grade": final_grade,
                "grade": grade
            }
            students.append(student)
        return students

# 合并两个文件中的学生信息
students1 = read_csv("1-2班成绩表.csv")
students2 = read_csv("3-4班成绩表.csv")
students = students1 + students2

# 获取平时成绩最好的学生信息
best_regular_grade_student = max(students, key=lambda x: x["regular_grade"])
print("平时成绩最好的学生:", best_regular_grade_student)
# 获取期末成绩最好的学生信息
best_final_grade_student = max(students, key=lambda x: x["final_grade"])
print("期末成绩最好的学生:", best_final_grade_student)
# 获取总成绩最好的学生信息
best_grade_student = max(students, key=lambda x: x["grade"])
print("总成绩最好的学生:", best_grade_student)
# 将学生根据总成绩进行排序
sorted_students = sorted(students, key=lambda x: x["grade"])
print("按照总成绩排序后的学生:", sorted_students)
# 获取总成绩的平均值
average_grade = reduce(lambda x, y: x + y, map(lambda x: x["grade"], students)) / len(students)
print("总成绩的平均值:", average_grade)
