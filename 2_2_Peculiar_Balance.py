# Marton Kiss 2015 - mrkmarton@gmail.com
# Problem by Google Foobar found on Github / rstuart85
# Fact: Man can survive underwater. But not for very long.

"""
Peculiar balance
================
Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure - but there's an
obstacle. The  door will only open if a challenge is solved correctly. The future of the zombified rabbit population is
at stake, so Beta reads the  challenge: There is a scale with an object on the left-hand side, whose mass is given in
some number of units. Predictably, the task is to  balance the two sides. But there is a catch: You only have this
peculiar weight set, having masses 1, 3, 9, 27, ... units. That is, one  for each power of 3. Being a brilliant
mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced  exactly using this set.
To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where the
weights should be  placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.
The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight,
and so on. Each  string is one of:
"L" : put weight on left-hand side
"R" : put weight on right-hand side
"-" : do not use weight
To ensure that the output is the smallest possible, the last element of the list must not be "-".
x will always be a positive integer, no larger than 1000000000.
"""

# Legacy function from 1_1. Lists number in base-3, reverse order
def change_base(n,base=3):
	#Takes two numbers. Outputs list.
	actual = base
	stop = 0
	out = []
	# max(n) = 10k, min(base) = 2, ergo we need max 14 iterations.
	# if you want to increase max(n), mae "14" bigger or, if all fails
	# use a while loop.
	act_divider = 1
	for i in range(14):
		#Stopping criterion
		if n< base:
			out += [n]
			break
		out += [n % base]
		n = n/base
	return out	
	
# For every "digit", determines where the weight should go.
def answer(W):
	list  = change_base(W)
	rem   = 0
	left  = 0
	right = 0
	out   = []
	for num in list:
		if num == 0:
			if rem == 0: out += ["-"]
			elif rem == 1: out += ["R"]
		elif num == 1:
			if rem == 0: out += ["R"]
			elif rem == 1: out += ["-"]	
		elif num == 2:
			if rem == 0: out += ["L"]; rem = 1
			elif rem == 1: out += ["-"]; rem = 1
	
	#If the last digit produced a total of "3", you need an additional weight
	#If  you couldn't do that, we could do this in binary
	if rem == 1:
		out += "R"

	return out
 
################
 
print answer(190000000)