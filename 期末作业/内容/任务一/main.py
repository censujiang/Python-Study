import csv
from random import randint

# 计算总成绩
def calculate_grade(regular_grade, final_grade):
    return round(regular_grade * 0.4 + final_grade * 0.6, 2)

# 读取csv文件
def read_csv(filename):
    with open(filename, "r", newline="" , encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        # 跳过第一行
        next(reader)
        for row in reader:
            regular_grade = randint(0, 100)
            final_grade = randint(0, 100)
            grade = calculate_grade(regular_grade, final_grade)
            # 将同学信息写入文件
            write_csv(filename, row[0], row[1], regular_grade, final_grade, grade)

# 写入csv文件
def write_csv(filename, student_id, name, regular_grade, final_grade, grade):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # 注意需要将整数，浮点数转换为字符串再写入
        writer.writerow([student_id, name, str(regular_grade), str(final_grade), str(grade)])

# 两个文件分别这样做一次
read_csv("1-2班成绩表.csv")
read_csv("3-4班成绩表.csv")
