import json
from student import Student

FILE_NAME = 'students.json'

def load_students():
    import os
    print("Reading file from:", os.path.abspath(FILE_NAME))
    with open(FILE_NAME,'r') as file:
        data = json.load(file)
        students = []
        for item in data:
            try:
                students.append(Student(item["id"],item["name"],item["marks"]))
            except:
                print("Error loading student:",item)
        return students

# def save_students(students):
#     data = []
#     for student in students:
#         data.append({
#             "id":student.id,
#             "name":student.name,
#             "marks":student.marks
#         })
#     with open(FILE_NAME,'w') as file:
#         json.dum(data,file,indent=4)