# Exercise 35: Branches And Functions

from sys import exit

prompt = "> "

def gold_room():
	"""How much gold can the player take and still remain alive to exit the gold room?"""
	print "This room is full of gold. How much do you take?"
	
	next = raw_input(prompt)
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	"""Trying to beat the bear and get past the door it guards."""
	print "There is a bear in here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False # threw error as f was lowercase in false
	
	while True: # make user loop till s/he gives a valid answer
		next = raw_input(prompt)
		
		if next == "take honey":
			dead("The bear looks at you and slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
				# and then return to the top of the 
				# infinite while loop
			
def cthulhu_room():
	"""The impossible level - Escaping Cthulhu's evil eye."""
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input(prompt)
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well, that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	"""Tell the deceased player why s/he died."""
	print why, "Good job!"
	exit(0)
	
def start():
	"""The game begins, in a dark room, with a terrfying choice: Left or Right... or a slow, slow death."""
	print "You are in a dark room."
	print "There is a door on your right and left."
	print "Which one do you take?"
	
	next = raw_input(prompt)
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()