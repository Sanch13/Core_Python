import multiprocessing
import os
import time
import random


# def whoami(what):
#     print("Process %s says: %s" % (os.getpid(), what))
#
#
# if __name__ == "__main__":
#     whoami("I'm the main program")
#     for n in range(4):
#         p = multiprocessing.Process(target=whoami, args=("I'm function %s" % n,))
#         p.start()


def says():
    wait = random.random()
    time.sleep(wait)
    print(f"I have been waiting {wait:.03} second and local time {time.strftime('%H:%M:%S')}")


if __name__ == "__main__":
    for n in range(3):
        p = multiprocessing.Process(target=says)
        p.start()