# OOPS - Object Oriented Programming Language

# 1. Encapsulation 
# 2. Inheritence
# 3. Polymorphism
# 4. Abstraction

# Encapsulation

class BankAccount():
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        print(f"Exisiting account balance - {self.__balance}")
        if amount > 0:
            print(f"Depositing amount - {amount}")
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
    def __transaction_logs(self, amount): # private method
        if amount>0 and amount <= self.__balance:
            print(f"Exisiting account balance - {self.__balance}")
            self.__balance -= amount
            print(f"After transaction account balance - {self.__balance}")
    
    def make_transaction(self, amount):
        self.__transaction_logs(amount)
        
    
# sandhya = BankAccount(2000)
# # print(sandhya.__balance)
# sandhya.deposit(3500)
# print(sandhya.get_balance())
# # sandhya.__transaction_logs(2500)
# sandhya.make_transaction(2500)


# Inheritence

# class ParentClass:
#     pass

# class ChildClass(ParentClass):
#     pass

# 1. Single Inheritance
# 2. Multi-level Inheritance
# 3. Multiple Inheritance
# 4. Hierarchal Inheritance

# Parent Class - Class from which your child class is inheriting
# Child Class - Class which is inheriting properties from the parent class

# Parent Class/Base class
# Child Class/Derived class

# Single Inheritance

class Parent:
    def parent_properties(self):
        return "Parent Owns a Resort"

class Child(Parent):
    def child_properties(self):
        return "Child Owns a Bike"


# child = Child()
# print(child.child_properties())
# print(child.parent_properties())

# Multi-level Inheritance

class GrandParent():
    def grand_parent_properties(self):
        return "Grand Parent owns a FarmHouse"

class Parent(GrandParent):
    def parent_properties(self):
        return "Parent Owns a Resort"

class Child(Parent):
    def child_properties(self):
        return "Child Owns a Bike"
    
# child = Child()
# print(child.child_properties())
# print(child.parent_properties())
# print(child.grand_parent_properties())


class Father():
    def father_properties(self):
        return "Father Owns a Resort"
    
class Mother():
    def mother_properties(self):
        return "Morther Owns 10 acre land"

class Child(Father, Mother):
    def child_properties(self):
        return "Child Owns a Bike"
    
# child = Child()
# print(child.child_properties())
# print(child.father_properties())
# print(child.mother_properties())


# Hierarchical Inheritance
# One Parent -> Many Children


class Father():
    def father_properties(self):
        return "Father Owns a Resort"
    
class Child1(Father):
    def child1_properties(self):
        return "Child1 Owns a Bike"

class Child2(Father):
    def child2_properties(self):
        return "Child2 Owns a Car"
    
child1 = Child1()
child2 = Child2()
print(child1.father_properties())
print(child2.father_properties())
