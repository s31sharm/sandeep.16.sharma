## Q1 Creating Class ##
from multiprocessing.heap import Arena


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