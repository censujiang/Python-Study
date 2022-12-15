import csv
import sqlite3

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
def get_best_quiz_grade(students):
  best_quiz_grade = 0
  est_quiz_grade_student = None
  
  for student in students:
    index, name, quiz_grade, exam_grade, total_grade = student
    if quiz_grade > best_quiz_grade:
      best_quiz_grade = quiz_grade
      est_quiz_grade_student = student

  return est_quiz_grade_student
est_quiz_grade_student = get_best_quiz_grade(students)
print("平时成绩最好的学生:",est_quiz_grade_student)
# 获取期末成绩最好的学生信息
def get_best_exam_grade(students):
  best_exam_grade = 0
  best_exam_grade_student = None
  
  for student in students:
    index, name, quiz_grade, exam_grade, total_grade = student
    if exam_grade > best_exam_grade:
      best_exam_grade = exam_grade
      best_exam_grade_student = student

  return best_exam_grade_student
best_exam_grade_student = get_best_exam_grade(students)
print("期末成绩最好的学生:",best_exam_grade_student)
# 获取总成绩最好的学生信息
def get_best_total_grade(students):
  best_total_grade = 0
  best_total_grade_student = None
  
  for student in students:
    index, name, quiz_grade, exam_grade, total_grade = student
    if total_grade > best_total_grade:
      best_total_grade = total_grade
      best_total_grade_student = student

  return best_total_grade_student
best_total_grade_student = get_best_total_grade(students)
print("总成绩最好的学生:",best_total_grade_student)
# 将学生根据总成绩进行排序
def sort_by_total_grade(students):
  return sorted(students, key=lambda student: student[4], reverse=True)
sorted_students = sort_by_total_grade(students)
print("根据总成绩排序后的学生信息:",sorted_students)
# 获取总成绩的平均值
def get_average_total_grade(students):
  total = 0
  for student in students:
    total += student[4]
  return total / len(students)
average_total_grade = get_average_total_grade(students)
print("总成绩的平均值:",average_total_grade)