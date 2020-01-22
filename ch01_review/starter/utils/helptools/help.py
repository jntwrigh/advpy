import io
import sys
import importlib


def list_module_contents(module_name):
    """
        This function will become a generator that yields one module top-level item at a time.
        Follow these steps to help create it:

        Step 1. load the desired module dynamically using importlib.import_module(name)

        Step 2. Create a StringIO buffer that works like a file.  Iterate over the results of a dir()
                command, passing the name of the module into it.

        Step 3. Send the output of the dir(module_name) command to the string buffer using the
                print statement's keyword argument: file=

        Step 4. Obtain the contents of the string buffer using buf.getvalue().

        Step 5. Yield one item from the buffer at a time.  Note: you may have to use split('\n')
                since getvalue() returns one long string of items separated by newlines.
    """
