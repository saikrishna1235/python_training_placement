class Animal:
    def eat(self):
        print("Eating food")
class Dog(Animal):
    def bark(self):
        print("Bark")

D = Dog()
D.eat()
D.bark()