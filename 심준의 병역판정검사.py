def grade(kg,cm):
    grade = 0
    bmi = kg / ((cm / 100) ** 2)
    if cm < 140.1:
        grade = 6
    elif 140.1 <= cm < 146:
        grade = 5
    elif 146 <= cm < 159:
        grade = 4
    elif 159 <= cm < 161:
        if 16.0 <= bmi < 35.0:
            grade = 3
        elif bmi > 16.0 or bmi <= 35.0:
            grade = 4
    elif 161 <= cm < 204:
        if bmi < 16.0 or bmi >= 35.0:
            grade = 4
        elif 16.0 <= bmi < 18.5 or 30.0 <= bmi < 35.0:
            grade = 3
        elif 18.5 <= bmi < 20.0 or 25.0 <= bmi < 30.0:
            grade = 2
        elif 20.0 <= bmi < 25.0:
            grade = 1
    elif cm >= 204:
        grade = 4
    return grade
for i in range(int(input())):
    cm,kg = map(int, input().split())
    print(grade(kg,cm))