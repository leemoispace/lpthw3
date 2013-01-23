# Exercise 42: Is-A, Has-A, Objects, and Classes

## Animal is-a object
class Animal(object):
	pass # this is a placeholder keyword that returns a null value
	# pass is useful to create scaffolding of functions and classes
	# even though specific functionality / composition may 
	# not be known
	
## Create a new Class Dog that is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## class Dog has-a __init__ that accepts self and name params
		self.name = name # an instance of name will be initialised
							# to the value contained in 'name'

## Create a new class named Cat that is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## class Cat has-a __init__ that accepts self and name params
		self.name = name
		
## Create a new class called Person that is-a base object type
class Person(object):
	
	def __init__(self, name):
		##
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None # None initialises self.pet to a null value
		
## Create a new class named Employee that is-a Person
class Employee(Person):
	
	def __init__(self, name, salary):
		## hmmm what is this strange magic?
		super(Employee, self).__init__(name) # this gives access
			# to the name attribute of Employee's parent object
			# i.e. Person. Apparently useful in the case of 
			# multiple inheritance.
		
		self.salary = salary
		
## Create a new class called Fish that is-a base object type
class Fish(object):
	pass
	
## Create a new class called Salmon that is-a Fish
class Salmon(Fish):
	pass
	
## Create a new class called Halibut that is-a Fish
class Halibut(Fish):
	pass

## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## From mary, get the attribute pet and set it to the value satan
mary.pet = satan # Now, Mary's pet is-a cat object named satan

## Frank is-a Employee, named "Frank" and perhaps numbered 120000
frank = Employee("Frank", 120000)

## From frank, get the attribute pet and set it to the value rover
frank.pet = rover # Now, Frank's pet is-a dog object named rover

## Flipper is-a fish
flipper = Fish()

## Crouse is-a Salmon, and Salmon is-a Fish
crouse = Salmon()

## Harry is-a halibut, and Halibut is-a Fish
harry = Halibut()
