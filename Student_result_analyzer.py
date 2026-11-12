# Student Result Analyzer
# Created by Sudarshan Kushwaha

print("=" * 40)
print("       STUDENT RESULT ANALYZER")
print("=" * 40)

name = input("Enter Student Name: ")

subjects = ["Python", "Maths", "English", "Science", "Computer"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter {subject} Marks (out of 100): "))

    if mark < 0 or mark > 100:
        print("Invalid Marks!")
        exit()

    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("\n------ RESULT CARD ------")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if min(marks) < 33:
    grade = "F"
    result = "FAIL"
elif percentage >= 90:
    grade = "A+"
    result = "PASS"
elif percentage >= 75:
    grade = "A"
    result = "PASS"
elif percentage >= 60:
    grade = "B"
    result = "PASS"
elif percentage >= 45:
    grade = "C"
    result = "PASS"
else:
    grade = "D"
    result = "PASS"

print("Grade:", grade)
print("Final Result:", result)

print("=" * 40)
print("Developed by Sudarshan Kushwaha")