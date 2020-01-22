class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{nm} (age:{age})'.format(nm=self.name, age=self.age)


class Employee(Person):
    def __init__(self, name, age, salary, dept):
        Person.__init__(self, name, age)
        self.salary = salary
        self.dept = dept

    def __str__(self):
        p_str = Person.__str__(self)
        return '{pers} Sal: {sal} Dept: {dept}'.format(pers=p_str, sal=self.salary, dept=self.dept)


class Commissioned:
    def __init__(self, rate):
        self.comm_rate = rate

    def __str__(self):
        return 'Rt: {comm_rate}'.format(comm_rate=self.comm_rate)


class Salesperson(Employee, Commissioned):
    def __init__(self, name, age, salary, region, dept='Sales', rate=0.02):
        Employee.__init__(self, name, age, salary, dept)
        Commissioned.__init__(self, rate)
        self.region = region

    def __str__(self):
        emp_str = Employee.__str__(self)
        comm_str = Commissioned.__str__(self)
        return '{emp}, {comm} - Reg: {reg}'.format(emp=emp_str, comm=comm_str, reg=self.region)

s = Salesperson('William', 37, 99275.00, 'Northeast')
print(s)