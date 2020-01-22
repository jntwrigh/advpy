from threading import Thread
import logging
from queue import Queue, Empty
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)


class WorkerThread(Thread):
    def __init__(self, task, req_queue, results_queue, name='WorkerThread', sentinel='TERMINATE', logging_on=False):
        super().__init__(name=name)
        self.task = task
        self.req_queue = req_queue
        self.results_queue = results_queue
        self.sentinel = sentinel
        self.level = logging.INFO if logging_on else logging.NOTSET

    def run(self):
        logger.log(self.level, '{0} starting'.format(self.name))
        while True:
            try:
                args = self.req_queue.get()
                logger.log(self.level, '{0} obtaining job: {1}'.format(self.name, args))
                if args[0] == self.sentinel:
                    break
                results = self.task(*args)
                self.results_queue.put(results)
                self.req_queue.task_done()
            except Empty:
                continue
        logger.log(self.level, '{0} ending'.format(self.name))


class ThreadPool(object):
    def __init__(self, task, Worker=WorkerThread, num_threads = 10, logging_on=False):
        """
        ThreadPool creates and manages a number of threads via a with control.
        Usage example:

        with ThreadPool(task):


        Args:
            task (function): a function that accepts any arguments and returns a result
            Worker (Thread): A thread class that overrides the default one provided.
                             Don't provide this unless a new run() method is needed.
            num_threads (int): The number of threads to create (def. = 10)
            logging_on (bool): Whether or not to display log output
        """
        self.sentinel = 'TERMINATE'
        self.thr_pool = []
        self.num_threads = num_threads
        self.req_queue = Queue()
        self.results_queue = Queue()
        self.task = task
        self.Worker = Worker
        self.logging_on = logging_on

    def __enter__(self):
        for i in range(self.num_threads):
            name = 'Thread {0}'.format(i)
            self.thr_pool.append(self.Worker(self.task, self.req_queue, self.results_queue, name, self.sentinel, self.logging_on))

        for th in self.thr_pool:
            th.start()

        return self.req_queue

    def __exit__(self, typ, val, tb):
        for th in self.thr_pool:
            self.req_queue.put((self.sentinel,))

        for th in self.thr_pool:
            th.join()

    def get_results(self):
        while not self.results_queue.empty():
            yield self.results_queue.get()
            self.results_queue.task_done()
