from abc import ABC, abstractmethod


# __init__ is the constructor that runs when you create an object
# self is like a empty shell of an object
# ==========================================
# 1. ABSTRACTION
# ==========================================
# By inheriting from ABC (Abstract Base Class), we define a blueprint.
# You cannot create an 'Account' object directly. It is too abstract.
# It forces any child class to implement the 'apply_monthly_logic' method.
#simple words = hiding complexity and showing whats only necessary
class Account(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        
        # ==========================================
        # 2. ENCAPSULATION
        # ==========================================
        # We hide the balance using double underscores (__).
        # This prevents external code from doing: account.__balance = 999999
        # The data is 'encapsulated' and only accessible via our safe methods.
        self.__balance = balance 

    # --- Encapsulation Gateway (Getter) ---
    def get_balance(self):
        """Allows users to see the balance without touching the raw data."""
        # if you try to access the balance outside class, you won't be able to as it is encapuslated
        return self.__balance
    

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" ${amount} deposited.")
        else:
            print(" Invalid deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        print(" Insufficient funds.")
        return False

#wrapper/decorator - this method doesn't have any code yet but every child class is required
# to write a own version of this method
    @abstractmethod
    def apply_monthly_logic(self):
        """This abstract method must be defined by children."""
        pass


# ==========================================
# 3. INHERITANCE
# ==========================================
# SavingsAccount 'is-a' Account. It inherits all attributes and methods.
# It doesn't need to rewrite 'deposit' or 'get_balance'; it gets them for free.
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        # We use super() to trigger the Parent's __init__ (Inheriting the setup)
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_monthly_logic(self):
        """Implementing the abstraction required by the parent."""
        # Note: We use self.get_balance() because __balance is private to the parent!
        interest = self.get_balance() * self.interest_rate
        print(f" Applying {self.interest_rate*100}% interest...")
        self.deposit(interest)


# ==========================================
# 4. POLYMORPHISM
# ==========================================
# Both Savings and Business have a 'withdraw' method, but they behave differently.
# Polymorphism allows us to 'override' the parent's behavior.
class BusinessAccount(Account):
    def __init__(self, owner, balance, fee=5.0):
        super().__init__(owner, balance)
        self.fee = fee

    def withdraw(self, amount):
        """Polymorphic Override: This version of withdraw includes a fee."""
        total = amount + self.fee
        print(f" Business Account: Deducting ${self.fee} transaction fee.")
        # We call the parent's withdrawal logic with the new total
        return super().withdraw(total)

    def apply_monthly_logic(self):
        print(" Business audit complete. No monthly interest applied.")


# --- TEST DRIVE ---
if __name__ == "__main__":
    # Create objects
    savings = SavingsAccount("Aris", 1000, 0.05)
    business = BusinessAccount("Aris Corp", 5000)

    # Demonstrate Polymorphism
    # We can put both in a list and call the same method names
    accounts = [savings, business]
    
    for acc in accounts:
        print(f"\nProcessing {acc.owner}'s account:")
        acc.apply_monthly_logic()  # Different behavior for each (Polymorphism)
        acc.withdraw(100)          # Business charges fee, Savings doesn't (Polymorphism)
        print(f"Final Balance: ${acc.get_balance()}")