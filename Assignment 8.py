""" Assignment of 28th Feb """

import matplotlib.pyplot as plt

students = ["Asha", "Ravi", "Neha", "Kiran", "Divya"]
marks = [85, 92, 78, 88, 95]

plt.bar(students, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.pie(marks, labels=students, autopct='%1.1f%%')
plt.title("Marks Distribution - Pie Chart")
plt.show()

plt.hist(marks, bins=5)
plt.title("Marks Distribution - Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()