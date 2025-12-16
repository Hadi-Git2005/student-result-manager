def rank_students(students):
    return sorted(
        students,
        key = lambda s : s.total_marks(),
        reverse=True
    )

def rank_by_subject(students,subject):
    return sorted(
        students,
        key = lambda s : s.marks.get(subject[0],0),
        reverse=True
        )

def topper_in_subject(students,subject):
    return max(students,key = lambda s:s.marks.get(subject,0))

def weak_subjects(student):
    threshold = 80
    return (student.name,[i for i,m in student.marks.items() if m < threshold])