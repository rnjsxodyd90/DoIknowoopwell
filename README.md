#Welcome to the Iron Bank system. This project is designed to transform your understanding of Python from simple scripting to architecting systems using oop.

#Learning Objectives
By completing this project, you will master:

Encapsulation: Protecting sensitive data (like account balances) from external tampering.

Inheritance: Creating specialized classes (Savings) from general classes (Bank Account).

The super() Function: Learning how to let a parent class handle the "heavy lifting" during initialization.

Method Chaining: Calling one method (like deposit) from inside another (like add_interest).

and many more basic concepts of OOP

1. The BankAccount Class (The Foundation)
The base class that defines what every bank account in the world must have.

Attributes: owner, __balance (Private).

Methods:

deposit(amount): Increases the balance.

withdraw(amount): Decreases the balance (if funds are sufficient).

get_balance(): Securely returns the current balance as a string.

2. The SavingsAccount Class (The Extension)
A specialized account that inherits everything from BankAccount but adds "Interest" logic.

Attributes: Everything from the parent + interest_rate.

New Method: add_interest(): Calculates interest based on the balance and deposits it automatically.

##Challenge: Implementation
To master this, your code must follow these strict rules:

Don't Touch the Private Variable: You cannot use self.__balance inside the SavingsAccount. You must use the public methods (deposit) to change the money. This is "High-Level" Encapsulation.

Use super(): In the SavingsAccount constructor, do not re-assign self.owner = owner. Let the parent do it!

Validation: Ensure no one can deposit a negative amount or withdraw more than they have.

##How to Run
Python
# 1. Create a Savings Account
account = SavingsAccount("Your Name", 1000, 0.05)

# 2. Add Interest
account.add_interest()

# 3. Check the results
print(account.get_balance())
