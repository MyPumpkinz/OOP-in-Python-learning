from person import Person

class Student(Person):
    def __init__(self, fname, lname, address, univName, heartValves, age, gradYear):
        super().__init__(fname, lname, address, univName, heartValves)
        self.age = age
        self.gradYear = gradYear
        
    def display(self):
        super().display()
        print("Age: ", self.age)
        print("Graduation Year: ", self.gradYear)