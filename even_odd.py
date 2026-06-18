numbers=[]
for i in range(10):
    num=int(input("enter the numbers :"))
    numbers.append(num)
for num in numbers:
    if num%2==0:
        print("Even numbers :" ,num)
    else:
        print("Odd numbers :" ,num)