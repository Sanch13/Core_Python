import sys

from colorama import Fore, Back, Style, init
# Инициализация для Windows (если требуется)
init()

answer = sys.stdout.write(Fore.GREEN + "Hello World!\n")
text = input(Fore.CYAN + "Enter your name: ")


answer_txt = sys.stdout.write(Fore.BLUE + f"Your name is {text}\n")


if __name__ == '__main__':
    sys.exit(0)
