
import signal
import time

def handle_it(signal, frame):
    print("Called with", signal)
    raise Exception("HELP ME!!!")

signal.signal(signal.SIGHUP, handle_it)

while True:
    print("waiting...")
    time.sleep(1)

