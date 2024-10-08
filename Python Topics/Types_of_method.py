class Student:
    school = "MKET"
    
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def avg(self):
        return (self.marks1 + self.marks2 + self.marks3)
    
    @classmethod
    def get_school_name(cls):
        return cls.school
    
    @staticmethod
    def data():
        print("this is the student code")

std1 = Student(120, 230, 130)
std2 = Student(340, 130, 400)
print(std1.avg())                # Output: 480
print(Student.get_school_name())      # Output: MKET
Student.data()                   # Output: this is the student code
