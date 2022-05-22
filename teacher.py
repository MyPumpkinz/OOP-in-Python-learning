from person import Person

class Teacher(Person):
    def __init__(self, fname, lname, address, univName, heartValves, age, salary):
        super().__init__(fname, lname, address, univName, heartValves)
        self.age = age
        self.salary = salary
        
    def display(self):
        super().display()
        print("Age: ", self.age)
        print("Salary per Month: ", self.salary)