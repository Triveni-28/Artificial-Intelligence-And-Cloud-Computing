""" Assignment of 19th Feb """

students = {
    "Asha": 85,
    "Ravi": 92,
    "Neha": 78,
    "Kiran": 88,
    "Divya": 95
}

total = 0
topper = ""
highest = 0

for name, marks in students.items():
    total = total + marks
    if marks > highest:
        highest = marks
        topper = name

average = total / len(students)

print("Topper:", topper, "-", highest)
print("Class Average:", average)

print("\nGrades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    print(name, ":", marks, "-", grade)