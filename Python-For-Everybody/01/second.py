a=(lambda x,y : x+y) 
print(a(12,32))

l=[2,32131,0,-324,-3243]
list(map(lambda x : x<0 , l))

x=89
print("global variable",x)
def fun(a,b):
	c=a+b
	x=23
	print("inside the function",x)
	print(c)
fun(12,123)
print("outside the function",x)
