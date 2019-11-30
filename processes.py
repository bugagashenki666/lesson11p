from multiprocessing import Process
import os
from time import sleep


def f(start, end, timeout):
    while start < end:
        print(f"Process {os.getpid()}:{start}")
        start += 1
        sleep(timeout)


if __name__ == "__main__":
    p1 = Process(target=f, args=(3, 30, 1))
    p2 = Process(target=f, args=(5, 40, 0.5))
    p1.start()
    p2.start()
    print("END")
