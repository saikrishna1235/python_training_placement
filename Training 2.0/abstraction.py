from abc import ABC,abstractclassmethod

class Payment:
    @abstractclassmethod
    def pay(self,amount):
        pass
class Upipayment(Payment):
    def pay(self,amount):
        print("Paid using UPI :" ,amount)
class Cardpayment(Payment):
    def pay(self,amount):
        print("Paid using card",amount)

Upi = Upipayment()
Upi.pay(1000)
card=Cardpayment()
card.pay(2500)