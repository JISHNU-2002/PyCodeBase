def add(num1,num2):
	print(num1+num2)
def sub(num1,num2):
	c=num1-num2
	return(c)
def mul(*args):
	print(args)
	type(args)
	m=a*b
	print(m)

def main():
	print("Hello world\n")
	add(33,11)
	var = (33,11)
	add(*var)
main()

a=int(input("Enter first number = "))
b=int(input("Enter secnd number = "))
choice=int(input("\n1.addition\n2.subtraction\n3.multiplication\n4.division\n\nchoose operation = "))
if(choice==1):
	add(a,b)
	add(a,sub(a,b))
elif(choice==2):
	d=sub(a,b)
	print("diff = ",d)
elif(choice==3):
	c=int(input("Enter third  number = "))
	d=int(input("Enter fourth number = "))
	mul(a,b,c,d)
elif(choice==4):
	print("quotient = ",a/b)
elif(choice==5):
	c=[1,2,4,-23,-5,6546,0,7826]
	for x in c:
		if(x<0):
			continue
		elif(x>0):
			print(x)
		else:
			print("break\n")
			break
elif(choice==6):
	for i in range(1,5):
		for y in 'python':
			print(y)
		print("--"+str(i)+"time--")
	print("invalid choice\n")
elif(choice==7):
	while(a>8):
		print(a)
		a=a-1
	else:
		print("b = ",b)
else:
	print("okay\n")
	pass
	print("pass\n")
