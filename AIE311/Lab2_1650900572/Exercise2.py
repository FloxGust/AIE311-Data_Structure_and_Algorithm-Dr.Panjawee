stack = []

stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
stack.append('E')
stack.append('F')

print("Normal Stack: ", stack)

reverse_stack = []
while stack:
    print(reverse_stack)
    reverse_stack.append(stack.pop())

print("Reverse Stack : ", reverse_stack)
