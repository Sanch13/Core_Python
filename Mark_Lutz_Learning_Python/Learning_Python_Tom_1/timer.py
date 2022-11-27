from timeit import timeit

reps = 10000
repslist = list(range(reps))


def forloop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res


def listcopm():
    return [abs(x) for x in repslist]


def mapcall():
    return list(map(abs, repslist))


def genexp():
    return [abs(x) for x in repslist]


def genfunc():
    def gen():
        for x in repslist:
            yield x
    return list(gen())


l = []
for test in (forloop, listcopm, mapcall, genexp, genfunc):
    # print(timeit(f'{test.__name__}()', globals=globals(), number=100), f'-> {test.__name__}')
    l.append(f'{test.__name__}-> '+str(timeit(f'{test.__name__}()', globals=globals(), number=100)))
# l = sorted(l[1])
# m = [ for a,b in l]
print(*l, sep='\n')