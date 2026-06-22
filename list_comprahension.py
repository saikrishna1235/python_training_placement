vowels='aeiouAEIOU'
n=input("Enter the name")
l=[i for i in n if i not in vowels]
for i in range(len(l)):
    print(l[i], end=" ")
print("---",len(l))