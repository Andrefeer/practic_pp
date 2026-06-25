# Py366 (Procesare Colecții Concurente): „Să se scrie un program Python (utilizând threading) care procesează simultan utilizând
# mai multe thread-uri un hashmap X și un dicționar Y cu formula f(x,y)=(x*y, y+1) iar rezultatul este depus în Y.
# Dicționarul are pereche de valoare și index i. Se va utiliza lock().”

import threading


X = {0: 2, 1: 3, 2: 4, 3: 5}
Y = {0: 10, 1: 20, 2: 30, 3: 40}

lock = threading.Lock()


def f(x, y):
    return x * y, y + 1


# 🔹 worker thread
def worker(indexes):
    global X, Y

    for i in indexes:
        x = X[i]

        with lock:
            y = Y[i]
            new_x, new_y = f(x, y)
            Y[new_y] = new_x

        print(f"Thread {threading.current_thread().name} -> i={i}, result={new_x}, new_y={new_y}")



keys = list(X.keys())
mid = len(keys) // 2

t1 = threading.Thread(target=worker, args=(keys[:mid],))
t2 = threading.Thread(target=worker, args=(keys[mid:],))

t1.start()
t2.start()

t1.join()
t2.join()

print("\nFinal Y:", Y)