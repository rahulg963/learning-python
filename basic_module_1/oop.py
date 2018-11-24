# mylist = [1,2,3]
# mylist.append(4)
# print(mylist)

# # everything is an object
# print(type([]))

class Sample():
	pass
x = Sample()
print(type(x))

class Dog():
	# Class Object attribute
	species = "mammal"
	def __init__(self, breed, name='DOG'):
		self.breed = breed
		self.name = name

mydog = Dog(breed = 'Lab', name = 'Sammy')
# otherdog = Dog(breed = 'Huskie')
print(type(mydog))
print(mydog.breed, mydog.name, mydog.species)
# print(otherdog.breed)


