from threading import Thread, Lock
import time
db_val = 0

def increase():
    global db_val

    local_copy = db_val

    #processing
    local_copy += 1
    time.sleep(0.1)

    db_val = local_copy


if __name__ == '__main__':
    lock = Lock

    print("start value", db_val)

    th1 = Thread(target=increase, args=(lock,))
    th2 = Thread(target=increase)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print("end value", db_val)

    print("end main")
