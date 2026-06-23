from abc import ABC,abstractclassmethod
class Bike(ABC):
    @abstractclassmethod
    def engine(self):
        pass
    def acc(self):
        pass
class Bullet(Bike):
    def engine(self):
        print("It has 1000cc of engine")
    def acc(self):
        print("It can pickup in 1.2 sec")
gt = Bullet()
gt.engine()
