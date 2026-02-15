#  The Iron Bank: Python OOP Mastery

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Build](https://img.shields.io/badge/status-active-success.svg)

A secure, hierarchical banking system built to demonstrate the core principles of **Object-Oriented Programming (OOP)**. This project transitions from procedural scripting to professional system architecture.

---

##  Learning Objectives

This project implements the four pillars of OOP:
* **Encapsulation**: Using private attributes (`__balance`) to protect sensitive data.
* **Inheritance**: Leveraging `super()` to extend functionality from a base class.
* **Abstraction**: Hiding complex logic behind simple method calls like `deposit()`.
* **Polymorphism**: Allowing specialized accounts to behave like standard accounts.

---

##  System Design

### 1. `BankAccount` (Base Class)
The foundational class responsible for core financial logic.
* **State**: Stores `owner` and a hidden `__balance`.
* **Logic**: Handles validation for withdrawals and deposits.

### 2. `SavingsAccount` (Child Class)
A specialized account type that adds interest-bearing capabilities.
* **Interest Logic**: Uses the parent’s methods to safely inject interest payments.
* **DRY Principle**: Uses `super().__init__` to avoid code duplication.

---

##  Getting Started

### Prerequisites
* Python 3.x installed on your machine.

### Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/iron-bank-oop.git](https://github.com/your-username/iron-bank-oop.git)

# 2. Add Interest
account.add_interest()

# 3. Check the results
print(account.get_balance())
