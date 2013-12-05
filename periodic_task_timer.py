import threading
import time

def periodic(periodic_time):
    def wrap(func):
        def event(*args, **kwargs):
            func(*args, **kwargs)
            threading.Timer(periodic_time, event, list(*args), **kwargs).start()
        return event
    return wrap

@periodic(2)
def foo(num, a=1):
    print num, a

foo(9)
foo(0)

#threading.Timer(2, foo, (9,)).start()
