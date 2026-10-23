
# Student Marks, Average and Grade Calculator

print("===== STUDENT RESULT CALCULATOR =====")

name = input("Enter student name: ")

# Enter marks for 5 subjects
subjects = ["Tamil", "English", "Maths", "Science", "Social"]

marks = []

for subject in subjects:
    mark = float(input(f"Enter marks for {subject} (out of 100): "))

    if mark < 0 or mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        exit()

    marks.append(mark)

# Calculate total, average and percentage
total = sum(marks)
average = total / len(subjects)
percentage = (total / (len(subjects) * 100)) * 100

# Calculate grade
if any(mark < 35 for mark in marks):
    grade = "F"
    result = "FAIL"
elif average >= 90:
    grade = "A+"
    result = "PASS"
elif average >= 80:
    grade = "A"
    result = "PASS"
elif average >= 70:
    grade = "B"
    result = "PASS"
elif average >= 60:
    grade = "C"
    result = "PASS"
elif average >= 50:
    grade = "D"
    result = "PASS"
else:
    grade = "E"
    result = "PASS"

# Display student result
print("\n===== STUDENT REPORT =====")
print("Student Name:", name)

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

print("Total Marks:", total, "/ 500")
print("Average:", round(average, 2))
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)
