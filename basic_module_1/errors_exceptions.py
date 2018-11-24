# try, except, finally

# SyntaxError
# print('hello)
# NameError 
# mylisthere = [1,2,3]
# print(mylist)

try:
	# f = open('simple.txt', 'r')
	f = open('simple.txt', 'w')
	f.write("Test to write simple text!")
except IOError:
	print("Error: Could not find file or read data")
except:
	print("Error occurred but type is not known")
else:
	# this will be exceuted only if error does not occur
	print("Success")
	f.close()
finally:
	print("I always work even if error occurres")
print("hello world")
