student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

def add_grade(student, score):
    if score > 90:
      student_grades[student] = 'Outstanding'
      return
    if score > 80:
      student_grades[student] = 'Exceeds Expectations'
      return
    if score > 70:
      student_grades[student] = 'Acceptable'
      return

    student_grades[student] = 'Fail'

for student in student_scores:
  add_grade(student, student_scores[student])

print(student_grades)