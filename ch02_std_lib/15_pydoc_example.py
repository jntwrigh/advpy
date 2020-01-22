"""
    15_pydoc_example.py

    Documentation for pydoc should be placed in 3 double quoted strings at various locations
    shown here.  These are called docstrings.
    Use:
                pydoc -w module_name  (or python -m pydoc -w module_name)

    to generate documentation.
"""

class Example:
    """
        Example is a sample class used to demonstrate placement of a docstring
    """
    def __init__(self, name):
        """
            Define methods, such as this one, which contains docstrings to
            describe the method.

            :param name: A name parameter passed in.
            :return: return value if any (none in this case)
        """
        self.name = name


def sample(value):
    """
        Documentation for standard functions are placed here
    """
    print(value)


if __name__ == '__main__':
    f = Example('Sam')
    sample(42)
