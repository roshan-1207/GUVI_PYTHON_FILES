class student:
    def __init__ (self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def get_details(self):
        print("The student name is",self.name,"age is",self.age, "marks",self.marks)
e1 = student("geethu",18,100)
e2 = student("roshan",18,100)
e1.get_details()
e2.get_details()
