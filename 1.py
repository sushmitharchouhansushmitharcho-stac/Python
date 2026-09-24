# even numbers
even_nos=[]
x= int(input("enter your age: "))
y = int(input("enter your father's / mother's age:"))
if(x>y):
    print("parents age should be greater: ")
    exit()

for i in range(x, y+1):
    if i % 2 == 0:
        even_nos.append(i)

print(f"even nos between (x) and (y) are = ", even_nos)
print(dir())        