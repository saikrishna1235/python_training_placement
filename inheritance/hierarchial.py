class Father:
    def land(self):
        print("I have 10 acers of land")
class Son(Father):
    def house(self):
        pass
class Daughter(Father):
    pass
obj=Son()
obj.land()
obj=Daughter()
obj.land()