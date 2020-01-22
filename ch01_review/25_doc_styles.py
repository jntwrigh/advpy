"""
    03_main_styles.py -  This source file shows different documentation styles
                        generally accepted within Python source files.

                        A popular tool for generating documentation is called Sphinx.
                        It must be installed and then can be run from the command line:

                        To set the documentation style within PyCharm, select:
                        File > Settings > Tools > Python Integrated Tools
                        and then select the docstring format.

                        $ pip install sphinx
                        $ sphinx-quickstart
"""


def plain_doc_style(arg1, arg2):
    """

    """
    return [arg1, arg2]


def reStructuredText_style(arg1, arg2):
    """
    This is the reST style.  It is the PyCharm default.
    The tool called Sphinx can use generate docs based on this format.
    It supports HTML and LaTeX formats.  rst uses shortened formats
    to display HTML, such as:
    *italics*
    **bold**
    - bullets


    :param arg1: this is the first argument
    :type arg1: int
    :param arg2: this is the second argument
    :type arg2:
    :return: the list of input arguments
    :rtype: list
    """
    return [arg1, arg2]


def google_doc_style(arg1, arg2):
    """This function illustrates the Google documentation style (Summary line)

    The first line is the summary, with perhaps additional description here.

    Args:
        arg1 (int): A value to be processed
        arg2 (str): The name of the process being performed

    Returns:
        list: the results are captured in a list for safe keeping

    """
    return [arg1, arg2]


def numpy_style(arg1, arg2):
    """The function illustrates the NumPy style of documentation (Summary line)

    This is the NumPy version of documentation (full description).

    Parameters
    ----------
    arg1 : int
        A value to be processed
    arg2 : str
        The name of the process being performed
    Returns
    -------
    list
        The results of the operations performed
    """
    return [arg1, arg2]


def epytext_style(arg1, arg2):
    """
    This is the epytext style.  It is designed to look like Javadoc
    documentation style.


    @param arg1: this is the first argument
    @type arg1: int
    @param arg2: this is the second argument
    @type arg2: str
    @return: list of input arguments
    @rtype: list
    """
    return None


