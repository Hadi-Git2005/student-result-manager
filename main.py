from student import Student
from analytics import *
s1 = Student(1,"Hadi",{"Math":90,"Science":85,"English":88})
s2 = Student(2,"Uwais",{"Math":90,"Science":95,"English":98})
s3 = Student(3,"Ali",{"Math":70,"Science":75,"English":78})
s4 = Student(4,"Ayaan",{"Math":95,"Science":95,"English":99})

students = [s1,s2,s3,s4]

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

weak = weak_subjects(s3)
name,subjects = weak
print(name,"is weak in",*subjects)
