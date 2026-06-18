n=input("Enter a snumber : ")
sum=0
t=n
while n>0:
    r=n%10
    sum=sum+r**3
    n=n//10
if sum==t:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")