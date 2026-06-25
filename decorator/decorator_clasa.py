import time
import math
from datetime import datetime
from functools import wraps


class Accepts:
    def __init__(self, data_type):
        self.data_type = data_type

    def __call__(self, f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, self.data_type):
                    raise Exception(f"Invalid parameter {arg} for {f.__name__}")

            for v in kwargs.values():
                if not isinstance(v, self.data_type):
                    raise Exception(f"Invalid parameter {v} for {f.__name__}")
            print(args[0],"Accepted")
            return f(*args, **kwargs)
        return wrapped


class Returns:
    def __init__(self, data_type):
        self.data_type = data_type

    def __call__(self, f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            output = f(*args, **kwargs)
            if not isinstance(output, self.data_type):
                raise Exception(
                    f"{f.__name__} returned {type(output)} instead of {self.data_type}"
                )
            print(args[0],"Returned")
            return output
        return wrapped


class TimeIt:
    def __call__(self, f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            start = time.time()
            out = f(*args, **kwargs)
            end = time.time()
            print("Time:", f.__name__, end - start)
            return out
        return wrapped


class LogIt:
    def __call__(self, f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            ts = datetime.now().timestamp()
            out = f(*args, **kwargs)

            with open("log_decorator.txt", "a") as fp:
                fp.write(f"[{ts}] {f.__name__} -> {out}\n")

            return out
        return wrapped


@Accepts(int)
@Returns(int)
@LogIt()
@TimeIt()
def factorial(num):
    time.sleep(1)
    return math.factorial(num)


if __name__ == "__main__":
    for i in range(3, 11):
        print(factorial(i))