# Exercise 16: Reading and Writing Files

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL+C (^C)."
print "If you DO want that, hit RETURN."

raw_input("? ")

# Open the file in write mode.
print "Opening the file..."
target = open(filename, 'w')

# truncate() empties the file.
print "Truncating the file. Goodbye!"
target.truncate()
	# But truncate() is not really required here as
	# the file was opened in 'w' mode, which opens the
	# file, truncates its contents and then makes it
	# available for writing.
	# http://docs.python.org/2/library/functions.html#open

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write(line1+'\n'+line2+'\n'+line3)
	# One line instead of the six above.

print "And finally we close it."
target.close()