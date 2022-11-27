import gevent, socket
from gevent import socket


# hosts = ['www.bplelektro.by', 'www.context.reverso.net']
# jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
# gevent.joinall(jobs, timeout=5)
# for job in jobs:
#     print(job.value)
# print(gevent.spawn(gevent.socket.gethostbyname, 'www.context.reverso.net'))
# print(gevent.socket.gethostbyname('www.bplelektro.by'))
print(socket.gethostbyname_ex('www.bplelektro.by'))
# ('bplelektro.by', ['www.bplelektro.by'], ['85.209.148.102'])
print(socket.getaddrinfo('www.bplelektro.by', 80))
# [(<AddressFamily.AF_INET: 2>, 0, 0, '', ('85.209.148.102', 80))]
print(socket.getaddrinfo('www.bplelektro.by', 80, socket.AF_INET, socket.SOCK_STREAM))
# [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 0, '', ('85.209.148.102', 80))]
print(socket.getservbyname('http'))
print(socket.getservbyname('https'))


