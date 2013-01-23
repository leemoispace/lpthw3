# Exercise 26: Fixing Zed's Deliberately Broken Code

# Moved function definitions of ex25 to sit above
# the test script that's also included in this file
# to improve readability via more logical grouping

# ---------------------------------
# Some printing practice
# ---------------------------------
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explantion
\twhere there is none.
"""
# deleted space after \n in line 3 of text
# removed \n and \t in last line to make more pretty

print "--------------"
print poem
print "--------------"

# ---------------------------------
# Some 'rithmetic and function practice
# ---------------------------------
five = 10 - 2 + 3 - 6 # changed 5 to 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 # divide operator fixed from \ to /
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point) 
	# '==' (equivalence) replaced with '=' (assignment)
	# argument name fixed from 'start-point' to 'start_point'

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates) # fixed typo 'jeans' to 'beans'

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) # fixed typo - 'crabapples' to 
	# 'crates' and completed function call.


# ---------------------------------
# Breaking Sentences: The functions (See also, ex25.py)
# ---------------------------------
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): # ':' was missing
    """Prints the first word after popping it off."""
    word = words.pop(0) # pop was poop
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # closing paren was missing
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# Breaking Sentences: Test data and function calls:

sentence = "All good things come to those who wait." # removed '\t' tab; fixed typos 'god' to 'good' and 'weight' to 'wait'

words = break_words(sentence) # deleted prefix 'ex25.'
sorted_words = sort_words(words) # deleted prefix 'ex25.'
# there is no need to invoke ex25 as a module because
# all the code is included in this file itself

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) # removed stray period at beginning of line
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence) # deleted prefix 'ex25.'
print sorted_words # fixed print command

print_first_and_last(sentence) # fixed function name in the function call: 'irst' to 'first'

print_first_and_last_sorted(sentence) # removed indentation, 
	# fixed function name: '_a_' to '_and_', 
	# fixed argument name 'senence' to 'sentence'