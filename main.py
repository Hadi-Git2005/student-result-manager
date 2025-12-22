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
    ranked_students = rank_students(students)
    for index,student in enumerate(ranked_students,start = 1):
        print(index,student.name,student.total_marks())
    print()

def subject_ranking(students,subject):
    subject_wise_rank = rank_by_subject(students,subject)
    for index,student in enumerate(subject_wise_rank,start=1):
        print(index,student.name,student.marks[subject])
    print()

def topper(students,subject):
    topper = topper_in_subject(students,subject)
    print("Topper in",subject,":",topper.name,topper.marks[subject])

def weak_subjects_report(students,id):
        c = 0
        for student in students:
            if student.id == id:
                c = 1
                weak = weak_subjects(student,id)
                print("Weak Subjects for:",weak[0],":",*weak[1])
        if c == 0:
            print("Invalid Id")
        

            

def main():
    students = load_students()

    while True:
        print()
        print("-----STUDENT RESULT MANAGER-----\n")
        print("Choices : \n")
        print("1 -> View Overall Ranking\n")
        print("2 -> View Subject-wise Ranking\n")
        print("3 -> View Topper in a subject\n")
        print("4 -> View Weak Subjects\n")
        print("5 -> Add New Student\n")
        print("6 -> Exit\n")

        choice = input("Enter Your Choice : ")
        print()

        if choice == "1":
            print("Overall Ranking \n")
            overall_ranking(students)
        elif choice == "2":
            print("Subject-wise Ranking: \n")
            sub = input("Enter The Subject : ")
            subject_ranking(students,sub)
        elif choice == "3":
            sub = input("Enter The Subject : ")
            print("\nTopper in the {sub}")
            topper(students,sub)
        elif choice == "4":
            id = int(input("Enter Student Id : "))
            print("Weak Subjects\n")
            weak_subjects_report(students,id)
        elif choice == "5":
            create_student()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
            print()
        
if __name__ == "__main__":
    main()

