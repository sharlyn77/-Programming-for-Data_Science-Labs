print("--- Problem 1: Two Numbers Calculation ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num2 != 0:
    print("Quotient:", num1 / num2)
else:
    print("Quotient: Division by zero is not allowed.")


print("\n--- Problem 2: Formatted Student Profile ---")
name = input("Enter student name: ")
student_id = input("Enter student ID: ")
age = input("Enter age: ")
department = input("Enter department: ")
cgpa = input("Enter CGPA: ")

print("\n--- Student Profile ---")
print("Name:", name)
print("ID:", student_id)
print("Age:", age)
print("Department:", department)
print("CGPA:", cgpa)


print("\n--- Problem 3: Temperature Conversion ---")
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Temperature in Fahrenheit:", fahrenheit)
print("Temperature in Kelvin:", kelvin)


print("\n--- Problem 4: Student Marks Analyzer ---")
student_name = input("Enter student name: ")
mark1 = float(input("Enter mark for course 1: "))
mark2 = float(input("Enter mark for course 2: "))
mark3 = float(input("Enter mark for course 3: "))
mark4 = float(input("Enter mark for course 4: "))
mark5 = float(input("Enter mark for course 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5


highest = mark1
if mark2 > highest: highest = mark2
if mark3 > highest: highest = mark3
if mark4 > highest: highest = mark4
if mark5 > highest: highest = mark5


lowest = mark1
if mark2 < lowest: lowest = mark2
if mark3 < lowest: lowest = mark3
if mark4 < lowest: lowest = mark4
if mark5 < lowest: lowest = mark5


passed_count = 0
if mark1 >= 50: passed_count += 1
if mark2 >= 50: passed_count += 1
if mark3 >= 50: passed_count += 1
if mark4 >= 50: passed_count += 1
if mark5 >= 50: passed_count += 1

print("\n--- Student Result Summary ---")
print("Student Name:", student_name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Passed Courses:", passed_count)
