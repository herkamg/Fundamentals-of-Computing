import time

class TimerError(Exception):
    """ A custom exception used to report errors in use of timer class """


class Timer:
    def __init__(self):
        self._start_time = None
    
    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")
        self._start_time = time.perf_counter()
    
    def stop(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start()  to start it")
        
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        print(f"elapsed time: {elapsed_time:0.4f} seconds")


# counter ticks
counter = 0
# Timer handler
def ticks():
    global counter
    print(counter)
    counter +=1

t = Timer()
t.start()
n =10000
while(n >0):
    n -= 1

t.stop()
