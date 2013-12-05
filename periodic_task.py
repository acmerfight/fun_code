#coding=utf-8
import sched, time
from functools import partial

def periodic(delay_time, start_time=time.time()):
    def wrap(func):
        def event(start_time, *args, **kwargs):
            if time.time() > start_time:
                func(*args, **kwargs)
            params = tuple([start_time + delay_time] + list(args))
            scheduler.enterabs(start_time + delay_time, 1, event, params, **kwargs)
            scheduler.run()
        scheduler = sched.scheduler(time.time, time.sleep)
        return partial(event, start_time)
    return wrap

# params delay_time and start_time
@periodic(2)
def foo(num, a=1):
    print num, a

foo(9)
