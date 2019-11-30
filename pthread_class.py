from threading import Lock, Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, name, begin, end, timeout, lock):
        super().__init__()
        self.name = name
        self.begin = begin
        self.end = end
        self.timeout = timeout
        self.lock = lock

    def run(self):
        while self.begin < self.end:
            with self.lock:
                print(f"Thread '{self.name}' : {self.begin}")
            self.begin += 1
            sleep(self.timeout)


lock = Lock()

t1 = MyThread(name="1", begin=3, end=10000, timeout=0, lock=lock)
t2 = MyThread(name="2", begin=5, end=15000, timeout=0, lock=lock)
t1.start()
t2.start()
# for i in range(5):
#     with lock:
#         print("Thread 'main': ", i)
#     sleep(0.5)

t1.join()
t2.join()
print("END")