# todos = open("todos.txt", "a", encoding="utf-8")
# print("ToDo 1", file=todos)
# print("ToDo 2", file=todos)
# print("ToDo 3", file=todos)
# todos.close()


tasks = open("todos.txt")
for line in tasks:
    print(line, end='')
tasks.close()


