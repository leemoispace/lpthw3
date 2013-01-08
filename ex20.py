# Exercise 20: Functions And Files

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	# The comma at the end of the print statement
	# negates the \n that print adds by default.
	# This avoids double line spacing as readline() 
	# returns the \n that *it* finds at EOL of the 
	# line it's reading.
	print line_count, f.readline(),
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

# The following code prints out successive lines because
# readline() reads the current line and stops after the \n
# at the end of that line, i.e. the beginning of the next line.
# And, the file object, in this case, 'f', automagically
# remembers the latest position
print "Let's print three lines:"

current_line = 1
# current_line += 1 failed as current_line was 
# never initialised before.
print_a_line(current_line, current_file)

# current_line = 2
current_line += 1
print_a_line(current_line, current_file)

# current_line = 3
current_line += 1
print_a_line(current_line, current_file)