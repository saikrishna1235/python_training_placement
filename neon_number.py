n=int(input("Enter the number"))
sum=0
res=n**2
while(res>0):
    r=res%10
    res=res//10
    sum=sum+r
if sum==n:
    print(n,"is a Neon number")
else:    
    print(n,"is not a Neon number")