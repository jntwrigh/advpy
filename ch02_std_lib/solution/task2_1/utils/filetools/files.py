"""
        files.py -      Provides the find_dups() function which returns a
                        list of duplicate files.
"""

import hashlib
import os


def find_dups(directory: str, alg: str='md5') -> list:
    """
        Accepts a file system directory (as a string) and a hashing algorithm
        (e.g. 'md5', 'sha1', 'sha512', etc. as a string) and returns a list of
        lists containing duplicate files

        :param directory: The directory to search for similar files
        :param alg: a string representing the hashing algorithm chosen
        :return: list containing lists of duplicate filenames
    """
    block_size = 65536
    mod = hashlib
    hashed_files = {}                                               # dict contains filename, hash_value entries
    dups = []                                                       # stores duplicate file names
    hash_alg = getattr(mod, alg)                                    # getattr(hashlib, md5) for example
    for filename in os.listdir(directory):
        hash_val = hash_alg()
        with open(os.path.join(directory, filename), 'rb') as f:
            data = f.read(block_size)
            while len(data) > 0:
                hash_val.update(data)
                data = f.read(block_size)
        hashed_files[filename] = hash_val.hexdigest()               # create the dict with filename keys and hash values

    #find the duplicates
    hash_list = list(hashed_files.values())                         # we did this to use the count() function
    for hash_val in hash_list:
        if hash_list.count(hash_val) > 1:                           # if the hash value occurs more than once, then lets find the duplicates
            duplicates = []
            for filename in hashed_files:                           # create a list of the matching files
                if hash_val == hashed_files[filename]:
                    duplicates.append(filename)

            if duplicates not in dups:                              # add the duplicates to a master list
                dups.append(duplicates)
    return dups
