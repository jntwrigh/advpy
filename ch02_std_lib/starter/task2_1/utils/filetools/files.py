import hashlib
import os


def find_dups(directory: str, alg: str='md5') -> list:
    block_size = 65536
    mod = hashlib
    hashed_files = {}                                               # dict contains filename, hash_value entries
    dups = []                                                       # stores duplicate file names

    # Step 1. Invoke the specific module method for the algorithm passed in
    #         Note: you can use f = getattr(obj, 'name') which returns obj.name


    # Step 2. Iterate over the directory, invoke the hashlib module's hash function
    #         (i.e. md5(), sha1(), etc...)


    # Step 3. For each file in the directory, open it, read from it (a block)
    #         and update the hash_value each time.
    #         Read the next block.  A 'with' control works for reading from
    #         the file.


    # Step 4. Once the hash value is calculated, add it to the hashed_files
    #         dictionary with the filename as the key and hash as the value


    # Step 5. find the duplicated hashes in the dictionary.  One approach is
    #         to get the dictionary's values and count their occurrences.  The
    #         list type has a count() function.  To convert the dictionary values
    #         to a list, pass it into the list constructor:
    #                         new_list = list(dictionary.values())


    # Step 6. Check the count for each hash, if it is greater than 1 then there is
    #         a duplicate.  Iterate over the dictionary of hashes and see which files
    #         have that hash value.  Add them to a list.

    # Step 7. Add the list of duplicate files to a master list (dups).  Return
    #         dups from the function

