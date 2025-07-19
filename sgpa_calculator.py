def get_grade_point(total_marks):
    if total_marks >= 90:
        return 10
    elif total_marks >= 80:
        return 9
    elif total_marks >= 70:
        return 8
    elif total_marks >= 60:
        return 7
    elif total_marks >= 50:
        return 6
    elif total_marks >= 40:
        return 5
    else:
        return 0

def calculate_sgpa():
    n = int(input("Enter number of subjects: "))
    total_credit_points = 0
    total_credits = 0

    for i in range(n):
        print(f"\nSubject {i+1}")
        title = input("  - Title: ")
        code = input("  - Code: ")
        credits = float(input("  - Credits: "))
        internal = float(input("  - Internals (out of 40): "))
        external = float(input("  - Externals (out of 60): "))
        
        total_marks = internal + external
        grade_point = get_grade_point(total_marks)
        credit_points = grade_point * credits
        
        total_credit_points += credit_points
        total_credits += credits

    sgpa = total_credit_points / total_credits if total_credits > 0 else 0
    print(f"\n🎓 Your SGPA is: {sgpa:.2f}")

if __name__ == "__main__":
    calculate_sgpa()
