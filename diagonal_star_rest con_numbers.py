def star(n):
    s=n
    for i in range(5):
        for j in range(1,n+1):
            if j == s:
                print("*",end="  ")
            else:
                print(j,end='  ')
        s-=1
        print()
n=int(input("Enter s value :"))
star(n)