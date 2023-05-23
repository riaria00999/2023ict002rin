grade_points = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5,
    "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0
}

total_credit_hours = 0
total_weighted_grade_points = 0

for _ in range(20):
    course_name, credit_hours, grade = input().split()
    credit_hours = float(credit_hours)
    
    if grade != "P":
        total_credit_hours += credit_hours
        total_weighted_grade_points += credit_hours * grade_points[grade]

gpa = total_weighted_grade_points / total_credit_hours
print(round(gpa, 6))
