def bs():
    am=50
    qu=int(input("Enter quantity"))
    bill=am*qu
    print("----------------")
    print("Amount   :",bill)
    print("GSt      :18rs")
    print("total    :",bill+18)
    print("---------------------")
def va():
    am=30
    qu=int(input("Enter quantity"))
    bill=am*qu
    print("----------------")
    print("Amount   :",bill)
    print("GSt      :18rs")
    print("total    :",bill+18)
    print("---------------------")
def st():
    am=30
    qu=int(input("Enter quantity"))
    bill=am*qu
    print("----------------")
    print("Amount   :",bill)
    print("GSt      :18rs")
    print("total    :",bill+18)
    print("---------------------")
def mwa():
    am=12
    qu=int(input("Enter quantity"))
    bill=am*qu
    print("----------------")
    print("Amount   :",bill)
    print("GSt      :18rs")
    print("total    :",bill+18)
    print("---------------------")
print("\t**********Welcome to chimtu icream center**********")
print("MENU\n1.bs-----50/-\n2.va-----30/-\n3.st-----30/-\n4.mwa-----12/-")
op=input("Select")
if op=="1":
    bs()
elif op=="2":
    va()
elif op=="3":
    st()
elif op=="4":
    mwa()
else:
    print("****Invalid number****")
