class Student:
    def __init__(self,s_name,s_gpa):
        self.name = s_name
        self.gpa = s_gpa
    def report_gpa(self):
        print(f'{self.name} has a {self.gpa}')