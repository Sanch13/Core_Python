from invoke import task


"""$ pip install invoke
Одним из вариантов использования пакета invoke является возможность сделать
функции доступными в качестве аргументов командной строки. Давайте создадим
файл tasks.py, который содержит строки, показанные в пример
(Аргумент ctx — первый аргумент для каждой преобразуемой функции, но используется он только самим
 пакетом invoke. Неважно, с каким именем, но этот аргумент там должен быть.)
$ invoke mytime
Local time is Thu May 2 13:16:23 2019

"""

@task
def mytime(ctx):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print("Local time is", time_str)
