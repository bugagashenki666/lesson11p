from threading import Thread
from time import sleep


def f(name, start, end, timeout):
    while start < end:
        print(f"Thread: '{name}' : {start}")
        start += 1
        sleep(timeout)


t1 = Thread(target=f, args=("Func1", 3, 10, 1), daemon=True)
t2 = Thread(target=f, args=("Func2", 5, 15, 0.5), daemon=True)
t1.start()
t2.start()

for i in range(5):
    print("Thread 'MAIN':", i)
    sleep(0.5)

t1.join()
print("F1 end")
t2.join()
print("F2 end")
print("END")
