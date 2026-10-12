student_name = input("Enter student name: ")
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
total_score = score1 + score2 + score3
average_score = total_score / 3

print(f"{student_name} - Total: {total_score: .2f}, Average: {average_score: .2f}")

# Task 2.1
if average_score < 0 or average_score > 100:
    letter_grade = "Invalid average"
elif average_score >= 80:
    letter_grade = "A"
elif average_score >= 70:
    letter_grade = "B"
elif average_score >= 60:
    letter_grade = "C"
elif average_score >= 50:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Letter Grade: {letter_grade}")

# Task 2.2
while True:
    try:
        score = float(input("Enter score (0-100): "))
        if score >= 0 and score <= 100:
            print(f"Accepted: {score}")
            break
        else:
            print("Invalid. Score must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

#Task 2.3
n = int(input("How many students are there? "))
for i in range(n):
    student_name = input(f"Enter name for student {i + 1}: ")
    score1 = float(input("Enter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))
    total_score = score1 + score2 + score3
    average_score = total_score / 3

    if average_score < 0 or average_score > 100:
        letter_grade = "Invalid average"
    elif average_score >= 80:
        letter_grade = "A"
    elif average_score >= 70:
        letter_grade = "B"
    elif average_score >= 60:
        letter_grade = "C"
    elif average_score >= 50:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print(f"{student_name} - Total: {total_score: .2f}, Average: {average_score: .2f}, Letter Grade: {letter_grade}")

#Task 2.4
num = int(input("Enter a number: "))
print(f"Table for: {num}")

for i in range(1, 13):
    product = num * i
    if product > 100:
        break  
    if product % 5 == 0:
        continue 
    print(f"{num} x {i} = {product}")