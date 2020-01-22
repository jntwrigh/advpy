class Account(object):
    fee = 10


class CheckingAccount(Account):
    fee = 15


class SavingsAccount(Account):
    fee = 5


class BusinessCheckingAccount(CheckingAccount):
    fee = 20


class BusinessSavingsAccount(SavingsAccount):
    fee = 17


class MyAccount(BusinessSavingsAccount, BusinessCheckingAccount):
    pass


a = MyAccount()
print(a.fee)

del BusinessSavingsAccount.fee
print(a.fee)

del SavingsAccount.fee
print(a.fee)

print(MyAccount.__mro__)
print(MyAccount.mro())