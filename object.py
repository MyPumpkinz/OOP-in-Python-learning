from person import *
from student import Student
from teacher import Teacher 

def object():
    # person object
    per = Person("Randy", "Anugerah", "Malang", univ, hv)
    per.display()
    print("===========================================")
    std = Student("Reza", "Dharma", "Kalsel", univ, hv, 22, 2022)
    std.display()
    print("===========================================")
    tch = Teacher("Alfin", "Yusriansyah", "Banyuwangi", univ, hv, 28, "2juta")
    tch.display()