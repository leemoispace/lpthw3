# Exercise 6: Strings and Text
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"

# string in a string
y = "Those who know %s and those who %s" % (binary, do_not) 

print x
print y

# string in a string
print "I said: %r." % x

# string in a string
print "I also said: '%s'." % y

hilarious = False
# %r forces raw data as a string inside a string
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e