from multiprocessing import Lock, Process
import os
from time import sleep


class MyProcess(Process):
    def __init__(self, begin, end, timeout, lock):
        super().__init__()
        self.begin = begin
        self.end = end
        self.timeout = timeout
        self.lock = lock

    def run(self):
        while self.begin < self.end:
            with self.lock:
                print(f"Process '{os.getpid()}' : {self.begin}")
            self.begin += 1
            sleep(self.timeout)


if __name__ == "__main__":
    lock = Lock()

    t1 = MyProcess(begin=3, end=10, timeout=1, lock=lock)
    t2 = MyProcess(begin=5, end=15, timeout=0.5, lock=lock)
    t1.start()
    t2.start()
    for i in range(5):
        with lock:
            print(f"Process '{os.getpid()}': ", i)
        sleep(0.5)

    t1.join()
    t2.join()
    print("END")
