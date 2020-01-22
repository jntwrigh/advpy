import inspect
import random
import time
from threading import Thread
from queue import Empty, Queue


def perform_task():
    sleep_time = random.randint(1, 4)
    callee = inspect.stack()[0][3]
    caller = inspect.stack()[1][3]
    print(f'{callee} called by {caller} starting')
    time.sleep(sleep_time)
    print(f'{callee} called by {caller} ending')


def task1():
    perform_task()


def task2():
    perform_task()


def task3():
    perform_task()


class ThreadPool(object):
    def __init__(self, Worker, num_threads=3):
        self.job_queue = Queue()
        self.thr_pool = []
        for i in range(num_threads):
            th = Worker(self.job_queue)
            self.thr_pool.append(th)
            th.start()

    def add_job(self, job):
        self.job_queue.put(job)

    def end_pool(self):
        for th in self.thr_pool:
            self.job_queue.put('TERMINATE')

        for th in self.thr_pool:
            th.join()


class Worker(Thread):
    def __init__(self, job_queue):
        super().__init__()
        self.job_queue = job_queue

    def run(self):
        print(f'{self.getName()} ended')
        while True:
            try:
                job = self.job_queue.get()
                if type(job) == str and job == 'TERMINATE':
                    break
                job()
                time.sleep(0.1)
            except Empty:
                continue
        print(f'{self.getName()} ended')


pool = ThreadPool(Worker)
pool.add_job(task1)
pool.add_job(task2)
pool.add_job(task3)
pool.end_pool()
