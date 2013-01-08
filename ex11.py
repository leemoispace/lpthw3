# Exercise 11: Asking Questions

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %s old, %s tall, %s heavy." % (
	age, height, weight)
# %r is used above to short-circuit the need for input type checking

