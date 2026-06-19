li=[2,4,5,3,6,"hi","mom","dad",True,False]
integers=[]
strings=[]
bools=[]
for i in range(len(li)):
    if type(li[i]) == int and li[i]%2 !=0:
        integers.append(li[i])
    elif type(li[i]) == str and li[i] == li[::-1]:
        strings.append(li[i])
    elif type(li[i] == bool) and li[i] == True:
        bools.append(li[i])
print(integers)
print(strings)
print(bools)