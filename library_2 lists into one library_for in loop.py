items = ['Fruits', 'Books', 'Others']
princes = [96,78,85,100,200]

d = {item: price for item , price in zip (items, princes)}
print(d)

e = {item.upper(): price for item , price in zip (items, princes)}
print(e)

