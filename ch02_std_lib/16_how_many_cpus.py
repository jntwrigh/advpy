import os
import subprocess

def count_cpus():
    """
        # CPUs on a system...
    """

    if hasattr(os, 'sysconf'):                                                          # unix, linux
        if os.sysconf_names.get('SC_NPROCESSORS_ONLN'):
            return os.sysconf('SC_NPROCESSORS_ONLN')
        else:                                                                           # osx:
            return int(subprocess.Popen('sysctl -n hw.ncpu').communicate()[0])

    return os.environ.get('NUMBER_OF_PROCESSORS', 'unknown')                            # Windows:

print(count_cpus())