#help(round)
import math
#from math import sqrt,log
print(dir(math))
#print(!pwd)

num1 = 6.5
num2 = 6.6
num3 = 8.8723686
print(round(num1))
print(round(num2))
print(round(num3,4))

print(math.ceil(num2))
print(math.floor(num3))

print(math.exp(3))

print(math.pow(2,9))

print(math.sqrt(49))

str = '456'
print(type(str),str)
num = int(str)
print(type(num),num)

print(1,2,3,4,5,sep = '->',end = " || ")
print(11,22,33,44,55,sep = '<-',end = " * ")
print(111,222,333,444,555,sep = '<-->')

x = 'python'
y = 'programming'
print('01 {} 02 {}'.format(x,y))
print('01 {0} 02 {1}'.format('python','programming'))
print('01 {1} 02 {0}'.format('python','programming'))

x = 15.34535
print("value of x = %2.2f"%x)
print("value of x = %2.4f"%x)





