"""
    Shows argparse module usage.

    Usage 20_argparse.py -n my_box1 -w 3 -t 3 -d 3 --volume --colors blue orange

"""
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Gets box information')
    parser.add_argument('-n', '--name', help='Box name')
    parser.add_argument('-w', '--width', help='Box width', default=0, type=int)
    parser.add_argument('-t', '--height', help='Box height', default=0, type=int)
    parser.add_argument('-d', '--depth', help='Box depth', default=0, type=int)
    parser.add_argument('-m', '--metric', default=True, help='Is this in metric units', action='store_true')
    parser.add_argument('-c', '--colors', help='Colors of the box', nargs='*')

    mutual_group = parser.add_mutually_exclusive_group()
    mutual_group.add_argument('-v', '--volume', action='store_true')
    mutual_group.add_argument('-s', '--surface_area', action='store_true')
    args = parser.parse_args()
    return args


print(get_args())
