## Day 3 understanding basics and anatomy of functions ##
## 1. Creating a function to find max. of a number list ##
# def max_of_three():
#
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     num3 = int(input("Enter the third number: "))
#
#     max_value = max(num1, num2, num3)
#
#
#     print(f"The maximum of the three numbers is: {max_value}")
#
# max_of_three()
from turtledemo.sorting_animate import start_isort
from unittest import removeResult

from pyodbc import lowercase


### type 2 without manually entering numbers ##
# def max_3(num1, num2, num3):
#     return max(num1, num2, num3)
#
# out=max_3(12,5,16)
#
# print("Max of given 3 numbers is : ",out)

### Q2 Multiplication ##

# def multiplying_list(Number):
#     result = 1
#     for num in Number:
#         result *=num
#     return result
#
# Number = [2,3,4,5,6,10]
# product_list = multiplying_list(Number)
# print("Product of given numbers is :",product_list)


## Q3 - Reverse String Function ##

# def reverse_string (s):
#         rstring = ""
#         for char in s:
#             rstring=char+rstring
#         return rstring
#
# string_new = input("Enter String to reverse :")
# Reversed = reverse_string(string_new)
#
# print("Reverse of entered string is : ", Reversed)

## Q4 Python function to calculate the factorial of a number ##
#
# def Factorial_New(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*Factorial_New(n-1)
#
# u_input = int(input("Enter a number to calculate factorial:"))
# if u_input<0:
#     print("Error Due to Negative Value")
# else :
#     output = Factorial_New(u_input)
#     print("Factorial of ",u_input," is ",output)


## Q5- Python function to remove duplicates from list ##
# def remove_dup(o_list):
#     return list(set(o_list))
#
# orig_list=[1,2,2,12,11,11,3,4,4,5,5,6]
# distinct_list=remove_dup(orig_list)
# print(distinct_list)

## Q6 Prime Number ##
# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
#
# prime_input=int(input("Enter the number to check prime or not : "))
# if prime_input<=1 :
#     print(f"{prime_input} is not a valid number")
# elif prime(prime_input):
#     print(f"{prime_input} is a prime number")
# else:
#     print(f"{prime_input} is not a prime number")


## Q7 Even Numbers only ##
# def even_list(list_e):
#

## Q8 Upper Case and Lower Case ##

# def case_count(str):
#     upper=0
#     lower=0
#     for char in str:
#         if char.isupper():
#             upper+=1
#         elif char.islower():
#             lower+=1
#     return upper,lower
#
# input_string=input("Enter the string to count case")
# upper_case ,lower_case=case_count(input_string)
# print(f"Number of upper cases are : {upper_case}")
# print(f"Number of lower case are : {lower_case}")


## Sum of Numbers in list ##

# def total_list(list):
#     total=0
#     for num in list:
#         total+=num
#     return total
#
# input_list = [1,2,3,4,5,8,12]
# sum_list=total_list(input_list)
# print(f"Sum of numbers in given list is : {sum_list}")

## Q-10 Palindrome ##

# def palindrome(s):
#     reversed_string = ""
#     for char in s:
#         reversed_string = char + reversed_string
#     return s==reversed_string
#
#
# string_new = input("Enter String to check palindrome :")
# if palindrome(string_new):
#     print("Given string is a palindrome")
# else:
#     print("Given String is not a palindrome")
