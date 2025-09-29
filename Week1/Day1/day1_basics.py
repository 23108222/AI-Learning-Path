# Day 1 - Python Basics for AI
# Author: Bilal Khan
# Repo: AI-Learning-Path

# -------------------------------
# Exercise 1 – Variables & Print
# -------------------------------
name = "Bilal"
age = 20
print("Hello", name, "you are", age, "years old.")
print("In 5 years you will be", age + 5, "years old.")

# -------------------------------
# Exercise 2 – If/Else Conditions
# -------------------------------
marks = 75

if marks >= 80:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Your grade is:", grade)

# -------------------------------
# Exercise 3 – Loops
# -------------------------------
print("Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")  # newline

# -------------------------------
# Exercise 4 – Functions
# -------------------------------
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 5 is:", factorial(5))

# -------------------------------
# Exercise 5 – Lists & Dictionaries
# -------------------------------
fruits = ["apple", "banana", "mango"]
print("Original fruits list:", fruits)

fruits.append("orange")  # add
fruits.remove("banana")  # remove

print("Updated fruits list:")
for fruit in fruits:
    print(fruit)

students = {"Ali": 85, "Sara": 92, "Bilal": 78}
print("\nStudent marks:")
for name, marks in students.items():
    print(name, ":", marks)

# -------------------------------
# End of Day 1
# -------------------------------
print("\n✅ Day 1 exercises completed successfully!")
