# import Mark_Lutz.Learning_Python_Tom_1.work_import.b              # 1 way
# import Mark_Lutz.Learning_Python_Tom_1.work_import.b as b         # 2 way
from Mark_Lutz.Learning_Python_Tom_1.work_import.b import spam, x      # 3 way

# print(Mark_Lutz.Learning_Python_Tom_1.work_import.b.spam('gumby'))    # 1 way
# print(b.spam('Gumby'), end='')                        # 2 way
print(spam('Gumby'))                            # 3 way


def set_x(x: int):
    return x * 10


print()
new_x = set_x(x)
print(x)
print()
print(new_x)

