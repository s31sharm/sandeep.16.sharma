## Tupple Exercise ##

## Creating Tupple ##
tupple1=("Red","Green","Blue")
print("Colors are ",tupple1)

#Accessing first and last element##
colors=("Red","Green","Blue","Yellow")

print("List of colors is ",colors)
print("First color is :",colors[0])
print("Last color is :",colors[-1])

# ### Changing Element in tupple ##
# color=("Red","Green","Blue")
# color[1] = "yellow"

### Tupple unpacking##
Coordinates=(10,20,30)
print("Original Coordinate list is :",Coordinates)
print("After Defining 3 variables for 3 values out-put is ")

x,y,z=Coordinates

print("x=",x)
print("y=",y)
print("z=",z)

#Check Element in Tuple##

colorname = ("red","green","blue")
print("Original color list is :",colorname)
print("Checking if blue is present or not")
if "blue" in colorname :
    print("Given color is available in list")
else:
    print("Given color is not available in list")


#Tuple Length##
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print("List of days is :",days)
print("Number of days are :",len(days))
