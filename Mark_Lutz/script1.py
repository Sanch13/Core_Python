import sys

print(sys.version)
# print(2**32)
# x = "Spam!"
# print(x*8)

s ='spam'
raw = open('data.txt', 'rb').read()
print(raw, len(raw))

d1 = {'a': 1, 'b': 2, 'c': 3,}
d2 = {'a': 1, 'b': 2, 'c': 3, 'd': 5}
b = 4
a = 3
print(b / (2.0 + a))