# Marton Kiss 2015 - mrkmarton@gmail.com
# Problem by Google Foobar found on Github / rstuart85
# Fact: Edmund Hillary who climbed Mount Everest for the first time did so accidentally
#		while chasing a bird.

"""
Fix my phone, minion!
=====================
"She escaped? This can't be happening! Get me the security team!"
Professor Boolean, a notorious mad scientist, just found out his precious rabbit specimen has escaped! He rushes to call
his security minions on the lab phone. However, the rabbit escapee hacked the phone to speed her escape! She left a sign
with the following clues: Each digit that is dialed has to be a number that can be reached by a knight chess piece from
the last digit dialed - that is, you must move precisely 2 spaces in one direction, and then 1 space in a perpendicular
direction to dial the next correct number. You can dial any number you want to start with, but subsequent numbers must
obey the knight's move rule.
The lab phone has the numbers arranged in the following way: 1, 2, 3 in the first row; 4, 5, 6 in the second row; 7, 8,
9 in the third row; and blank, 0, blank in the fourth row.
123
456
789
 0
For example, if you just dialed a 1, the next number you dial has to be either a 6 or an 8.  If you just dialed a 6, the
next number must be a 1 or 7.
Professor Boolean wants you to find out how many different phone numbers he can dial under these conditions. Write a
function called answer(x, y, z) that computes the number of phone numbers one can dial that start with the digit x, end
in the digit y, and consist of z digits in total. Output this number as a string representing the number in base-10.
x and y will be digits from 0 to 9. z will be between 1 and 100, inclusive.
"""

# Original verion can handle a length of ~120.
# If you wish to increase that, use the lines
# below. Be advised, it could cause system
# instability so be careful and watch out
# for your RAM (stack overload)!

# from sys import setrecursionlimit
# setrecursionlimit(1500)

class Memoize:
	def __init__(self,function):
		self.memo = {}
		self.function = function
	
	def __call__(self,*args):
		if args not in self.memo:
			self.memo[args] = self.function(*args)
		return self.memo[args]
		
def rules():
	# Lists all possibilities from a given number
	# reached via knight's move (because I can).
	# Sorry, list looks a bit funny, but this way,
	# no IndexErrors. Trust me, looks better than
	# handling every exception.
	a = -1
	list = [[a,a,a,a,a,a,a],
			[a,a,a,a,a,a,a],
			[a,a,1,2,3,a,a],
			[a,a,4,5,6,a,a],
			[a,a,7,8,9,a,a],
			[a,a,a,0,a,a,a],
			[a,a,a,a,a,a,a],
			[a,a,a,a,a,a,a]]
	
	new_dic = {}
	for i in range(len(list)):
		for j in range(len(list[0])):
			possibility = []
			if list[i][j] != -1:
				if list[i-2][j-1] != -1: possibility += [list[i-2][j-1]]
				if list[i-2][j+1] != -1: possibility += [list[i-2][j+1]]
				if list[i-1][j-2] != -1: possibility += [list[i-1][j-2]]
				if list[i-1][j+2] != -1: possibility += [list[i-1][j+2]]
				if list[i+1][j-2] != -1: possibility += [list[i+1][j-2]]
				if list[i+1][j+2] != -1: possibility += [list[i+1][j+2]]
				if list[i+2][j-1] != -1: possibility += [list[i+2][j-1]]
				if list[i+2][j+1] != -1: possibility += [list[i+2][j+1]]
				new_dic[list[i][j]] = tuple(possibility)
				
	return new_dic

def answer(begin,end,length):
	# I tried so hard not to pollute global namespace...
	# If I try to pass the dict to "dial()", but have to
	# "pickle" the memoization process and it would hurt
	# efficiency (a bit).
	global rules_dict
	rules_dict = rules()
	return dial(begin,end,length)

@Memoize
def dial(begin,end,length):
	if length == 1: return 0
	if length == 2:
		if end not in rules_dict[begin]:
			return 0
		else:
			return 1
			
	combinations = 0
	for i in rules_dict[begin]:
		combinations += dial(i,end,length-1)
	return combinations
	
##################

print answer(2,3,120)