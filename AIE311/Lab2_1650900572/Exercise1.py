print("\n__________________________________Part 1___________________________________\n")

FILO = []
FILO.append('A')
FILO.append('B')
FILO.append('C')
FILO.append('D')
FILO.append('E')
FILO.append('F')

print("Stack after pushing: ", FILO)

while FILO:
    print("Stack:", FILO)
    print("Popped:", FILO.pop())

print("Finish", FILO)


print("\n__________________________________Part 2___________________________________\n")

FIFO = []
print("Stack after pushing: ", FIFO)

FIFO.append('A')
FIFO.append('B')
FIFO.append('C')
FIFO.append('D')
FIFO.append('E')
FIFO.append('F')

while FIFO:
    print("Stack::", FIFO)
    print("Popped:", FIFO.pop(0))
print("Finish", FIFO)

