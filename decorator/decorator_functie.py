import time
import math
from datetime import datetime
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.time()
        output = func(*args, **kwargs)
        end = time.time()

        print("Total time taken in:", func.__name__, end - begin)
        return output

    return wrapper

def log_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().timestamp()

        output = func(*args, **kwargs)

        with open("log_decorator.txt", "a") as fp:
            fp.write(
                f"[{timestamp}]: function '{func.__name__}' returned {output}\n"
            )

        return output

    return wrapper


def accepts(data_type):
    def wrap(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, data_type):
                    raise Exception(
                        f"Invalid parameter {arg} for function {func.__name__}"
                    )

            for value in kwargs.values():
                if not isinstance(value, data_type):
                    raise Exception(
                        f"Invalid parameter {value} for function {func.__name__}"
                    )

            return func(*args, **kwargs)

        return wrapper

    return wrap


def returns(data_type):
    def wrap(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            output = func(*args, **kwargs)

            if not isinstance(output, data_type):
                raise Exception(
                    f"The function {func.__name__} returned {type(output)} instead of {data_type}"
                )

            return output

        return wrapper

    return wrap



@accepts(int)
@returns(int)
@log_it
@time_it
def factorial(num):
    time.sleep(1)
    return math.factorial(num)



if __name__ == "__main__":
    for i in range(3, 11):
        print(f"factorial({i}) = {factorial(i)}")