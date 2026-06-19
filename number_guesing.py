def num_guess():
    import random
    num=random.randint(1,10)
    ch=5
    points=0
    while ch>0:
        g_num = int(input("Enter num to guess"))
        if ch == 5 and g_num == num:
            points+=10
            break
        elif ch == 4 and g_num == num:
            points+=8
            break
        elif ch == 3 and g_num == num:
            points+=5
            break
        elif ch == 2 and g_num == num:
            points+=2
            break
        elif ch == 51 and g_num == num:
            points+=1
            break
        else:
            ch-=1
    else:
        print(num)
try:
    num_guess()
except:
    print("Enter only nums")
