x=1
for x in range(1,10):
   for y in range(1, x+1):
       print( x , '*', y, '=', x*y, end='\t')
   print()