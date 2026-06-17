for i in range(4):
    if i % 2 == 0:
        for j in range(6):
            if j == 0:
                print(0, end=" ")
            elif j <= 2:
                print(1, end=" ")
            else:
                print(2, end=" ")
    else:
        for j in range(6):
            if j < 3:
                print(2, end=" ")
            elif j < 5:
                print(1, end=" ")
            else:
                print(0, end=" ")
    print()