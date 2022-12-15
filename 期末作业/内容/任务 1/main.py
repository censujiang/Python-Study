import csv
from random import randint

# 计算总成绩
def calculate_grade(regular_grade, final_grade):
    return round(regular_grade * 0.4 + final_grade * 0.6, 2)

# 读取csv文件
def read_csv(filename):
    with open(filename, "r", newline="" , encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = []
        # 读取整个文件
        for row in reader:
            data.append(row)
        # 更新同学成绩信息
        for i in range(1, len(data)):
            regular_grade = randint(0, 100)
            final_grade = randint(0, 100)
            grade = calculate_grade(regular_grade, final_grade)
            # 在列表中更新同学成绩信息
            data[i][2] = str(regular_grade)
            data[i][3] = str(final_grade)
            data[i][4] = str(grade)
        # 将整个列表重新写入文件
        write_csv(filename, data)

# 写入csv文件
def write_csv(filename, data):
    with open(filename, "w", newline="" , encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 写入更新后的整个列表
        for row in data:
            writer.writerow(row)

# 两个文件分别这样做一次
read_csv("1-2班成绩表.csv")
read_csv("3-4班成绩表.csv")
