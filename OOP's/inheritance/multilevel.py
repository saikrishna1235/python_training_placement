class Grand_father:
    def land(self):
        print("I have 10 acers of land")
class Father(Grand_father):
    def house(self):
        print("I have 5 acers of land")
class Child(Father):
    pass
obj=Child()
obj.land()
obj.house()