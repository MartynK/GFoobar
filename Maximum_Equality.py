# Marton Kiss 2015 - mrkmarton@gmail.com
# Problem by Google Foobar found at
# http://code.runnable.com/VRiAkt8IeEMM6NB9/maximum-number-of-equal-elements-in-array-for-python-google-foobar-and-googlefoobar

"""
Maximum equality
Your colleague Beta Rabbit, top notch spy and saboteur, has been working tirelessly to discover a way to break into Professor
Boolean's lab and rescue the rabbits being held inside. He has just excitedly informed you of a breakthrough - a secret bridge
that leads over a moat (likely filled with alligators, or zombies, or alligator-zombies, given his penchant for zombifying...
You should probably stop thinking about it.). The only way over the moat is by a rickety train, but there's a catch: The train
is rigged such that under particular conditions, it will throw its passengers overboard. You've determined that the best odds
of getting safely across is to have as many cars share the same exact weight as possible. Luckily, all the rabbits' weights
are essentially equal. How convenient!

The rabbits are already organized into families, but these families vary in size. In order for this plan to work, you need
to find a way to make as many train cars as possible have exactly the same number of passengers.

Beta Rabbit will provide you with an array x, where each element in the array is an integer representing the number of
rabbits that want to share a particular car. You can give the command for a rabbit to move from any one car to any other,
and you have enough time to give as many commands as you need. In other words, choose two elements of the array, x[i] and
x[j] (idistinct fromj) and simultaneously increment x[i] by 1 and decrement x[j] by 1. Your goal is to get as many elements
of the array to have equal value as you can.

For example, if the array was [1,4,1] you could perform the operations as follows:

Send a rabbit from the 1st car to the 0th: increment x[0], decrement x[1], resulting in [2,3,1] Send a rabbit from the 1st
car to the 2nd: increment x[2], decrement x[1], resulting in [2,2,2].

All the elements are of the array are equal now, and you've got a strategy to report back to Beta Rabbit!

Note that if the array was [1,2], the maximum possible number of equal elements we could get is 1, as the cars could never
have the same number of rabbits in them.

Write a function answer(x), which takes the array of integers x and returns the maximum number of equal array elements that
we can get, by doing the above described command as many times as needed.

The number of cars in the train (elements in x) will be at least 2, and no more than 100. The number of rabbits that want to
share a car (each element of x) will be an integer in the range [0, 1000000].
"""

# Cheeky problem... n-1 equal wagons are possible in every case (all has one rabbit inside, last has the rest)
# n equal wagons can be achieved if average number of rabbits in every wagon doesn't leave any rabbits out.
# Classic O(n) solution would be to equalize the outliers and see what's left.


def answer_classic(list):
	""" Imperative approach """
	if list == []: return 0
	stop = 0
	while stop == 0:
		max_element = max(list)
		min_element = min(list)
		diff = max_element - min_element
		if diff < 2:
			stop = 1
		else:
			maxindex = list.index(max_element)
			minindex = list.index(min_element)
			list[maxindex] -= diff/2
			list[minindex] += diff/2
	# now all items differ at most by 1
	a = None
	a_count = 0
	b = None
	b_count = 0
	for i in list:
		if a == None: 
			a = i
			a_count += 1
		elif b == None and a != i:
			b = i
			b_count += 1
		else:
			if i == a:
				a_count += 1
			elif i == b:
				b_count += 1
			else:
				print "something went horribly wrong"
	if b_count == None:
		return a_count
	else:
		return a_count + b_count -1
		
def answer(list):
	""" Functional approach """
	if list == []: return 0
	summa = sum(list)
	averag = summa/len(list)
	if averag * len(list) != summa:
		return len(list) - 1
	else:
		return len(list)
		
######
		
print answer([1,7,8,5,2])