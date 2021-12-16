list = {
    'A': 100,
    'B': 200,
    'C': 300
}

print(list)

A = list['A']
print(A)

print(list.get('D'))




print('A' in list)
print('A' not in list)

del list['A']
print(list)

list.clear()
print(list)

list['D'] = 98
print(list)

list['D'] = 100
print(list)

