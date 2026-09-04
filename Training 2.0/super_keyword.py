class Animal:
    def eat(self):
        print("Eating food")

class Dog(Animal):
    def eat(self):
        super().eat()
        print("Dog is eating")

    def bark(self):
        print("Bark")

dog = Dog()
dog.eat()
dog.bark()