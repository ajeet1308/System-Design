"""
Encapsulation

Encapsulation is the process of hiding the internal state of an object and requiring all interactions to be performed through an object's methods.

Use Case:
- Provides better control over data.
- Prevents accidental modification of data.
- Promotes modular programming.

Working:
- Data Hiding
- Access through Methods
- Control and Security

"""

import traceback
from abc import ABC, abstractmethod


# Interface
class BankAccountInterface(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass
    
    @abstractmethod
    def set_balance(self, amount):
        pass

class BankAccount(BankAccountInterface):
    def __init__(self, owner, balance=0):
        self.owner = owner # Public attribute
        self.__balance = balance # Private attribute
    
    def deposit(self, amount):
        try:
            if amount > 0:
                self.__balance += amount
                print(f"Deposited {amount} to {self.owner}'s account.\n New balance: {self.__balance}")
            else:
                print("Invalid deposit amount.")
        except Exception as e:
            print(f"Error depositing amount: {traceback.format_exc()}")
    
    def withdraw(self, amount):
        try:
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount} from {self.owner}'s account.\n New balance: {self.__balance}")
            else:
                print("Invalid withdrawal amount or insufficient balance.")
        except Exception as e:
            print(f"Error withdrawing amount: {traceback.format_exc()}")
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        try:
            if amount > 0:
                self.__balance = amount
            else:
                print("Invalid balance amount.")
        except Exception as e:
            print(f"Error setting balance: {traceback.format_exc()}")

if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Current balance: {account.get_balance()}")
