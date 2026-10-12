# Q1: The language I know best is Java, which requires explicit class definitions, the psvm entry point, and semicolons at the end of each statement to run. Python does not require any of that. Instead, I was able to write what I wanted to print directly.
# Q2: They are data types. int represents integers or whole numbers, float represents decimal numbers, str represents strings or text, and bool represents boolean values (True or False). On the other hand, type() is a built-in Python function that returns the data type of an object or variable.
# Q3: Trying to print "5" + 5 creates a TypeError because Python does not allow concatenation of a string and an integer. However, using int("5") converts the string "5" to an integer, allowing the addition operation to work correctly and return 10.

# Task 1.1
student_name = input("Enter student name: ")
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
total_score = score1 + score2 + score3
average_score = total_score / 3

print(f"{student_name} - Total: {total_score: .2f}, Average: {average_score: .2f}")

# Task 1.2
print(type(student_name))
print(type(score1))
print(type(score2))
print(type(score3))
print(type(total_score))
print(type(average_score))

# Task 1.3
print(7 / 2) # 3
print(7 // 2) # 3
print(7 % 2) # 1
print(2 ** 3) # 6
print("ab" * 3) # TypeError

