import fnmatch
import os
import shelve


for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '*.py'):
        print(filename)


shelve_data = '/temp/shelve_it.dat'
with shelve.open(shelve_data) as sh:
    sh['Bob'] = ['221 Eastbrook Ave.', 'Denver', 'CO', '80101']

print(sh['Bob'])        # ValueError, shelve is closed

with shelve.open(shelve_data) as sh:
    print(sh['Bob'])
