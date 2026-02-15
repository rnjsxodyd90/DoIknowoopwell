class BankAccount:
    def __init__(self, owner, starting_balance):
        self.owner = owner
        # encapsulation: We hide the balance so it can't be changed directly.
        self.__balance = starting_balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" Added ${amount}. New balance: ${self.__balance}")
        else:
            print(" You can't deposit a negative amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f" Withdrew ${amount}. Remaining: ${self.__balance}")
        else:
            print(" Transaction declined: Insufficient funds or invalid amount")

    # Getter lets us see the balance without changing it directly.
    def get_balance(self):
        return f"Current balance for {self.owner}: ${self.__balance}"