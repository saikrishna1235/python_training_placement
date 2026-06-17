n=int(input("Enter the number"))
res=n**2
t=n
count=0
while n>0:
    n=n//10
    count+=1
r=res%pow(10,count)
if(t==r):
    print("Automorphic number")
else:
    print("Not an Automorphic number")