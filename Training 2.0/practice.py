from abc import ABC,abstractmethod
class Person:
  @abstractmethod
  def name(self):
    pass
  def superpower(self,power):
    print("my power is ",power)
  def weakness(self,weakness):
    print("my weakness is ",weakness)
  def role(self,role):
    print("my role is ",role)
class Student(Person):
  def name(self,name):
    print("my name is ",name)
s1=Student()
s1.name('arjun')
s1.superpower('sleeping only in class')
s1.weakness('monday morning')
s1.role('Pakka playboy')