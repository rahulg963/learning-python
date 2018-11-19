# use snake_case
# function defination
def my_func(param1='default'):
	"""
	This is the docstring,
	This should be immediately below function,
	This should be inside multi line comment
	"""
	print('my first python function! {}'.format(param1))
my_func()
my_func("Hello")

def hello():
	return 'Hello'
result = hello()
print(result)

def add_num(num1, num2):
	return num1 + num2
# numbers are added
print(add_num(2,3))
# strings are added
print(add_num("2","3"))
# throw error
# print(add_num(2,"3"))
def addNum(num1, num2):
	if(type(num1) == type(num2) == type(10)):
		return num1 + num2
	else:
		return "Sorry!"
print(addNum(2,3))
print(addNum("2","3"))

# Lamda Expression
# Filter function
mylist = [1,2,3,4,5]
def is_even(num):
	return num%2 ==0 
evens = filter(is_even, mylist)
print(type(evens))
# this can be generator object as well || Check for it
print(evens)
print(list(evens))

# Lambda > used once inside a function, no need to create different fucntion
print('Lambda')
print(filter(lambda num:num%2==0, mylist))

tweet = "Go Sports! #Sports"
result = tweet.split('#')
print(type(result))
print(result)

# False
print('x' in [1,2,3])
#True
print('x' in [1,2,3,'x'])