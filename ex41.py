# Exercise 41: Learning to Speak Object Oriented

# Word drills:
	# class : Tell python to make a new kind of thing
	# object : Two meanings: The most basic kind of thing, 
		# and any instance of some thing.
	# instance : What you get when you tell Python to create a class
	# def : How you define a function inside a class.
	# self : Inside the functions in a class, self is a variable
		# for the instance/object being accessed.
	# inheritance : The concept that one class can inherit traits
		# from another class, much like you and your parents.
	# composition : The concept that a class can be composed of
		# other classes as parts, much like how a car has wheels
	# attribute : A property classes have that are from composition
		# and are usually variables.
	# is-a : A phrase to say that something inherits from another,
		# as in a Salmon is-a Fish.
	# has-a: A phrase to say that something is composed of other
		# things or has a trait, as in a Salmon has-a mouth

# Phrase Drills:
def phrase_drills():
	print """
	class X(Y)
	Make a class X that is-a Y.
	"""
	print """
	class X(object): def __init__(self, J)
	class X is-a base object that has a __init__ that takes 
	parameters 'self' and 'J'.
	"""
	print """
	class X(object): def M(self, J)
	class X is-a base object that has-a function M that takes
	parameters 'self' and 'J'."""
	print """
	foo = X()
	Set foo to an instance of class X.
	"""
	print """
	foo.M(J)
	From foo, get the M function, and call it with 
	parameters self, J.
	"""
	print """
	foo.K = Q
	From foo, get the K attribute and set it to Q.
	"""

# Calling the Phrase Drills function
phrase_drills()
