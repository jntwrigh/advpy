import argparse

from ch01_review.solution.utils import list_module_contents, list_module_alternate


def get_module_name():
    """
        Retrieves command line arguments.  The only argument that
        should be provided will be the name of a module.
        (e.g. python task1_1.py sys)

        :return: the arguments object containing a mod_name attribute
    """
    parser = argparse.ArgumentParser(description='Module Help Utility')
    parser.add_argument('mod_name', help='Module name to load (do not include .py extension)')
    args = parser.parse_args()
    return args.mod_name


module_name = get_module_name()

for item in list_module_contents(module_name):
    print(item)


# using the alternate method provided in help.py (not a part of the exercise)
for item in list_module_alternate(module_name):
    print(item)
