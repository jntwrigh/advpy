import functools


months = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}


abbr_iter = map(lambda mo: mo[:3], months)
results = list(abbr_iter)
print(results)


reduced = functools.reduce(lambda mo1, mo2: '{0} {1}'.format(mo1, mo2), results)
print(reduced)


no_ber_months = filter(lambda mo: mo[-3:] != 'ber', months)
results = list(no_ber_months)
print(results)


print(any([mo < 29 for mo in months.values()]))
print(all([mo > 29 for mo in months.values()]))

f = open('../resources/alice.txt', encoding='utf-8-sig')
ge = (line.strip() for line in f if len(line) > 1)
for line in ge:
    print(line)
