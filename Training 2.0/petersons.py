
balance = 1000
flag = False
def withdraw(amount):
    global balance
    flag = True

    if balance >= amount:
        balance -= amount
        print("Amount deducted and balance is ", balance)
    else:
        print("Insufficient balance")

    flag = False

if flag == False:
    withdraw(700)
else:
    print("Access Denied")