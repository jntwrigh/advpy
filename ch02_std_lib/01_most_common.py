"""
    01_most_common.py   -   retrieving the most common item: 3 ways
"""

data = [1, 2, 3, 4, 5, 3, 1, 5, 2, 1, 5, 3, 4, 2, 5]

# technique 1   -    use of Counter
from collections import Counter
print('(Technique 1) Most abstract value: {0} with {1} occurrences.'.format(*Counter(data).most_common(1)[0]))

# technique 2   -    manually populating a dict
occurs = {}
for val in data:
    if val not in occurs.keys():
        occurs[val] = 1
    else:
        occurs[val] += 1

most_common = sorted(occurs.items(), key=lambda x: x[1], reverse=True)
print('(Technique 2) Most abstract value: {0} with {1} occurrences.'.format(*most_common[0]))

# technique 3   - using a default dict
from collections import defaultdict
occurs = defaultdict(int)
for val in data:
    occurs[val] += 1
most_common = sorted(occurs.items(), key=lambda pair: pair[1], reverse=True)
print('(Technique 3) Most abstract value: {0} with {1} occurrences.'.format(*most_common[0]))

