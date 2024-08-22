import time
from concurrent.futures import ThreadPoolExecutor


def worker(number):
    print(f"Calculating the result for number {number}")
    time.sleep(2)

    return number**2


pool = ThreadPoolExecutor(2)

work1 = pool.submit(worker, 7)
work2 = pool.submit(worker, 9)
work3 = pool.submit(worker, 5)
work4 = pool.submit(worker, 5)
work5 = pool.submit(worker, 8)
work6 = pool.submit(worker, 9)
work7 = pool.submit(worker, 3)
work8 = pool.submit(worker, 1)


print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")


if work3.done():
    print(work3.result())
else:
    print("No results yet")

time.sleep(5)

if work3.done():
    print(work3.result())


work9 = pool.submit(worker, 8)
work10 = pool.submit(worker, 9)
work11= pool.submit(worker, 3)

pool.shutdown()
