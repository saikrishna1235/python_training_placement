def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
try:
    n=int(input("Enter a number :"))
    if is_prime(n) and is_prime(n+2):
        print("Twin prime")
    else:
        print("Get lost!!!")
except:
    print("Only int's should give")