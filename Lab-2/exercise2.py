print("--- Problem 1: Course Marks ---")
marks = [75, 82, 45, 90, 60]

total = 0
passed_count = 0
highest = marks[0]
lowest = marks[0]

for m in marks:
    total += m
    if m >= 50:
        passed_count += 1
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m

average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Passed Courses:", passed_count)


print("\n--- Problem 2: Weekend Temperatures ---")
temperatures = (28.5, 30.0, 29.2, 27.0, 26.5, 27.8)

highest_temp = temperatures[0]
lowest_temp = temperatures[0]

print("Temperature Readings:")
for temp in temperatures:
    print(temp)
    if temp > highest_temp:
        highest_temp = temp
    if temp < lowest_temp:
        lowest_temp = temp

print("Highest Temperature:", highest_temp)
print("Lowest Temperature:", lowest_temp)


print("\n--- Problem 3: Word Analyzer ---")
text = input("Enter a word or short sentence: ")

char_count = 0
vowel_count = 0
space_count = 0
vowels = "aeiouAEIOU"

for char in text:
    char_count += 1
    if char == " ":
        space_count += 1
    elif char in vowels:
        vowel_count += 1

print("Total Characters:", char_count)
print("Total Vowels:", vowel_count)
print("Total Spaces:", space_count)


print("\n--- Problem 4: Grade Calculator ---")
def calculate_grade(marks_list):
    total_marks = 0
    for m in marks_list:
        total_marks += m
    average_mark = total_marks / len(marks_list)
    
    if average_mark >= 80:
        return 'A'
    elif average_mark >= 70:
        return 'B'
    elif average_mark >= 60:
        return 'C'
    elif average_mark >= 50:
        return 'D'
    else:
        return 'F'

my_marks = [78, 85, 90, 65, 80]
grade = calculate_grade(my_marks)
print("Calculated Grade:", grade)


print("\n--- Problem 5: Shopping Cart Processor ---")
cart = [
    {"name": "Notebook", "price": 150, "quantity": 4},
    {"name": "Pen", "price": 20, "quantity": 10},
    {"name": "Bag", "price": 1200, "quantity": 1},
    {"name": "Marker", "price": 50, "quantity": 5}
]

total_cost = 0
for item in cart:
    line_total = item["price"] * item["quantity"]
    total_cost += line_total

def apply_discount(total):
    if total >= 2000:
        return total - (total * 0.10)
    else:
        return total

final_cost = apply_discount(total_cost)
print("Original Total Cost:", total_cost)
print("Final Cost after Discount:", final_cost)


print("\n--- Problem 6: Countdown ---")
num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Please enter a non-negative integer.")
else:
    while num >= 0:
        print(num)
        num -= 1


print("\n--- Problem 7: Student Record Analyzer ---")
students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]

passed_students = 0
total_student_marks = 0
highest_marks = students[0]["marks"]
top_student = students[0]["name"]

print("Student Names and Marks:")
for s in students:
    print(s["name"], ":", s["marks"])
    total_student_marks += s["marks"]
    
    if s["marks"] >= 50:
        passed_students += 1
        
    if s["marks"] > highest_marks:
        highest_marks = s["marks"]
        top_student = s["name"]

class_average = total_student_marks / len(students)

print("\nTotal Students Passed:", passed_students)
print("Class Average Marks:", class_average)
print("Top Student:", top_student, "with marks:", highest_marks)


print("\n--- Problem 8: Product Inventory Summary ---")
products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

total_inventory_value = 0
highest_line_total = 0
top_product = ""

for p in products:
    line_total = p["price"] * p["quantity"]
    total_inventory_value += line_total
    print(p["name"], "- Line Total:", line_total)
    
    if line_total > highest_line_total:
        highest_line_total = line_total
        top_product = p["name"]

print("\nTotal Inventory Value:", total_inventory_value)
print("Product with Highest Line Total:", top_product, "with value:", highest_line_total)
