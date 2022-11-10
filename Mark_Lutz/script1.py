import sys


def func():
    x = "Spam!"
    return x * 8

# while True:
#     reply = input('Enter text: ')
#     if reply == 'stop': break
#     elif not reply.isdigit():
#         print('Bad!'*8)
#     else:
#         print(int(reply)**2)
# print('Bye')

# while True:
#     reply = input('Enter text: ')
#     if reply == 'stop': break
#     try:
#         num = int(reply)
#     except:
#         print('Bad! ' * 8)
#     else:
#         print(num ** 2)
# print('Bye')


print(func(), file=open(r'D:\Python39\Core_Python\txt.txt', 'a'))
