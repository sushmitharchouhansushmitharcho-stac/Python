# Variablen = A container for values ( (4 different types of data types) string, integer, float, boolean).
#              A variable behaves as if it was the value it contains.

# Strins : These are series of characters that are used to store text data. enclosed in single or double quotes. 
#            they can include numbers but we treat them as characters.
first_name = "Sushmitha"
food = "Biryani"
email_id = "sushmitha123@gmail.com"

# print(first_name)

# to use formatted string litrels(f-string or F-string), begin a string with f or F before the opwning quotatiion mark.
# Inside this string, you can write a python expression between { and } characters that can refer
# to variables or literal values.

print(f"hello {first_name}") # output = hello Sushmitha
# print(f"hello {first_name}") // output = hello {first_name} 
print(f"you like {food}")
print(f"your email id is {email_id}")

# Integers : An integeer is a whole number (no quotes).
age = 19
quantity = 3 
num_of_students = 60

print(f"your age is {age}")
print(f"you are {age} years old")
print(f"you are buying {quantity} items")
print(f"your class has {num_of_students} students")

# Floats : a float is a number that has a decimal point. (no quotes)( Float means floating points)
price = 10.99456
cgpa = 8.11
distance = 6.7

# print(f"the price of this product is ${price:.2f}") // output = the price of this product is $10.99
# this .2f (. f) means that we just need 2 decimal values after the decimal point.
print(f"the price of this product is ${price}")
print(f"your cgpa is {cgpa}")
# print(f"your cgpa is {cgpa:.1f}") // output = youe cgpaa is 8.1
print(f"the distace from college to home is {distance} km")

# Boolean : it has only 2 values i.e, True or Flase. (no quotes) (Boolean is used to represent the truth values).
# it is either true or false.
is_student = False # 1
# is_student = true // error ( only capital T and F are allowed )

#print(f"are you a student? {is_student}")

# using conditional statements
if is_student:
    print("you are a student")

else:
    print("you are not a student")


for_sale = True # 2
if for_sale:
    print("this car is for sale")
else:
    print("not available")


is_online = False #3
if is_online:
    print("you are online")
else:
    print("you are offline")