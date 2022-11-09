import sys

print(sys.version)
print(2 ** 32)
x = "Spam!"
print(x * 8)

# while True:
#     reply = input('Enter text: ')
#     if reply == 'stop': break
#     elif not reply.isdigit():
#         print('Bad!'*8)
#     else:
#         print(int(reply)**2)
# print('Bye')

while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('Bad! ' * 8)
    else:
        print(num ** 2)
print('Bye')
