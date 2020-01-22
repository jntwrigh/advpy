class LastDay:
    def __init__(self):
        self.count = 0
        self.last_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __next__(self):
        if self.count >= len(self.last_days):
            raise StopIteration
        val = self.last_days[self.count]
        self.count += 1
        return val

    def __iter__(self):
        self.count = 0
        return self

lastday1 = LastDay()
for day in lastday1:
    print(day, end=' ')
    if day == 28:
        break
print(end='\n')

for day in lastday1:
    print(day, end=' ')
    if day == 30:
        break
print(end='\n')

lastday2 = LastDay()
for day in lastday1:
    print(day)
    for day2 in lastday2:
        print(day2, end=' ')
    print(end='\n')
