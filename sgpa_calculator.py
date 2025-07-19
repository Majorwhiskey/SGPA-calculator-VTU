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

def input_subject_data():
    n = int(input("Enter number of subjects: "))
    total_credits = 0
    total_credit_points = 0

    print("\nSubject-wise Entry:")
    for i in range(n):
        print(f"\nSubject {i+1}")
        title = input("  - Subject Title: ")
        code = input("  - Subject Code: ")
        credits = int(input("  - Credits: "))
        internals = int(input("  - Internal Marks: "))
        externals = int(input("  - External Marks: "))
        total = internals + externals
        grade_point = get_grade_point(total)
        credit_point = grade_point * credits

        print(f"    => Total: {total}, Grade Point: {grade_point}, Credit Point: {credit_point}")
        total_credits += credits
        total_credit_points += credit_point

    sgpa = round(total_credit_points / total_credits, 4) if total_credits else 0
    print(f"\n🎓 Final SGPA: {sgpa}")

# Run the script
input_subject_data()

