import time


def snooze():
	time.sleep(1)


class TimeContextManager:

	def __enter__(self):
		self.time_start = time.time()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		time_end = time.time()
		print(f"{(time_end - self.time_start):.4f} sec")


with TimeContextManager():
	snooze()

#  1.0155 sec