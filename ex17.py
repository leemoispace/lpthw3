# Exercise 17: More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

# We could do these in one line too, how?
# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file, 'r').read()
	# If this is used, then there is no need to 
	# close the file at the end of the program.

print "The input file is %d bytes long." % len(indata)

print "Does the output file exist? %r" % exists(to_file)
	# Error as I missed typing %r
print "Ready, hit RETURN to continue, CTRL+C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close() # Error as I typed out_file(close)
# in_file.close()