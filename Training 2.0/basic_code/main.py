# for i in range(5):
#     print("GFG")

# sum = 0
# for i in range(1,6):
#     sum += i
# print(sum)

# n = 123
# while n>0:
#     l_d = n % 10
#     print(l_d)
#     n = n // 10
    

# n = 3
# for i in range(1,11):
#     print(n,"X",i,"=",i*n)

# n = 123456
# count=0
# while n>0:
#     digit = n%10
#     n = n//10
#     count+=1
# print(count)

# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# for i in range(3, 8, 1):
#     print(i)



# def is_prime(n):
#     if n<=1:
#         return False
#     if n == 2:
#         return True
#     if n%2 == 0:
#         return False
#     for i in range(3,int(n**0.5)+1,2):
#         if n%2==0:
#             return False
#     return True

# print(is_prime(1))


# n = 12

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# n = 153 
# digits = len(str(n))
# temp = n
# total = 0
# while temp>0:
#     digit = temp%10
#     total+=digit**digits
#     temp//=10
# print(total==n)


# n=100
# digits=len(str(n))
# temp=n
# total=0
# while temp>0:
#     digit = temp%10
#     total+=digit**digits
#     temp//=10
# print(total==n)

# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# p=0
# n=0
# for i in range(len(numbers)):
#     if numbers[i]>0:
#         p+=1
#     else:
#         n+=1
# print(p,n)

# sum=0
# for i in range(2,11,2):
#     sum+=i
# print(sum)


# s = "Python"
# r_s = ""

# for ch in s:  
#     r_s = ch+r_s

# print(r_s)


# number = 5
# fact = 1
# while number>0:
#     fact*=number
#     number-=1
# print(fact)


# while True:
#     number = int(input("Enter the number"))
#     if number >0 and number <=10:
#         print("Good number")
#         break
#     else:
#         print("invalid number")



# number = 29

# is_prime =True
# if number>1:
#     for i in range(2,number):
#         if (number%i) == 0:
#             is_prime = False
#             break
# print(is_prime)

# list = ["apple","banana","orange","mango"]

# un=set()

# for item in list:
#     if item in un:
#         print("Duplicate")
#         break
#     else:
#         un.add(item)



# arr = [1,2,3,4,5]

# i = 0
# j = len(arr)-1
# while i < j:
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp
#     i+=1
#     j-=1
# print(arr)



# s = "racecar"
# i=0
# j=len(s)-1
# pal = True
# while i<j:
#     if s[i] == s[j]:
#         i+=1
#         j-=1
#         pal = True
#     else:
#         pal = False
#         break

# print(pal)

# def remove_duplicates(arr):
#     if len(arr) == 0:
#         return 0
#     i = 0
#     for j in range(1,len(arr)):
#         if arr[j]!=arr[i]:
#             i+=1
#             arr[i]=arr[j]
#     return i+1

# arr = [1,1,2,2,3,4,4]
# k = remove_duplicates(arr)
# print(arr[:k])



# arr = [0,1,0,3,12]

# i = 0
# for j in range(len(arr)):
#     if arr[j]!=0:
#         arr[i],arr[j]=arr[j],arr[i]
#         i+=1
# print(arr)


# number = 29

# is_prime =True
# if number>1:
#     for i in range(2,number):
#         if (number%i) == 0:
#             is_prime = False
#             break
# print(is_prime)




# n=12

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# n = 12345
# while n>0:
#     digit = n%10
#     print(digit)
#     n = n//10


# n = 100
# count=0
# result=0
# while n>0:
#     digit=n%10
#     count+=1
#     n=n//10
# print(count)
# for i in range(1,count+1):
#     digit = n%10
#     result+=digit**count
#     n=n//10
# print(result==n)