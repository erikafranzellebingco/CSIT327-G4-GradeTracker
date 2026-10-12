student_name = input("Enter student name: ")
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
total_score = score1 + score2 + score3
average_score = total_score / 3

print(f"{student_name} - Total: {total_score: .2f}, Average: {average_score: .2f}")

# Task 3.1
avg_list = []
avg_list.append(average_score)
total_students = len(avg_list)
class_mean = sum(avg_list) / total_students
highest_score = max(avg_list)
lowest_score = min(avg_list)

sorted_avgs = sorted(avg_list, reverse=True)

top3 = sorted_avgs[:3]
print("Top 3 averages:", top3)

# Task 3.2
records = []
records.append(("Alex", 82.5, "A"))

for name, avg, grade in records:
    print(f"{name:<12}{avg:>8.2f}{grade:>6}")
# Tuple is a sensible choice here because it doesn't support object assignment, meaning that finalised records such as grades cannot be easily changed.

# Task 3.3

def calculate_average(scores):
    """Return the average of a list of numbers."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def get_grade(avg):
    """Return the letter grade for a numeric average."""
    if avg < 0 or avg > 100:
        return "Invalid average"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def get_stats(avg_list):
    """Return (highest, lowest, mean) for a list of averages."""
    if not avg_list:
        return (0.0, 0.0, 0.0)
    highest = max(avg_list)
    lowest = min(avg_list)
    mean = sum(avg_list) / len(avg_list)
    return (highest, lowest, mean)