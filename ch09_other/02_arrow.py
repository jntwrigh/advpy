"""
        02_arrow.py

        Uses the 3rd Party tool: arrow.  To use this module:
            pip install arrow

"""

import arrow

utc = arrow.utcnow()
my_now = arrow.now()
my_now_pacific = arrow.now('US/Pacific')

print(utc)
print(my_now)
print(my_now_pacific)

print(my_now.format())
print(my_now.format('MMM/DD/YY'))
print(my_now.humanize())

print(my_now.year)
print(my_now.day)
print(my_now.month)

some_date = arrow.get('2020-05-08 22:05:48', 'YYYY-MM-DD HH:mm:ss')
print(some_date.format('MMM/DD/YY'))
print(some_date.humanize())

extract_date = arrow.get('May I go on a march in November, 2021.', 'MMMM, YYYY')
print(extract_date.format('MMMM, YYYY'))
