"""
        files.py -      Provides the copy_files() function which returns a
                        list of duplicate files.
"""
import filecmp
import os
import shutil


def copy_files(src, dst):
    """
    This function copies files from src to dst.

    :param src: Directory of files to be copied (string)
    :param dst: Directory for destination of files (string)
    :return: The files that were copied (list)
    """

    # Step 1. Check that dst directory exists first.  Use os.path.exists()
    #         for this.  If it does not exist, use os.makedirs(dst) to create it.

    # Step 2. Compare the two directories.  The files on the left_only
    #         should be copied to the destination directory.

    # Step 3. Iterate over the list of files returned from step 2.
    #         Use os.path.join() to join the filename and src directory
    #         and use shutil's copy2() function to copy files.

