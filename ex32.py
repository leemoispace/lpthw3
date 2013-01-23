# Exercise 32: Loops And Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
# Same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# Also we can go through mixed lists too
# Notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
	
# We can also build lists, first start with an empty one
elements = []

# Then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list" % i
	# append() is a function that lists understand
	elements.append(i)

# Now we can print them out too
for i in elements:
	print "Element was: %d" % i
	
# Drill answer:
# Yes, there's a one-liner way to do the assignment
def populate_list_with_range(a, b, c):
	"""The full form of range() returns a list 
	of plain integers. We can exploit this fact 
	to populate a list with integer values. 
	See: http://docs.python.org/2/library/functions.html#range"""
	# Populating the list 
	new_elements = range(a, b, c)
	print """A list of integers beginning at %d, to the limit of %d, incremented in steps of %d.""" % (a, b, c)
	print new_elements

populate_list_with_range(0, 10, 1)
populate_list_with_range(2, 100, 2)
populate_list_with_range(0, -100, -5)