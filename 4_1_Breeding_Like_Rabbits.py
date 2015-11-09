# Marton Kiss 2015 - mrkmarton@gmail.com
# Problem by Google Foobar found on Github / rstuart85
# Fact: In Greek mythology Daedalus developed wings for himself for flight
#		so a group of minotaurs would stop teasing him about it.

"""
Breeding like rabbits
=====================
As usual, the zombie rabbits (zombits) are breeding... like rabbits! But instead of following the Fibonacci sequence
like all good rabbits  do, the zombit population changes according to this bizarre formula, where R(n) is the number of
zombits at time n:
R(0) = 1
R(1) = 1
R(2) = 2
R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)
(At time 2, we realized the difficulty of a breeding program with only one zombit and so added an additional zombit.)
Being bored with the day-to-day duties of a henchman, a bunch of Professor Boolean's minions passed the time by playing
a guessing game: when will the zombit population be equal to a certain amount? Then, some clever minion objected that
this was too easy, and proposed a slightly different game: when is the last time that the zombit population will be
equal to a certain amount? And thus, much fun was had, and much merry was made.
(Not in this story: Professor Boolean later downsizes his operation, and you can guess what happens to these minions.)
Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n
such that R(n) = S. Return the answer as a string in base-10 representation. If there is no such n, return "None". S
will be a positive integer no greater than 10^25.
"""

class Memoize:
	def __init__(self,func):
		self.memo = {}
		self.func = func
		
	def __call__(self,*args):
		if args not in self.memo:
			self.memo[args] = self.func(*args)
		return self.memo[args]

@Memoize
def rabbit(x):
	if x == 0:
		out = 1
	elif x == 1:
		out = 1
	elif x == 2:
		out = 2
	else:
		tn = x
		n = tn/2.0
		if tn/2 == n:
			#even
			n = tn/2
			out = rabbit(n) + rabbit(n+1) + n
		else:
			#odd
			n = tn/2
			out = rabbit(n-1) + rabbit(n) + 1
	return out
	
def odd(x):
	y = x/2.0
	if x/2-y == 0:
		return 0
	else:
		return 1
	return -1	# Something went wrong
	
def checksmallser(x,lowint = 1,highint = 0,oddity = 2):
	if oddity == 2:
		#first run
		highint = x
		oddity = odd(x)
		if oddity == 0: highint += 1
	
	halfpoint = (((lowint-1)/2+(highint-1)/2)/2)*2+1

	#inspect halfpoint
	candidate = rabbit(halfpoint)
	if candidate == x:
		return halfpoint
	elif candidate > x:
		diff = highint
		highint = halfpoint
		diff -= highint
	elif candidate < x:
		diff = lowint
		lowint = halfpoint
		diff -= lowint
	
	#stopping criterion
	if lowint == x:
		return lowint
	elif highint == x:
		return highint
	elif lowint == highint:
		return lowint
	elif highint - lowint < 3 and diff == 0:
		return lowint
	elif diff != 0:
		# Recursion!
		return checksmallser(x,lowint,highint,oddity)

	return lowint
	
def checkbigser(x,lowint = 0,highint = 0,oddity = 2):
	#even indexes
	#first run
	if oddity == 2:
		#first run
		highint = x
		oddity = odd(x)
		if oddity == 1: highint += 1
	
	halfpoint = ((lowint/2+highint/2)/2)*2
	#inspect halfpoint
	candidate = rabbit(halfpoint)
	if candidate == x:
		return halfpoint
	elif candidate > x:
		diff = highint
		highint = halfpoint
		diff -= highint
	elif candidate < x:
		diff = lowint
		lowint = halfpoint
		diff -= lowint
	
	#stopping criterion
	if lowint == x:
		return lowint
	elif highint == x:
		return highint
	elif lowint == highint:
		return lowint
	elif highint - lowint < 3:
		return lowint
	else:
		#raw_input()
		return checkbigser(x,lowint,highint,oddity)
	
	# Don't expect this to run
	return lowint,highint	

def answer(x):
	smal = checksmallser(x)
	if rabbit(smal) == x:
		return smal
	else:
		#no smallser answer
		big = checkbigser(x)
		if rabbit(big) == x:
			return big
		else:
			#No joy
			return -1
	
######
test = 2914

print answer(test)