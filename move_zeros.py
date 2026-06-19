li=[1,1,0,25,0,1,0,6]
# for i in range(len(li)):
#     if li[i] == 0:
#         print("Found")
for i in range(len(li)):
    # print(li[i])
    if li[i]==0:
        li[i]=li[i+1]
    else:
        i+=1
print(li) 

# def move_zeros():
#     num=[1,1,0,25,0,1,0,6]
#     nz=[]
#     z=[]
#     for i in num:
#         if i == 0:
#             z.append(i)
#         else:
#             nz.append(i)
#     nz.extend(z)
#     print(nz)
# move_zeros()