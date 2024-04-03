stack = []

def push(element):
    stack.append(element)

def pop():
    if len(stack) != 0:
        stack.pop()
    
def peek():
    if len(stack) != 0:
        print( stack[-1] )

def display():
    for i in stack[::-1]:
        print(i)

push(2)
push(2)
push(2)
push(1)
display()