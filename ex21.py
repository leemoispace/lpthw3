# Exercise 21: Functions can return something

def add(a, b):
	print "ADDING: %d + %d" % (a, b)
	return a + b
	
def subtract(a, b): # don't forget the ':' in function definitions
	print "SUBTRACTING: %d - %d" % (a, b)
	return a - b
	
def multiply(a, b): # don't forget the ':' in function definitions
	print "MULTIPLYING: %d * %d" % (a, b)
	return a * b
	
def divide(a, b): # don't forget the ':' in function definitions
	print "DIVIDING: %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit. Type it any way.
	# This script consists of functions passsed as
	# arguments. 
	# Note that the variables passed to the functions were 
	# already initialised. They were assigned the
	# return values of previous function calls.
	previous
print "Here is a puzzle:"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
