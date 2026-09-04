class Father:
    def skill(self):
        print("Driving")
class Mother:
    def talent(self):
        print("Cooking")
class Child(Father,Mother):
    def study(self):
        print("Studying")
C = Child()
C.skill()
C.talent()
C.study()

