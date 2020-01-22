import inspect
import random
import time


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


task1()
task2()
task3()
