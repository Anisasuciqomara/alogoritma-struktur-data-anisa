a,b= 5,10
print(a, '>',b, '=',a > b)
print(a, '<',b, '=',a > b)
print(a, '==',b, '=',a == b)
print(a, '!=',b, '=',a != b)
print(a, '>=',b, '=',a >=b)
print(a, '<=',b, '=',a <=b)
#karena a jadi float, kita ubah lagi menjadi integer
a = int (a)
a %=9
print('a %= 9 -> ',a)
a //=6
print('a //= 6 ->',a)
a **=1
print('a **= 1 ->',a)