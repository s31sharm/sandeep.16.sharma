## Q1 Creating Class ##

# class mycar:
#     make = "Hyundai"
#     model = "i-20"
#     year = "2017"
#     color = "white"
#
# co_name=mycar()
# print(co_name.make)
# print(co_name.model)
# print(co_name.year)
# print(co_name.color)

## Q2. Student Information ##
# class Student:
#     def __init__(self,name,roll_number,marks):
#         self.name=name
#         self.roll_number=roll_number
#         self.marks=marks
#     def display_info(self):
#         print(f"Name:{self.name}")
#         print(f"Roll No. :{self.roll_number}")
#         print(f"Marks: {self.marks}")
#
# Ghatotkach=Student("Ghatotkach",13,99)
# Hidimba=Student("Hidimba",14,98)
# Ghatotkach.display_info()
# Hidimba.display_info()

##Q3 Rectangle - Parimeter and Area ##
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def display_info(self):
#         Perimeter=2*(self.length+self.breadth)
#         Area=self.length*self.breadth
#         print(f"Perimeter = {Perimeter}")
#         print(f"Area = {Area}")
# #### Have a Query if we want to print for which Rectangle which is output how to do that ###
# Rectangle1=Rectangle(13,11)
# Rectangle2=Rectangle(11,12)
# Rectangle1.display_info()
# Rectangle2.display_info()

## Q4 Area and Circumference of Circle by get command ##

# class Circle():
#     def __init__(self,radius):
#         self.radius=radius
#     def get_area(self):
#         ##Area=pi*rsquare##
#         return 3.14*self.radius*self.radius
#     def get_circumference(self):
#         ##Circumference=2*pi*r##
#         return 2*3.14*self.radius
#
# Circle1=Circle(5)
# print(f"Area= {Circle1.get_area()}")
# print(f"Circumference= {Circle1.get_circumference()}")

## 5. Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.##

# class Bank:
#     def __init__(self,number,balance=0):
#         self.number=number
#         self.balance=balance
#     def debit(self,amount):
#         self.balance-=amount
#         print(f"Debited amount {amount},New balance is : {self.balance}")
#     def credit(self,amount):
#         self.balance+=amount
#         print(f"Amount Credited : {amount} , New Balance is : {self.balance}")
#     def print_balance(self):
#         print(f"Account Number : {self.number}  Balance is {self.balance}")
#
# account=Bank(14768,5000)
# account.print_balance()
# account.debit(1000)
# account.credit(500)
# account.print_balance()

## 6. Creating Class object for counting Employees ##

# class Employee:
#     employee_count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Employee.increment_employee_count()
#     @classmethod
#     def increment_employee_count(cls):
#         cls.employee_count += 1
#     @classmethod
#     def get_employee_count(cls):
#         return cls.employee_count
#
# emp1 = Employee("Sandeep")
# emp2 = Employee("Atendra")
# emp3 = Employee("Anand")
# emp4 = Employee("Satyawan")
#
#
# print(f"Total Employees are: {Employee.get_employee_count()}")


## 7. Book with attributes title, author, and price##

# class Book:
#     def __init__(self, title, author,price=534):
#         self.title=title
#         self.author=author
#         self.price=price
#     def display_details(self):
#         print(f"Book Name is {self.title}\nAuthor is {self.author}\nBook Price is {self.price}")
#
# Book1=Book("Suryavansham","Sony",2)
# Book1.display_details()
# print("\n")
# Book2=Book("Zehar wali kheer","Thakur Bhanu Pratap")
# Book2.display_details()

## 8. Temperature Converter##

# class TConverter:
#     def celsius_to_fahrenheit(self, celsius):
#         fahrenheit = (celsius * 9/5) + 32
#         return fahrenheit
#
#
# converter = TConverter()
# t_calc = [23, 31, 42]
# for celsius in t_calc:
#     t_fahrenheit = converter.celsius_to_fahrenheit(celsius)
#     print(f"{celsius} Degree Celcius is equal to {t_fahrenheit:} Degree Fahrenheit")

## 9. Time##

# class Time:
#     def __init__(self, hours=0, minutes=0):
#         self.hours = hours
#         self.minutes = minutes
#         self._normalize()
#
#     def _normalize(self):
#         if self.minutes >= 60:
#             extra_hours = self.minutes // 60
#             self.hours += extra_hours
#             self.minutes %= 60
#         elif self.minutes < 0:
#             extra_hours = (-self.minutes // 60) + 1
#             self.hours -= extra_hours
#             self.minutes = (self.minutes + 60 * extra_hours) % 60
#
#     def add_time(self, other):
#         new_hours = self.hours + other.hours
#         new_minutes = self.minutes + other.minutes
#
#         return Time(new_hours, new_minutes)
#
#     def __str__(self):
#         return f"{self.hours:02}:{self.minutes:02}"
#
# time1 = Time(2, 45)
# time2 = Time(3, 30)
# result_time = time1.add_time(time2)
# print(result_time)

## Q-10 Create a class EmployeeSalary##

# class EmployeeSalary:
#     basic_salary = 0.0
#     bonus_percentage = 0.0
#
#     def __init__(self, name, basic_salary):
#         self.name = name
#         self.basic_salary = basic_salary
#
#     @classmethod
#     def set_bonus_percentage(cls, new_percentage):
#         cls.bonus_percentage = new_percentage
#
#     def calculate_total_salary(self):
#         bonus = (self.basic_salary * self.bonus_percentage) / 100
#         total_salary = self.basic_salary + bonus
#         return total_salary
#
#     def __str__(self):
#         return f"{self.name}: Basic Salary = {self.basic_salary}, Bonus Percentage = {self.bonus_percentage}%, Total Salary = {self.calculate_total_salary()}"
#
# EmployeeSalary.set_bonus_percentage(10)
# employee1 = EmployeeSalary("Ramesh", 50000)
# employee2 = EmployeeSalary("Suresh", 60000)
# print(employee1)
# print(employee2)

