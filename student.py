class Student:
    def __init__(self,id,name,marks):
        self.id = id
        self.name = name
        self.marks = marks
    def total_marks(self):
        return sum(self.marks.values())
    def avg_marks(self):
        return self.total_marks()/len(self.marks)
