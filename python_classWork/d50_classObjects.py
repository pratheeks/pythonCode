class Person:
    f_name = 'pratik'
    l_name = 'seraje'
    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name
    def display(self):
        print("First Name:",self.f_name,"Last Name:",self.l_name)

p1=Person("seraje","pratik")

p1.display()

