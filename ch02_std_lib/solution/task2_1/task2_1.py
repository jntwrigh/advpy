import timeit
from ch02_std_lib.solution.task2_1.utils import find_dups

algorithm = ['md5', 'sha1', 'sha512']
file_dir = '../../task2_1_files'
number_loops = 5000
repeat_times = 3

print(find_dups(file_dir))

#comparing with timeit
for alg in algorithm:
    t = timeit.Timer(stmt='find_dups(file_dir, alg)', setup='from __main__ import find_dups, file_dir, alg')
    print('{0} {1} loops repeated {2} times: {3}'.format(alg, number_loops, repeat_times, t.repeat(repeat=3, number=number_loops)))
