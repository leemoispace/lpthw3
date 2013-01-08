# Exercise 17 in one line

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copied %s to %s" % (from_file, to_file)
open(to_file, 'w').write(open(from_file, 'r').read())
	# Write takes exactly one argument and it is valid
	# to pass methods as arguments.
	
# There is no need to explicitly close any file.
# The above script should open and close files automatically.