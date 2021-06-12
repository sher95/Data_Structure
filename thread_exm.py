# GIL Global interpreter lock
# A lock allows only one thread at a time to execute in python
# Need in CPython because memory management is not thread-safe
# Use multiprocessing
from threading import Thread
import os
import time


def square():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == "__main__":
    thr = []
    num_thr = os.cpu_count()

    # create processes
    for i in range(num_thr):
        p = Thread(target=square)
        thr.append(p)

    
    # start
    for p in thr:
        p.start()


    # join
    for p in thr:
        p.join()

    print("end main")