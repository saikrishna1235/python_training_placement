class Grandparent:
    def speak(self):
        print("Speak")
class Parent(Grandparent):
    def car(self):
        print("Car")
class Child(Parent):
    def play(self):
        print("Play")

C = Child()
C.play()
C.car()

P = Parent()
P.car()
P.speak()

G = Grandparent()
G.speak()