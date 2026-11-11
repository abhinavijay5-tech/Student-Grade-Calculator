
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

print("Welcome,", name)

mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))
mark4 = float(input("Enter marks for subject 4: "))
mark5 = float(input("Enter marks for subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5

percentage = (total / 500) * 100

print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")