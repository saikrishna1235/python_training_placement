class Grand_father:
    def land(self):
        print("I have 10 acers of land")
class Father(Grand_father):
    def house(self):
        print("I have 5 acers of land")
class Son(Father):
    pass
class Daughter(Father):
    pass
obj=Son()
obj.land()
obj.house()
obj=Daughter()
obj.land()
obj.house