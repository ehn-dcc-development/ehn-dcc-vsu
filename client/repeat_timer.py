"""
https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds

Client usage:

 def my_func():
    print("abc")

rep_timer = RepeatTimer(1, my_func)
rep_timer.start()
time.sleep(5)   # NOTE: sleep from time package
rep_timer.cancel()

prints 4 x "abc"

"""

from threading import Timer


class RepeatTimer(Timer):
    def run(self) -> None:
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
