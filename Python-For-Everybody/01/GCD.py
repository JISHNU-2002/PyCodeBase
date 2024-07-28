num1 = int(input('Enter num1 = '))
num2 = int(input('Enter num2 = '))
a = num1
b = num2
while(b > 0):
    r = a % b
    a = b
    b = r
print('GCD of {} & {} = {}'.format(num1,num2,a))

