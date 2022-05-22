from university import University
from heart import Heart

class Person:
    def __init__(self, fname, lname, address, univName, heartValves):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.univname = univName
        self.heartValves = heartValves #Aggregation
        # self.heartObject = Heart(self.heartValves)   # Composition
        
    def display(self):
        print("First Name: ", self.fname)
        print("Last Name: ", self.lname)
        print("Address: ", self.address)
        print("Universitas Name :", univ.get_university_name())
        print("No of Heart Valves: ", hv.display()) 
        # print("No of Heart Valves: ", self.heartObject.display())

univ = University("Universitas Muhammadiyah Malang")
hv = Heart(4)