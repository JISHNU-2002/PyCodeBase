#Program to find the sum of the sine series x - x^3/3! + x^5/5! - ....
import math
n = int(input('Enter the value of n = '))
x = float(input('Enter the degree = '))
x = math.radians(x)
s = x
t = x
i = 1
for i in range(1,n):
    t = ((-t * x * x)/((2*i)*(2 * i + 1)))
    s = s + t
print ('sum = %0.2f' % s)
print()

#Program to find the sum of the cosine series 1 - x^2/2! + x^4/4! - ...
import math
n = int(input('Enter the value of n :'))
x = float(input('Enter the degree :'))
d = x
x = math.radians(x)
s = 1
t = 1
i = 1
for i in range(1,n):
    t = ((-t * x * x)/((2*i)*(2 * i - 1)))
    s = s + t
print ('cos(',d,') = %0.2f' % s)