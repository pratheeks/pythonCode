class Person:
    def __init__(self):
        self.name=input("Enter the name")
        self.age=input("Enter the age")
        self.gender=input("Enter the gender")
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
class Marks:
    def __init__(self):
        self.m1=int(input("Enter the m1 marks"))
        self.m2=int(input("Enter the m2 marks"))
        self.m3=int(input("Enter the m3 marks"))
    def display(self):
        print("Total Marks",(self.m1+self.m2+self.m3))
        
class Student(Person,Marks):
    def __init__(self):
        Person.__init__(self)
        Marks.__init__(self)
    def results(self):
        Person.display(self)
        Marks.display(self)

s1=Student()
s1.results()

s2=Student()
s2.results()