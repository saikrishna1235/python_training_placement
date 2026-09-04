class Student:
    college ="SRU"
    def __init__(self,name,dept,year):
        self.name = name
        self.dept = dept
        self.year = year
    def display(self):
        print(self.name)
        print(self.dept)
        print(self.year)
S1 = Student("Nithu" , "CSE", "2026")
S2 = Student("Dheeksha" , "CSE" ,  "2026")

S1.display()
S2.display()
