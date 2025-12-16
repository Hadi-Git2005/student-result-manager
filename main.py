from student import Student
from analytics import *
from storage import load_students, add_students

def create_student():
    try:
        id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        marks = {}
        subjects = ["Math","Science","English"]
        for sub in subjects:
            m = int(input(f"Enter marks for {sub} : "))
            marks[sub] = m
        student = Student(id,name,marks)
        add_students(student)
        print("Student added successfully!")
    except Exception as e:
        print("Error creating student:",e)
    print()

def overall_ranking(students):
    print("Overall Ranking: \n")
    ranked_students = rank_students(students)
    for index,student in enumerate(ranked_students,start = 1):
        print(index,student.name,student.total_marks())
    print()

def subject_ranking(students):
    print("\nRanking by Subjects")
    subject = ["Math","Science","English"]
    for sub in subject:
        subject_wise_rank = rank_by_subject(students,sub)
        print(f"\nRanking for {sub}:")
        for index,student in enumerate(subject_wise_rank,start=1):
            print(index,student.name,student.marks[sub])
        print()

def topper(students):
    for subject in ["Math","Science","English"]:
        topper = topper_in_subject(students,subject)
        print("Topper in",subject,":",topper.name,topper.marks[subject])
    print()

def weak_subjects_report(students):
    print("Weak Subjects Report:")
    for student in students:
        weak = weak_subjects(student)
        print("Weak Subjects for:",weak[0],":",*weak[1])
    print()

def main():
    students = load_students()

    #Display existing data
    overall_ranking(students)
    subject_ranking(students)
    topper(students)
    weak_subjects_report(students)

    #Add new student
    create_student()

    #Display updated data
    students = load_students()
    overall_ranking(students)
    subject_ranking(students)
    topper(students)
    weak_subjects_report(students)

if __name__ == "__main__":
    main()

