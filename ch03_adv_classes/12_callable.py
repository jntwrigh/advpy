import datetime


class Today(object):
    def __init__(self, fmt='%b %d, %Y'):
        self.fmt = fmt

    def now(self):
        return datetime.date.today().strftime(self.fmt)

    __call__ = now

t = Today()
print(t())
print(t.now())
print(Today('%m-%d-%y')())
