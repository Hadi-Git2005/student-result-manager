import json
from student import Student

FILE_NAME = 'students.json'

def load_students():
    import os
    print("Reading file from:", os.path.abspath(FILE_NAME))
    students = []
    try:
        with open(FILE_NAME,'r') as file:
            data = json.load(file)
            for item in data:
                try:
                    students.append(Student(item["id"],item["name"],item["marks"]))
                except:
                    print("Error loading student:")
    except json.JSONDecodeError:
        print("JSON file not found. Starting with empty student list.")
    except FileNotFoundError:
        print("File not found. Starting with empty student list.")
    return students
              
def save_students(students):
    data = []
    for student in students:
        data.append({
            "id":student.id,
            "name":student.name,
            "marks":student.marks
        })
    with open(FILE_NAME,'w') as file:
        json.dump(data,file,indent=4)

def add_students(student):
    students = load_students()
    students.append(student)
    save_students(students)
