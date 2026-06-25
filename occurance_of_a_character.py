# def occurance(name):
#     count=0
#     for i in range(len(name)):
#         if name[i] in 'aA':
#             print(name[i])
#             count+=1
#         else:
#             pass
#     print(count)
# occurance("Akaksha")

def name():
    d={}
    name = input("Enter name")
    for ch in name:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch]+=1
    print(d)
name()