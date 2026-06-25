import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time


# CPU-bound task (nu sleep, ca să fie relevant pentru GIL)
def countdown():
    x = 50_000_000
    while x > 0:
        x -= 1


# 🔵 1. THREADING (concurență, NU paralelism real)
def ver_1():
    t1 = threading.Thread(target=countdown)
    t2 = threading.Thread(target=countdown)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


# 🟡 2. SECVENTIAL
def ver_2():
    countdown()
    countdown()


# 🔴 3. MULTIPROCESSING (paralelism real)
def ver_3():
    p1 = multiprocessing.Process(target=countdown)
    p2 = multiprocessing.Process(target=countdown)

    p1.start()
    p2.start()

    p1.join()
    p2.join()


# 🟠 4. THREADPOOL EXECUTOR
def ver_4():
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [
            executor.submit(countdown),
            executor.submit(countdown)
        ]

        for f in futures:
            f.result()


# ⏱️ helper pentru măsurare timp
def measure(func, name):
    start = time.time()
    func()
    end = time.time()
    print(f"\n{name}: {end - start:.4f} sec")


if __name__ == "__main__":
    measure(ver_1, "Threading (GIL - pseudo parallelism)")
    measure(ver_2, "Sequential")
    measure(ver_3, "Multiprocessing (real parallelism)")
    measure(ver_4, "ThreadPoolExecutor (GIL)")