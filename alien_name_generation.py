for i in range(10):
    names=input().split()
    if len(names)==2:
        if names[0].isalpha() and names[1].isalpha():
            if len(names[0])>=2 and len(names[1])>=2:
                nick=names[0][-2:]+names[1][0:2]
                print(nick[::-1])
            else:
                print("Name should contain min 2 char")
        else:
            print("Only alphas are allowed")
    else:
        print("Only 2 names are allowed")