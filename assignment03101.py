def calculate_grade(score):
    if score < 0.0 or score > 100.0:
        return "Error: Score is out of range"
    elif score >= 90.0:
        return "A"
    elif score >= 80.0 :
        return "B"
    elif score >= 70.0:
        return "C"
    elif score >= 60.0:
        return "D"
    elif score >= 50.0:
        return "E "
    else:
        return "F"
try:
    score = float(input("Enter a score between 0.0 and 100.0 : "))
    grade = calculate_grade(score)
    print(f"Grade is {grade}")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")