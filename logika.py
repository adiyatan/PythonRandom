print('===NOT===')
a = True
c = not a
print('data a =',a)

print('===NOT===')
print('data c =',c)

print('===OR===')
a = False
b = False
c = a or a
print(a,"OR",b,'=',c)
a = False
b = True
c = a or a
print(a,"OR",b,'=',c)
a = True
b = False
c = a or a
print(a,"OR",b,'=',c)
a = True
b = True
c = a or a
print(a,"OR",b,'=',c)

print('===AND===')
a = False
b = False
c = a and a
print(a,"AND",b,'=',c)
a = False
b = True
c = a and a
print(a,"AND",b,'=',c)
a = True
b = False
c = a and a
print(a,"AND",b,'=',c)
a = True
b = True
c = a and a
print(a,"AND",b,'=',c)

print('===XOR===')
a = False
b = False
c = a ^ a
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ a
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ a
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ a
print(a,'XOR',b,'=',c)