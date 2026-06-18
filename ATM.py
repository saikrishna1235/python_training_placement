import time
amount = 10000
def withdraw():
    global amount
    am=int(input("Enter amount withdraw :"))
    if am<= amount and am>0:
        if am%100 == 0:
            print("Processing.......")
            time.sleep(1)
            print("Withdraw sucess")
            amount = amount-am
            time.sleep(5)
            print("Thanks for using Fraud Bank")
        else:
            print("Enter 100 multiples")
    else:
        print("Invalid amount")
def deposit():
    global amount
    am=int(input("Enter amount deposit :"))
    if  am>0:
        if am%100 == 0:
            time.sleep(1)
            print("Processing.......")
            amount = amount+am
            time.sleep(4)
            print("deposit sucess")
            time.sleep(3)
            print("Balance :",amount)
            time.sleep(1)
            print("Thanks for using Fraud Bank")
        else:
            print("Enter 100 multiples")
    else:
        print("Invalid amount")
def balance():
    global amount
    print("\t********Account balance********")
    print("Balance :",amount)
def transferr():
    global amount
    secure_deposit=15000
    ac=int(input("Enter the account number :"))
    dac=int(input("Re_enter account number"))
    if ac==dac:
        am=int(input("enter the amount to Transfer :" ))
        if am>secure_deposit:
            pan=input("For security reasons enter the PAN number :")
            amount-=am
            time.sleep(3)
            print(amount)
            print("Thanks for using Fraud Bank")
        else:
            amount-=am
            time.sleep(3)
            print(amount)
            print("Thanks for using Fraud Bank")
    else:
        print("acount number not matching")
print("\t\t********Welcome to Fraud Bank********")
ch=3
while ch>0:
    name=input("Enter Username")
    psw=input("Enter password")
    if name =="admin" and psw == "1234":
        op=input("Select\n1.Withdraw\n2.Deposit\n3.Check Balance\n4.Transfer")
        if op == "1":
            withdraw()
            break
        elif op == "2":
            deposit()
            break
        elif op =="3":
            balance()
            break
        elif op == "4":
            transferr()
            break