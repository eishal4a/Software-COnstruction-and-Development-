
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

car1 = Car("Toyota", "Red")
print("Model:", car1.model)
print("Color:", car1.color)















class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())














class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        print("Average Marks:", avg)

student1 = Student("Ali", 80, 75, 90)
student1.average()














class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print("Passed")
        else:
            print("Failed")

s1 = Student("Sara", 65)
s1.result()














class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance













class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def debit(self, amount):
        self.balance -= amount

    def credit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance:", self.balance)

acc = Account(12345, 1000)
acc.credit(500)
acc.debit(200)
acc.show_balance()












class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary















class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def annual_salary(self):
        print("Annual Salary:", self.salary * 12)

emp1 = Employee(1, "Ahmed", 50000)
emp1.annual_salary()













class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount(101, 2000)
account.deposit(500)
account.withdraw(300)
account.show_balance()














class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def display(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)

s1 = Student("Ayesha", 88)
s1.display()















class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def update_salary(self, amount):
        self.__salary = amount

    def display_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Usman", 60000)
emp.update_salary(70000)
emp.display_salary()
