n = int(input('Enter the number :'))
prime = True
i = 2
while (i <= n/2):
    if (n % i == 0):
        prime = False
        break
    i = i + 1
if (prime):
    print("The number {} is prime".format(n))
else:
    print("The number {} is not prime".format(n))

#prime number or not
#prime numbers have more than one factors to divide
#non-prime has only one factor(1,number)
n = int(input('Enter a number = '))
prime = True
i = 2

while(n//2 >= i):
    if(n%i == 0):
        prime = False
        break
    i+=1

if(prime == True):
    print('{} is prime'.format(n))
else:
    print(n,'is not prime')