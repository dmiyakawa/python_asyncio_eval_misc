import gevent
import gevent.socket

hosts = ['www.crappytaxidermy.com',
         'www.walterpottertaxidermy.com',
         'www.nonexistent.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
