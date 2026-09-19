import threading
import time

sema = threading.Semaphore(3)


def accessing():
    print(threading.current_thread().name, "waiting")

    sema.acquire()

    print(threading.current_thread().name, "accessing")

    time.sleep(1)

    print(threading.current_thread().name, "finished")

    sema.release()


threads = []

for i in range(6):
    t = threading.Thread(target=accessing, name=f"Thread-{i+1}")
    threads.append(t)
    t.start()


for t in threads:
    t.join()

print("All threads completed")