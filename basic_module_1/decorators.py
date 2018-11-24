# s = "GLOBAL VARIABLE"
# def func(s):
# 	print(s)
# func(s)

# def func():
# 	s=50
# 	print(s)
# func()
# print(s)

# def func():
# 	# this will effect global variable
# 	global s
# 	s=50
# 	print(s)
# func()
# print(s)

# def func():
# 	mylocal = 10
# 	# dict containg local variables
# 	print(locals())
# 	# dict containg global variables
# 	print(globals())
# func()

# def hello(name="Jose"):
# 	return "hello " + name
# print(hello())

# # mynewgreet contains reference to hello function
# mynewgreet = hello
# mynewgreet()


# def hello(name = "Jose"):
# 	print("THE HELLO() FUNCTION HAS BEEN RUN!")
	
# 	def greet():
# 		return "THIS STRING IS INSIDE GREET()"
	
# 	def welcome():
# 		return "THIS STRING IS INSIDE WELCOME!"

# 	print(greet())
# 	print(welcome())
# 	print("End of hello()")
# hello()  

# def hello(name = "Jose"):
# 	print("THE HELLO() FUNCTION HAS BEEN RUN!")
	
# 	def greet():
# 		return "THIS STRING IS INSIDE GREET()"
	
# 	def welcome():
# 		return "THIS STRING IS INSIDE WELCOME!"

# 	if name == "Jose":
# 		return greet
# 	else:
# 		return welcome
# x = hello()
# print(x())

# def hello():
# 	return "Hi Jose"
# # passing function inside other functions
# def other(func):
# 	print("Hello")
# 	print(func)

# other(hello)


# <<<<Without @ in decorator>>>>
# def new_decorator(func):
# 	def wrap_func():
# 		print("Code here before executing func")
# 		func()
# 		print("Func() has been called")
# 	return wrap_func

# def func_needs_decorator():
# 	print("This function is in need of a decorator")

# func_needs_decorator()
# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()

# <<<<with @new_decorator>>>>
def new_decorator(func):
	def wrap_func():
		print("Code here before executing func")
		func()
		print("Func() has been called")
	return wrap_func

@new_decorator
def func_needs_decorator():
	print("This function is in need of a decorator")

# func_needs_decorator = new_decorator(func_needs_decorator) ==== @new_decorator
func_needs_decorator()


