import random
cell_num=input("Enter cell number:")
st="9876"
if len(cell_num)==10:
    if cell_num.isdigit():
        if cell_num[0] in st:
            print("Entered cell number")
            otp= random.randint(1000,9999)
            print(otp)
            ent=int(input("Enter OTP"))
            if ent==otp:
                print("Proceed to bookings")
            else:
                print("Invalid OTP")
        else:
            print("Enter valid cell num")
    else:
        print("Enter only nums")