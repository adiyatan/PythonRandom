a = 4
b = 2
#>

print('============= lebih besar dari (>)===========')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = a > 12
print(b,'>',12,'=',hasil)

print('============= lebih kecil dari (<)===========')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = a < 12
print(b,'<',12,'=',hasil)

print('============= lebih dari sama dengan (>=)===========')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = a >= 12
print(b,'>=',12,'=',hasil)

print('============= kurang dari sama dengan (<=)===========')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = a <= 12
print(b,'<=',12,'=',hasil)

print('============= sama dengan (==)===========')
hasil = a == 3
print(a,'==',3,'=',hasil)
hasil = a == 12
print(b,'==',12,'=',hasil)

print('============= tidak sama dengan (!=)===========')
hasil = a != 3
print(a,'!=',3,'=',hasil)
hasil = a != 12
print(b,'!=',12,'=',hasil)

#is
print('============= object identity (is)===========')
x = 5
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai x =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai x =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

#isnot
print('============= object identity (is not)===========')
x = 5
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai x =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)

x = 5
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai x =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)