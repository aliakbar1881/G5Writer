import functools
import time

def sleep(_func=None, *, sleeping_time=2):
    def decorator(func):
        functools.wraps(func)
        def wraper(*args, **kwargs):
            time.sleep(2.0)
            output = func(*args, **kwargs)
            return output
        return wraper
    if _func is None:
        return decorator
    else:
        return decorator(_func)

