"""
    help.py
    This module contains a generator function that can be iterated over to retrieve
    the top level items of a module
"""
import io
import importlib


def list_module_contents(module_name):
    """
        This generator accepts a module name and yields the results of the dir() command.

        :param module_name: str name of a module (e.g. 'os' or 'sys')
        :return: yields a string representing one top-level module item
    """
    mod = importlib.import_module(module_name)
    dir_buf = io.StringIO()

    for mod_entry in dir(mod):
        print(mod_entry, file=dir_buf)

    for item in dir_buf.getvalue().split('\n'):
        yield item


def list_module_alternate(module_name):
    """
        This version provides another way to perform our task, although it does not
        follow the task instructions exactly as written.  It uses the vars() function,
        which is equivalent to object.__dict__.

        We can supply the name of the module to return the top-level entries this way.

        :param module_name: str name of a module (e.g. 'os' or 'sys')
        :return: yields a string representing one top-level module item
    """
    mod = importlib.import_module(module_name)
    for attr in vars(mod):
        yield attr
