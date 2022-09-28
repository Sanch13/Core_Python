import gevent
from gevent import socket


hosts = ['www.bplelektro.by', 'www.context.reverso.net']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
print(gevent.spawn(gevent.socket.gethostbyname, 'www.context.reverso.net'))
print(gevent.socket.gethostbyname('www.bplelektro.by'))