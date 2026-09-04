def call(i):
    print(i)
    if(i<3):
        call(i+1)
        call(i=i+i)
call(1)