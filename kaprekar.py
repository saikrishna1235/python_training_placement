n=10
res=n**2
length=len(str(n))
print(length)
r=res%pow(10,length)
left=res//pow(10,length)
sum=r+left
if n==sum:
    print(n,"is a Kaprekar number")
else:
    print(n,"is not a Kaprekar number")


