class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        print("Brand :",self.brand)
        print("Model :",self.model)
        print("Price :",self.price)

c1 = Car("BMW" , "M4" , 10000000)
c2 = Car("Toyato", "Foutuner", 6000000)

c1.display()
c2.display()