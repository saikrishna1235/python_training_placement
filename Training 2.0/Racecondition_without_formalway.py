#implementation of syncronization manually

import threading
import time
balance = 1000
lk = 0
def lock():
    global lk
    while(lk==1):
        pass
    lk =1
def unlock():
    global lk
    lk = 0
def withdraw(amt):
    global balance
    lock()

    curr_bal = balance
    time.sleep(1)
    balance = curr_bal-amt

    unlock()

    print(threading.current_thread().name, "Withdraw",amt)

t1 = threading.Thread(target=withdraw, args=(200,), name="thread_1")
t2 = threading.Thread(target=withdraw, args=(300,), name="thread_2")
t1.start()
t2.start()
t1.join()
t2.join()
print("Completed and current Balance",balance)