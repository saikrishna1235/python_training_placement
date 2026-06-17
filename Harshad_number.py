#Harshad number is a number that is divisible by the sum of its digits. For example, 18 is a Harshad number because 1 + 8 = 9 and 18 is divisible by 9.
sum=0
n=18
r=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
if 18%sum==0:
    print(18,"is a Harshad number")
else:    print(18,"is not a Harshad number")