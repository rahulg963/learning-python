# Arithmetic
print("Hello World")
# 105
2 + 10 * 10 + 3

# ------

# String
# basics
print("I'm a dog")
# Indexing
my_string = 'abcdefg'
print(my_string)
print(my_string[0])
print(my_string[-1])
# Slicing
# start from index 2 till end
print(my_string[2:])
# Start from index 0 till in 0 (not including 3)
print(my_string[:3])
# cde from abcdefg, not including 5
print(my_string[2:5])
# return entire string
print(my_string[:])
# defing step size > aceg
print(my_string[::2])
# String are immutable > Not allowed
# my_string[0] = 'X'
# Methods
upper_string = my_string.upper()
lower_string = my_string.lower()
print(upper_string)
# split
hello_world = 'Hello Word'
x = hello_world.split('o')
print(x)
# Inserting
x = "Item One : {} Item Two : {}".format("dog", "cat")
print(x)
x = "Item One : {x} Item Two : {y}".format(y = "dog", x = "cat")
print(x)

# ------

# LIST
mylist = [1, 2, 3]
# It can be nested and mixed data type
mylist = ['adsad', 1, True]
print(len(mylist))
# Slicing is same as strings
# LIST is MUTABLE unlike STRINGS
mylist = ['a', 'b', 'c', 'd'] 
print('before reassignment')
print(mylist)
mylist[0] = 'Rahul'
print('after reassignment') 
print(mylist)
mylist.append("New Item")
print(mylist)
# add another list to original list
mylist.append(['x', 'y'])
print(mylist)
# add items to same list
mylist.extend(['p', 'o'])
print(mylist)
# pop item from list
mylist.pop()
print(mylist)
mylist.pop(1)
print(mylist)
# In place reverse > make changes in original list
mylist.reverse()
print(mylist) 
mylist.sort()
print(mylist)
# Nested List Indexing
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[0][0])
# grab and return row[0] > List Comprehension
first_col = [row[0] for row in matrix]
print(first_col)

# ------

# Dictionay
# Python hash table, do not have order
# Can be nested or any type of data
mystuff = {"key1" : "value", "key2" : "value2"}
print(mystuff['key1'])
print(mystuff)
mystuff = {'lunch' : 'pizza', 'bfast': 'eggs'}
# changes are permanent and items can be added
mystuff['lunch'] = 'Burger'
mystuff['dinner'] = 'pasta'
print(mystuff['lunch'])
print(mystuff)

# ------

# Tupes are immutable List
# Sets unordered collection
# Booleans > True, False, 1, 0
# Tuples
t = (1,2,3)
print(t[0]) 
# can hold mixed data types like list
t = ('a', True)
print(t)
# throw error
# t[0] = "NEW"
print(t)
# Tuples and Strinds are immutable
# List are mutable
# List [], tuple ()
mylist = ['a', True]
print(mylist)
mylist[0] = 'New'
print(mylist)
# Sets > <unordered> collection of <unique> elements
x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(0.1)
x.add('a')
# unique elements
x.add(4)
print(x)
converted = set([1,2,1,1,1,1,1,3,3,3,3,3,2,2,2])
print(converted)

# ------

# Basic operators 
# False
print('1' == 1)
# True
print(1 == 1)
# <and> <or> <logical operator>
if 1<2:
	print('yes!')
elif 2>3:
	print('no')
else:
	print('yeah!!')
if 1<2:
	if 2<3:
		print("True")
if 1<2:
	print('First Block')
	if 20<3:
		print('Second Block')
seq = [1,2,3,4,5,6,7]
for item in seq:
	print(item)
	# Order is not maintained
d = {"sam" : 1, "frank" : 2, "Dan" : 3 }
# Only keys are printed
for item in d:
	print(item)
# Key and value
for item in d:
	print(item)
	print(d[item])
# Values
for item in d.values():
	print(item)
# tuples iterations
mypairs = [(1,2), (3,4)]
for item in mypairs:
	print(item)
# Tuple packing
for tupItem1, tupItem2 in mypairs:
	print(tupItem2)
	print(tupItem1)
# While Loops
i = 1
while i<5:
	print("i is {}".format(i))
	i = i + 1
# Range from 0 to 4 
# range returns a generator, it does not make complete
print(list(range(0,5)))
print(list(range(0, 21, 2)))

for item in range(10):
	print(item)
x = [1, 2, 3, 4]
out = []
# style 1
for num in x:
	out.append(num**2)
print(out)	
# style 2
out = [num**2 for num in x]
print(out)