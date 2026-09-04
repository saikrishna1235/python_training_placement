class Parent:
    def Land(self):
        print("Land")
class C1(Parent):
    def car(self):
        print("Car")
class C2(Parent):
    def Bike(self):
        print("Bike")

C = C1()
C.Land()

CC = C2()
C.Land()

# CC.car()