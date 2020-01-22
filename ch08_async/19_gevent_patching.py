import time

def task(id):
    print('Performing task {0}'.format(id))
    time.sleep(2)


t = time.time()
for i in range(3):
    task(i)
print('Elapsed {0:.1f} sec.'.format(time.time() - t))


import gevent.monkey
import gevent.pool

pool = gevent.pool.Pool(3)

gevent.monkey.patch_all()
t = time.time()
for i in range(3):
    pool.spawn(task, i)

pool.join()

print('Elapsed {0:.1f} sec.'.format(time.time() - t))
