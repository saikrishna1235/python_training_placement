class Person:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name

    def display_person(self):
        print("ID :", self.ID)
        print("Name :", self.Name)


class Student(Person):
    def __init__(self, Student_ID, Student_Name, Department, Number_of_Late_Days):
        super().__init__(Student_ID, Student_Name)
        self.Department = Department
        self.Number_of_Late_Days = Number_of_Late_Days

    def calculate_fine(self):
        if self.Number_of_Late_Days <= 0:
            print("Fine : 0")
        elif self.Number_of_Late_Days <= 5:
            print("Fine : 50")
        elif self.Number_of_Late_Days <= 10:
            print("Fine : 100")
        else:
            print("Fine : 200")

    def display(self):
        self.display_person()
        print("Department :", self.Department)
        print("Number of Late Days :", self.Number_of_Late_Days)
        self.calculate_fine()


# Creating Student objects
s1 = Student(101, "Arun", "CSE", 7)
s2 = Student(102, "Vijay", "ECE", 11)

# Displaying student details and fine
print("----- Student 1 -----")
s1.display()

print("\n----- Student 2 -----")
s2.display()