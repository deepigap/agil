class Student: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def display(self): 
        print("Name:", self.name) 
        print("Age:", self.age) 
class GradeCalculator: 
    @staticmethod 
    def calculate_grade(marks): 
        if marks >= 90: 
            return "A" 
        elif marks >= 75: 
            return "B" 
        else: 
            return "C"