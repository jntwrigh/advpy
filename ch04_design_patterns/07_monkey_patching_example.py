import os
import sys

patched_items = {}


def patch(module, attr, newitem):
    default = object()
    olditem = getattr(module, attr, default)
    if olditem is not default:
        patched_items[(module, attr)] = olditem
    setattr(module, attr, newitem)


def unpatch(module, attr):
    default = object()
    olditem = getattr(module, attr, default)
    if olditem is default:
        return olditem
    old = patched_items[(module, attr)]
    setattr(module, attr, old)


def get_files(dirname):
    return os.listdir(dirname)


def listdir_patch(dirname):
    return ['no files found']


patch(os, 'listdir', listdir_patch)
print(get_files('.'))

unpatch(os, 'listdir')
print(get_files('.'))

patch(sys, 'path', 'hello!')
print(sys.path)
unpatch(sys, 'path')
print(sys.path)
