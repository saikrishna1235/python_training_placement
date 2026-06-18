ages=[]
for i in range(5):
    age=int(input("Enter the age of the person:"))
    ages.append(age)
elr=ages[0]
you=ages[0]
for age in ages:
    if age>elr:
        elr=age
    if age<you:
        you=age
print(elr,you)