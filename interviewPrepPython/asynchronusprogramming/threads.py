import threading
import time

def worker():
    time.sleep(2)
    print("Done")


t1 = threading.Thread(target=worker)
t1.start()
t2 = threading.Thread(target=worker)
t2.start()
t3 = threading.Thread(target=worker)
t3.start()
t4 = threading.Thread(target=worker)
t4.start()


# Independent individual threads