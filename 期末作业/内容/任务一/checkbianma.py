import chardet

with open("1-2班成绩表.csv", "rb") as file:
    content = file.read()
    result = chardet.detect(content)
    print(result)