class Parent1:
    def land(self):
        print("I have 10 acers of land")
class Parent2:
    def gold(self):
        print("I have 10 kg of gold")
class Child(Parent1,Parent2):
    pass
obj=Child()
obj.land()
obj.gold()