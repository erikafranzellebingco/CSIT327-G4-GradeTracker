# Bingco, Erika Franzelle R. 9/29/2026

"""Student Grade Tracker Python Quick-Start Lab"""

def get_valid_score(prompt):
    """Keep asking until the user enters a number from 0 to 100."""
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                print(f"Accepted: {score}")
                return score
            else:
                print("Invalid. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_average(scores):
    """Return the average of a list of numbers."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def get_grade(avg):
    """Return a letter grade (A/B/C/D/F) for an average."""
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

def print_report(records):
    """Print the formatted table. records is a list of (name, avg, grade)."""
    print("\n===== CLASS REPORT =====")
    print(f"{'Name':<12}{'Average':>10}{'Grade':>8}")
    for name, avg, grade in records:
        print(f"{name:<12}{avg:>10.2f}{grade:>8}")

def main():
    records = []  
    avg_list = [] 
    
    n = int(input("How many students? "))
    
    for i in range(n):
        print(f"\nStudent {i + 1}:")
        name = input(f"Student {i + 1} name: ")
        
        scores = []
        for j in range(3):
            score = get_valid_score(f"  Score {j + 1}: ")
            scores.append(score)
            
        avg = calculate_average(scores)
        grade = get_grade(avg)
        
        records.append((name, avg, grade))
        avg_list.append(avg)

    print_report(records)
    
    highest, lowest, mean = get_stats(avg_list)
    print(f"\nHighest: {highest:.2f}    Lowest: {lowest:.2f}    Class mean: {mean:.2f}")
    
    sorted_records = sorted(records, key=lambda r: r[1], reverse=True)
    top3 = sorted_records[:3]
    top3_names = ", ".join([r[0] for r in top3])
    print(f"Top 3: {top3_names}")

if __name__ == "__main__":
    main()