#numbers = [100,200,300,400]
#key = 300
#if key in numbers:
#    print("found")
#else:
#    print("not found")    


#a = [10,20,30,40,50]
#key = int(input("enter the key to search : "))
#if key in a:
#    print("found")
#else:
#    print("not found")    


a = list(map(int,input("enter the numbers: ").split())) 
# map convets the input string into intrgers and list converts the 
# map object into actual list and split seperates the input sting 
# into individial numbers.
key = int(input("enter the key to search : "))
if key in a:
    print("found")
else:
    print("not found")    