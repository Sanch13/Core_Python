from timeit import timeit
import time


def snooze():
	time.sleep(1)


run_time = timeit('snooze()', globals=globals(), number=1)
print(f'Function run time is equals : {run_time:.4f} sec')
# Function run time is equals : 1.0011 sec
