
album_year = 1983
album_year = 1970
if album_year == 1970:
    print("Album year is greater than 1969")
print('do something..')

if album_year>1969 and album_year<1980:
    print('and')
if album_year<1968 or album_year>1969:
    print('or')
if not(album_year == 1983):
    print('not')
if album_year<1980 or album_year<1991 or album_year<1993:
    print('album year = ',album_year)


#largest among three
num1 = int(input('Enter num1 = '))
num2 = int(input('Enter num2 = '))
num3 = int(input('Enter num3 = '))

if(num1>=num2 and num1>=num2):
    largest = num1
elif(num2>=num1 and num2>=num3):
    largest = num2
else:
    largest = num3
print('largest = ',largest)


#leap year
#year ending with 00 - century year
year = int(input('Enter the year = '))
if((year%400 == 0) and (year%100 == 0)):
    print('leap year')
elif((year%4 == 0) and (year%100 != 0)):
    print('leap year')
else:
    print('not a leap year')


#to find three sides form right angle triangle
side1 = int(input('Enter side1 = '))
side2 = int(input('Enter side2 = '))
side3 = int(input('Enter side3 = '))

sq1 = side1 ** 2
sq2 = side2 ** 2
sq3 = side3 ** 2

if((sq1+sq2 == sq3) or (sq1+sq3 == sq2) or (sq2+sq3 == sq1)):
    print('right angle triangle')
else:
    print('not a right angle triangle')