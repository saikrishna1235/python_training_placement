def star(n):
    s=n
    for i in range(5):
        for j in range(1,6):
            if j == i+1:
                print(s,end="  ")
            else:
                print("*",end='  ')
        s-=1
        print()
n=int(input("Enter s value :"))
star(n)