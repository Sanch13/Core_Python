from datetime import datetime
from pprint import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, "%H:%M").strftime("%I:%M%p")


with open("csv.csv") as file:
    # d = {line.strip().split(",")[0]: line.strip().split(",")[1] for line in file}
    d = {}
    for line in file:
        k, v = line.strip().split(",")
        print(k, v)
        if v not in d:
            d.setdefault(v.capitalize(), []).append(convert2ampm(k))
        else:
            d.get(v).append(convert2ampm(k))

pprint(d)
