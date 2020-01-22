import filecmp

file1 = './sample_files/dir1/sample_file1.txt'
file2 = './sample_files/dir2/sample_file1.txt'

dir1 = 'sample_files/dir1'
dir2 = 'sample_files/dir2'

print(filecmp.cmp(file1, file2))
print(filecmp.cmp(file1, file2, shallow=False))

results = filecmp.dircmp(dir1, dir2)
results.report()

print('Left only:  ', results.left_only)
print('In Common:  ', results.common)
print('Right only: ', results.right_only)
