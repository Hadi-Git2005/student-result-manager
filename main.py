from analytics import *
from storage import load_students

students = load_students()

print("Student lenght :",len(students))
for s in students:
    print(s.name)

subject = "Math"

ranked_students = rank_students(students)

print("Overall Ranking: \n")
for index,student in enumerate(ranked_students,start = 1):
    print(index,student.name,student.total_marks())

subject_wise_rank = rank_by_subject(students,subject)

print("\nRanking by", subject)
for index,student in enumerate(subject_wise_rank,start=1):
    print(index,student.name,student.marks[subject])

print()

topper = topper_in_subject(students,subject)
print("Topper in",subject,":",topper.name,topper.marks[subject])

print()

for student in students:
    weak = weak_subjects(student)
    print("Weak Subjects for:",weak[0],":",*weak[1])
