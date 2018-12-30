from abc import ABCMeta, abstractmethod

class Account(metaclass = ABCMeta):

    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def displayBalance():
        return 0




class SavingAccount:
    def __init__(self):
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        pass

    def authenticate(self, name, accountNumber):
        pass

    def withdraw(self, withdrawalAmount):
        pass

    def deposit(self, depositAmount):
        pass

    def displayBalance(self):
        pass


