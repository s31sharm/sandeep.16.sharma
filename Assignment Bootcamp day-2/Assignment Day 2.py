##Program to find Maximum of 3 Numbers##

print("Program to find Maximum of 3 Numbers")
A = int(input("Enter First Number"))
B = int(input("Enter Second Number"))
C = int(input("Enter Third Number"))

print("Maximum of these 3 numbers is ",max(A,B,C))

## Program to find Biggest of given 2 Numbers from the Key Board##
print("Program to find Biggest of given 2 Numbers")
X = int(input("Enter First Number"))
Y = int(input("Enter Second Number"))

if X>Y:
    print("First number is bigger i.e. ",X)
elif X==Y:
    print("Both Numbers are equal i.e. ",Y)
else:
    print("Second number is bigger i.e. ","Y")

## Program to Check whether the given Number is in between 1 and 10 ##
print("Program to Check whether the given Number is in between 1 and 10")
M = int(input("Enter any number "))
if M>0 and M<=10 :
    print("Given Number ",M," is between 1 and 10")
else:
    print("Given Number ",M," isn't between 1 and 10")


##Question 1 : Arithmatic Operation ##
print("Program to do Arithmatic Operation")
C = int(input("Enter first Number"))
D = int(input("Enter Second number"))
print("Sum of two given numbers is ",C+D)
print("Difference of two given numbers is ",C-D)
print("Product of two given numbers is ",C*D)
print("Float Division of two given numbers is ",C/D)
print("Floor Division of two given numbers is ",C//D)
print("Modulus of two given numbers is ",C%D)
print(C,"to the power",D ,"is",C**D)

## Question 2 : even or odd  ##
print("Program to check even or odd")
E = int(input("Enter Number"))
if E%2==0:
    print("Number is even")
else:
    print("Number is odd")

## Question 3 : positive, negative, or zero  ##
print("Program to check positive, negative, or zero")
F = int(input("Enter Number"))
if F>0:
    print("Number",F," is a positive number")
elif F==0:
    print("Number", F, " is Zero")
else:
    print("Number", F, " is a negative number")

## Question 4 : grade of a student based on the marks   ##
print("Program to check grade of a student based on the marks")
S = int(input("Enter Score of Student"))
if S>90:
    print("Student has ",S," marks and passed with Grade A")
elif S>=80 and S<90:
    print("Student has ", S, " marks and passed with Grade B")
elif S>= 70 and S<80:
    print("Student has ", S, " marks and passed with Grade C")
elif S>=60 and S<70:
    print("Student has ", S, " marks and passed with Grade D")
else:
    print("Student has ", S, " marks and has Grade F")

## Question 5 : create a text file called sample.txt    ##
print("Create write and read file")
name = "sample.txt"
with open(name, 'w') as file:
    file.write("Hello, this is a sample file.")
with open(name, 'r') as file:
    content = file.read()
print("Content of the file:")
print(content)

## Question 6 : create a text file called sample.txt    ##
print("Count Words of file")
name2="data.txt"
with open(name2, 'w') as file:
    file.write("Hello, this is a file in which i need to count number of words")
with open(name2, 'r') as file:
            content = file.read()
word_count = len(content.split())
print("Words in file are ",word_count)

## Question 7 : print the numbers from 1 to 10 using a for loop    ##
print("print the numbers from 1 to 10")
print("Ascending order of numbers 1-10 is :")
for numberA in range(1,11,1):
    print(numberA)
print("Descending order of numbers 1-10 is :")
for numberD in  range(10,0,-1):
    print(numberD)

## Question 8 : multiplication table of a number using a for loop   ##
print("multiplication table/multiples")
Num=int(input("Enter the number you want to get multiples of : "))
Mul=int(input("Enter the number of multiples you want to get : "))
print(Mul,"Multiples of number ",Num," are as follows :")
for m in range(1,Mul+1):
    result=Num*m
    print(Num,"*",m,"=",result)



