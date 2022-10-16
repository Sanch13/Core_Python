import time


def decorator(func):
	def wrapper(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()
		print(f"Run time is : {end_time - start_time:.4f} sec")	 # Run time is : 1.0011 sec
		return result
	return wrapper


@decorator
def snooze():
	time.sleep(1)


snooze()
