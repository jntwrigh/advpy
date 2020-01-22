import errno
import functools
from itertools import islice


def advance(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        co = f(*args, **kwargs)
        next(co)
        return co
    return wrapper


@advance
def splice_files(write_filename, num_lines=10):
    try:
        with open(write_filename, mode='w', encoding='utf-8') as f_out:

            while True:
                read_filename = (yield)
                try:
                    with open(read_filename, encoding='utf-8-sig') as f_in:
                        lines = list(islice(f_in, num_lines))
                        f_out.writelines(lines)
                except IOError as err:
                    if err.args[0] == errno.ENOENT:     # no such file or directory error
                        print('{0} not found--not merged'.format(read_filename))

    except IOError:
        print('Error with file to write to.')


splicer = splice_files('temp.txt')
splicer.send('../resources/alice.txt')
splicer.send('../resources/iliad.txt')
splicer.send('NOT_REAL')
splicer.send('../resources/poe.txt')
