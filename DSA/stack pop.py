size = 5
stack = [1,2,3,4,5]
top = 3

if top == -1:
    print("stack is empty")

else:
    x = stack[top]
    top -= 1 # line 3
    print("Popped element is: ", x)
    print("Stack: ", stack[:top+1]) 
    # for this last condition there is connection of  line 10.