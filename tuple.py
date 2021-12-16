t = (10, [20,30], 9)
print(t)
print(type(t))
print(t[0])
print(t[1])
print(t[2])

# t[1] = 100           # Error  # tuple cannot be modified for elements

t[1].append(100)
print(t)

