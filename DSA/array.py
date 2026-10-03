n = int(input("enter the number of elements:"))

arr = []

for i in range(n):
   # element = int(input("enter the element: ")) 
   # out put : enter the number of elements:5
            #enter the element: 10
            #enter the element: 20
            #enter the element: 30
            #enter the element: 40
            #enter the element: 50
            #Array elements are: 
            #10 20 30 40 50 
   # element = int(input(f"enter the element: "))(same as first one)
    element = int(input( f"enter the element {i+1}: "))
    # out put : enter the number of elements:5
            #enter the element 1: 10
            #enter the element 2: 20
            #enter the element 3: 30
            #enter the element 4: 40
            #enter the element 5: 50
            #Array elements are: 
            #10 20 30 40 50 
    arr.append(element)

print("Array elements are: ")
for element in arr:
    print(element, end=" ")