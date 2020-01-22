import hashlib

print('{0}'.format(hashlib.algorithms_available))
print('{0}'.format(hashlib.algorithms_guaranteed))

data_bytes = b'Very important message.'
hash_md5 = hashlib.md5(data_bytes)
hash_sha1 = hashlib.sha1(data_bytes)
hash_sha512 = hashlib.sha512(data_bytes)
print(hash_md5.hexdigest())
print(hash_sha1.hexdigest())
print(hash_sha512.hexdigest())


import uuid

def hash_pswd(pswd):
    salt = uuid.uuid4().hex
    hash = hashlib.sha256(salt.encode() + pswd.encode()).hexdigest()
    return '{0}:{1}'.format(salt, hash)


def verify_pswd(hashed_pswd, user_pswd):
    salt, hash = 0, 0
    try:
        salt, hash = hashed_pswd.split(':')
    except:
        pass
    return hash == hashlib.sha256(salt.encode() + user_pswd.encode()).hexdigest()
 
user_pswd = input('Enter a password: ')
hashed_password = hash_pswd(user_pswd)
print('Hashed password is: {0}'.format(hashed_password))

repeat_pass = input('Enter password again to verify it: ')
if verify_pswd(hashed_password, repeat_pass):
    print('Password is correct.')
else:
    print('Passwords do not match.')


# hashing any file
filename = '14_using_hashlib.py'
block = 65536
hash_val = hashlib.md5()
with open(filename, 'rb') as f:
    data = f.read(block)
    while len(data) > 0:
        hash_val.update(data)
        data = f.read(block)
print('Hashed file value: '.format(hash_val.hexdigest()))