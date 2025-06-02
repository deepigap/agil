class Student: 
    def __init__(self, name, age, marks): 
        self.name = name 
        self.age = age 
        self.marks = marks 
    def display(self): 
        print("Name:", self.name) 
        print("Age:", self.age) 
        print("Marks:", self.marks) 
    def calculate_grade(self): 
        if self.marks >= 90: 
            return "A" 
        elif self.marks >= 75: 
            return "B" 
        else: 
            return "C"
        