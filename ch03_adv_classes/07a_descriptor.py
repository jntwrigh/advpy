class FullName:

    def __get__(self, instance, owner):
        return ' '.join([instance.first, instance.last])

    def __set__(self, instance, new_name):
        names = new_name.split(' ')
        if len(names) == 1:
            first = ''
            last = new_name
        else:
            first = names[0]
            last = ' '.join(names[1:])
        instance.first = first
        instance.last = last


class Person:

    full_name = FullName()

    def __init__(self, first='', last=''):
        self.first = first
        self.last = last


p1 = Person('John', 'Smith')
p2 = Person('Sally','Jones')
p3 = Person('Fred', 'Davis')
print(p1.full_name)
p2.full_name = 'Sally Van Wilder'
print(p2.full_name)
p3.full_name = 'Freddy Davis'
print(p3.full_name)
