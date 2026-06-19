def even_char(name):
    for i in range(len(name)):
        if i%2==0 and name[i].isalpha():
            if name[i] == 'z':
                print("a")
            elif name[i] == 'Z':
                print("Z")
            else:
                print(chr(ord(name[i])+1),end='')
        else:
            print(name[i],end='')
name= input("Enter a name :")
even_char(name)