
"""
When it rains it pours
======================
It's raining, it's pouring. You and your agents are nearing the building where
the captive rabbits are being held, but a sudden storm puts your escape plans at
risk.
The structural integrity of the rabbit hutches you've built to house the
fugitive rabbits is at risk because they can buckle when wet. Before the rabbits
can be rescued from Professor Boolean's lab, you must compute how much standing
water has accumulated on the rabbit hutches.
Specifically, suppose there is a line of hutches, stacked to various heights and
water is poured from the top (and allowed to run off the sides). We'll assume
all the hutches are square, have side length 1, and for the purposes of this
problem we'll pretend that the hutch arrangement is two-dimensional.
For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3]:
...X...
.X.X...
.X.X..X
.XXX.XX
XXXXXXX
1425123
When water is poured over the top at all places and allowed to runoff,
it will remain trapped at the 'O' locations:
...X...
.XOX...
.XOXOOX
.XXXOXX
XXXXXXX
1425123
The amount of water that has accumulated is the number of Os,
which, in this instance, is 5.
Write a function called answer(heights) which, given the heights of the stacked
hutches from left-to-right as a list, computes the total area of standing water
accumulated as water is poured from the top and allowed to run off the sides.
The heights array will have at least 1 element and at most 9000 elements.
Each element will have a value of at least 1, and at most 100000.
"""

def slice(list):
	if len(list) == 0: return 0,0,0,0
	maxi = list.index(max(list))
	return list[:maxi],list[maxi+1:],list[maxi],maxi
	
def flow(list,upp = []):
	if upp == []: upp = [0 for i in list]
	summit = slice(list)

	if summit[0] != []:
		left = slice(summit[0])
		if left[1] != []:	
			for i in range(left[3]+1,summit[3]):
				upp[i] = left[2]	
			remainleft = [left[0],left[3]]
			upleft = flow(remainleft[0]+[summit[2]])
			for i in range(len(upleft)):
				upp[i] = upleft[i]			
			
	if summit[1] != []:
		right = slice(summit[1])
		if right[0] != []:
			for i in range(summit[3]+1,summit[3]+right[3]+1):
				upp[i] = right[2]
			remainright = [right[1],summit[3]+right[3]+1]
			upright = flow([summit[2]]+remainright[0])
			diff = len(upp) - len(upright)	
			for i in range(len(upright)):
				upp[i+diff] = upright[i]				
	return upp
	
	
def answer(list):
	listtu = flow(list)
	out = 0
	for i in range(len(listtu)):
		if listtu[i] != 0: out += listtu[i]-list[i]
		#print list[i],listtu[i]	#DEBUG INFO
	return out


#####################
data = [6,4,5,9]
print answer(data)