import platform
import sys


try:
    from typing import Dict
except ImportError:
    print('Requires 3.5 or later.')
    print(f'Using Python version: {platform.python_version()}')   # '{}.{}.{}'.format(sys.version_info[:3])
    sys.exit()

Definition = Dict[str, str]


def read_data(filename: str):

    words: Definition = {}

    try:
        with open(filename, encoding='utf8') as in_val:
            for line in in_val:
                try:
                    word, definition = line.split(maxsplit=1)
                    words[word] = definition
                except ValueError:
                    pass
    except IOError as err:
        print('Error reading from file.', err)
        sys.exit()

    return words


data = read_data('../resources/dictionary.txt')

# this would not be allowed due to the typing defined above, but at runtime
# python doesn't do anything to stop this
data[10] = 20
