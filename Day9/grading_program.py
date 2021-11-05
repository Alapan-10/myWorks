student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
}

student_grades = {}
for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        grade = "Excellent"
    elif score < 91 and score >= 81:
        grade = "Exceeds Expectations"
    elif score < 81 and score >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade

print(student_grades)
