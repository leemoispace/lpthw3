from sys import argv 
	# This basically tells Python 
	# to accept arguments that are passed to it 
	# via sys / the command line.

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third