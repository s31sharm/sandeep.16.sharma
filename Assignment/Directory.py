## Dictionary ##

## Creating a Dictionary ##

Student = {
    "Alice": 85,
"Bob": 90,
"Charlie": 78,
}

print("Students Grades Are",Student)

#Accessing Dictionary Values##

print("Bob's Grade is ",Student["Bob"])


## Adding and Removing Key-Value Pairs ##
Student["David"]=92
del Student["Charlie"]

print("Updated Student List is :",Student)

## Updating a value ##
Student["Bob"]=95
print("Updated Marks of Students are :",Student)

## Checking a key value ##

if "Alice" in Student:
    print("Alice is in student list")
else:
    print("Alice isn't in student list")

## Dictionary Length ##

print("Number of key pairs in student list is ",len(Student))
