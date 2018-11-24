# INHERITANCE

class Animal():
	def __init__(self):
		print("Animal Created")
	def whoAmI(self):
		print("Animal")
	def eat(self):
		print("Eating")

class Dog(Animal):
	def __init__(self):
		# Animal.__init__(self)
		print("Dog Created")
	def bark(self):
		print("Whoof")
	def eat(self):
		print("Dog eating")
# mya = Animal()
# mya.whoAmI()
# mya.eat()

mya = Dog()
mya.whoAmI()
mya.eat()
mya.bark()
