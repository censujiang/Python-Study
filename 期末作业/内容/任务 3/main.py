import csv
import sqlite3
from functools import reduce
from operator import attrgetter

# 连接到SQLite3数据库
conn = sqlite3.connect('students.db')

# 创建表
with conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students_1_2 (
            id INTEGER PRIMARY KEY,
            name TEXT,
            regular_grade REAL,
            final_grade REAL,
            total_grade REAL
        )
    """)

# 读取1-2班成绩表.csv文件
with open('1-2班成绩表.csv', 'r', encoding='utf-8') as f:
    # 忽略第一行（列名）
    next(f)
    reader = csv.reader(f)
    # 遍历每一行（学生）
    for row in reader:
        # 解析成绩信息
        id, name, regular_grade, final_grade, total_grade = row
        # 将成绩信息插入表中
        with conn:
            conn.execute("""
                INSERT INTO students_1_2 VALUES (
                    :id, :name, :regular_grade, :final_grade, :total_grade
                )
            """, {
                'id': int(id),
                'name': name,
                'regular_grade': float(regular_grade),
                'final_grade': float(final_grade),
                'total_grade': float(total_grade)
            })

# 创建表
with conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students_3_4 (
            id INTEGER PRIMARY KEY,
            name TEXT,
            regular_grade REAL,
            final_grade REAL,
            total_grade REAL
        )
    """)

# 读取3-4班成绩表.csv文件
with open('3-4班成绩表.csv', 'r', encoding='utf-8') as f:
    # 忽略第一行（列名）
    next(f)
    reader = csv.reader(f)
    # 遍历每一行（学生）
    for row in reader:
        # 解析成绩信息
        id, name, regular_grade, final_grade, total_grade = row
        # 将成绩信息插入表中
        with conn:
            conn.execute("""
                INSERT INTO students_3_4 VALUES (
                    :id, :name, :regular_grade, :final_grade, :total_grade
                )
            """, {
                'id': int(id),
                'name': name,
                'regular_grade': float(regular_grade),
                'final_grade': float(final_grade),
                'total_grade': float(total_grade)
            })

# 从两张表中读取数据并合并存储为Python数组
students = []
with conn:
    for row in conn.execute("""
        SELECT * FROM students_1_2
        UNION
        SELECT * FROM students_3_4
    """):
        students.append(row)

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