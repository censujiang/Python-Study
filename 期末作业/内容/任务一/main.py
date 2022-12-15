# 首先导入需要的库
import random
import csv

# 打开文件并读取内容
with open("1-2班成绩表.csv" ,encoding='gb18030') as file:
    reader = csv.reader(file)
    # 读取所有行
    rows = list(reader)

# 遍历每一行，为每个学生提供平时成绩和期末成绩
for row in rows:
    # 取出学号和姓名
    student_id = row[0]
    name = row[1]

    # 使用randint函数生成平时成绩和期末成绩
    midterm_grade = random.randint(0, 100)
    final_grade = random.randint(0, 100)

    # 计算总成绩
    total_grade = round(midterm_grade * 0.4 + final_grade * 0.6, 2)

    # 将学生成绩信息添加到行中
    row.append(midterm_grade)
    row.append(final_grade)
    row.append(total_grade)

# 写入文件
with open("1-2班成绩表.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
