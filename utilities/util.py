import functools
import time


def profile_args(func):
    @functools.wraps(func)
    def checker(*args, **kwargs):
        print("< Arguments of %s were: %s, %s >" % (func.__name__, args, kwargs))
        return func(*args, **kwargs)

    return checker


def profile_time(func):
    @functools.wraps(func)
    def time_perf(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start
        print("< Function %s, took %s sec >" % (func.__name__, elapsed_time))
        return res

    return time_perf
