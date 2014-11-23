import signal
import functools
import time


class TimeoutError(Exception):
    pass


def timeout(seconds, default_value):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError()

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, seconds, 0)
            try:
                result = func(*args, **kwargs)
            except TimeoutError:
                return default_value
            finally:
                signal.alarm(0)
            return result

        return functools.wraps(func)(wrapper)

    return decorated


@timeout(seconds=0.2, default_value=2)
def slow_function():
    time.sleep(0.3)
    return False

print slow_function()
