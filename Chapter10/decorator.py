import time


def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        return_value = func(*args, **kwargs)
        print("Calling {0} with {1} and {2}".format(
            func.__name__, args, kwargs))
        return return_value
    return wrapper


def print_something(func):
    def wrapper(*args, **kwargs):
        print(
            f"Doing something with {func.__name__} along with {args} and {kwargs}")

        return func(*args, **kwargs)
    return wrapper


@print_something
@log_calls
def test1(a, b, c):
    print("\ttest1 called")


@print_something
@log_calls
def test2(a, b):
    print("\ttest2 called")


@print_something
@log_calls
def test3(a, b):
    print("\ttest3 called")
    time.sleep(1)


# test1 = log_calls(test1)
# test2 = log_calls(test2)
# test3 = log_calls(test3)
test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)
