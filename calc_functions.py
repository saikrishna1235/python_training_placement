def add(a,b):
    print(a+b)
def sub(a,b):
    print(a+b)
def mul(a,b):
    print(a+b)
def div(a,b):
    print(a+b)
def mod(a,b):
    print(a+b)
a=int(input("Enter number 1 :"))
op=input("select one option\n1.add\n2.sub\n3.mul\n4.div\n5.mod")
b=int(input("Enter number 2 :"))
if op=="1":
    add(a,b)
elif op=="2":
    sub(a,b)
elif op=="3":
    mul(a,b)
elif op=="4":
    div(a,b)
elif op=="5":
    mod(a,b)
else:
    print("Invalid number")