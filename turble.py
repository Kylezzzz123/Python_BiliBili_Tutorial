list = [1,3,2,5,4]
print(id(list))
list.append(300)
print(id(list))


t = ('Python', 'world', 98)
print(t)
print(type(t))

tl = tuple(('Python', 'world', 98))
print(tl)
print(type(tl))

t2 = 'Python', 'world', 98
print(t2)
print(type(t2))

t3 = ('Python')   # this is type of string, if you want it to become turble, t3 = ('Python',)
print(t3)
print(type(t3))

t4=()
t5=tuple()

