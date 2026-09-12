import threading
mutex = threading.Lock()

balance = 1000

def withdraw(amount):
    global balance
    mutex.acquire()

    if balance >= amount:
        balance -= amount
        print("Amount deducted and balance is ", balance)
    else:
        print("Insufficient balance")

    mutex.release()

t1 = threading.Thread(target=withdraw,args=(700,))
t2 = threading.Thread(target=withdraw,args=(200,))

t1.start()
t2.start()

t1.join()
t2.join()


