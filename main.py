from student import Student
s1 = Student(1,"Hadi",{"Math":90,"Science":85,"English":88})
s2 = Student(2,"Uwais",{"Math":90,"Science":95,"English":98})

students = [s1,s2]

for s in students:
    print(f"Name: {s.name}, Total Marks: {s.total_marks()}, Average Marks: {s.avg_marks()}")
    