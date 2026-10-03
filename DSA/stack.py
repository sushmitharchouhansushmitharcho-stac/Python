# 1
size = 5
stack = [0] * size
top = -1

while top < size - 1:
    x = int(input("enter the element to push: "))

    top += 1
    stack[top] = x

print("Stack: ", stack)
print("Top: ",top)

# output: enter the element to push: 10
# enter the element to push: 20
# enter the element to push: 30
# enter the element to push: 40
# enter the element to push: 50
# Stack:  [10, 20, 30, 40, 50]
# Top:  4

# 2
size = 5
stack = [0] * size
top = -1

x = int(input("enter the element to push: "))

if top == size - 1:
    print("stack is full")

else:
    top += 1
    stack[top] = x

print("Stack: ", stack)
print("Top: ", top)

# output:
# enter the element to push: 10 
# Stack:  [10, 0, 0, 0, 0]
# Top:  0