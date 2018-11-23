# Scopes
# Local, Enclosing function locals, Global, Built-in
# L E G P
x = 25
def my_func():
 	x = 50
 	return x
print(x)
print(my_func())

# x is local level
lambda x: x**2

# this is global variable 
name = 'This is a global name!'

def greet():
	# enclosing function locals
	# here name is enclosed level scope
	name = "sammy"
	def hello():
		print("hello " + name)
	hello()
greet()
print(name)

# python variable
# len = 23

y = 50
def func(y):
	print('y is: ', y)
	y = 1000
	print('local y changed to : ', y)

func(y)
print(y)	

def func():
	global y
	y = 1000

print("before function call, y is:", y)
func()
print("After function call, y is:", y)
