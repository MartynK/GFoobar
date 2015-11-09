# Marton Kiss 2015 - mrkmarton@gmail.com
# Problem by Google Foobar found on Github / rtheunissen

"""
Minglish lesson
===============
Welcome to the lab, minion. Henceforth you shall do the bidding of Professor
Boolean. Some say he's mad, trying to develop a zombie serum and all... but we
think he's brilliant!
First things first - Minions don't speak English, we speak Minglish. Use the
Minglish dictionary to learn! The first thing you'll learn is how to use the
dictionary.
Open the dictionary. Read the page numbers, figure out which pages come before
others. You recognize the same letters used in English, but the order of letters
is completely different in Minglish than English (a < b < c < ...).
Given a sorted list of dictionary words (you know they are sorted because you
can read the page numbers), can you find the alphabetical order of the Minglish
alphabet?
For example, if the words were ["z", "yx", "yz"] the alphabetical order would be
"xzy," which means x < z < y. The first two words tell you that z < y, and the
last two words tell you that x < z.
Write a function answer(words) which, given a list of words sorted
alphabetically in the Minglish alphabet, outputs a string that contains each
letter present in the list of words exactly once; the order of the letters in
the output must follow the order of letters in the Minglish alphabet.
The list will contain at least 1 and no more than 50 words, and each word will
consist of at least 1 and no more than 50 lowercase letters [a-z].
It is guaranteed that a total ordering can be developed from the input provided,
(i.e. given any two distinct letters, you can tell which is greater),
and so the answer will exist and be unique.
"""

from copy import deepcopy

def readcsv(file):
	out = []
	for i in file:
		out += [i]
	return out
	
def getfirst(list):
	actual = []
	updatelist = []
	kluster = []
	for i in list:
		actual += i[0].lower()
		updatelist += [i[1:]]
		if len(actual) == 1:
			kluster += [[updatelist[0]]]
		else:
			if actual[-1] == actual[-2]:
				kluster[-1].append(updatelist[-1])
			else:
				kluster.append([updatelist[-1]])
	out = []
	for i in kluster:
		if len(i) > 1:
			out += [i]
	return actual,out
	
def klean(list):
	out = []
	for i in range(len(list)):
		if out == []:
			out += [list[i]]
		else:
			if out[len(out)-1] != list[i]: out.append(list[i])
	return out

def ribbons(words):
	bklean,out = getfirst(words)
	array = [klean(bklean)]
	array2 = []
	
	while True:
		if out == []:
			break
		else:
			for i in out:
				bklean,outt = getfirst(i)
				if len(klean(bklean)) > 1:
					array += [klean(bklean)]
				array2 += [outt]
		out = []
		out = outt
	return array

def letterlist(list):
	ll = []
	for i in list:
		for j in i:
			if j not in ll:
				ll += [j]
	return ll
		
def before(list):
	#do letter list
	ll = letterlist(list)
	b4list = []
	for i in ll:
		b4 = []
		for j in list:
			switch = 0
			for k in j:
				if switch and k not in b4: b4 += [k]
				if k == i: switch = 1
		b4list += [b4]
		
	return b4list
	
def check(list):
	ll = letterlist(list)
	b4l = before(list)
	processed = []
	out = []
	for i in range(len(ll)):
		counter = 0
		for j in b4l:
			if j == []:
				out += ll[counter]
				b4l.remove(j)
				ll.remove(ll[counter])
				b4l = kleaning(b4l,out)
			counter += 1
	return out[::-1]
	
def kleaning(list,excl):
	out = deepcopy(list)
	for i in range(len(list)):
		for j in list[i]:
			if j in excl:
				out[i].remove(j)
	return out
			
def answer(list):
	return check(ribbons(list))
	
#########
#file = open("minglis.csv")
#print ribbons(readcsv(file))
#str = [["a","b"],["x","a"],["a","d"],["a","c"],["b","d"],["b","c"],["c","d"]]
str = ["axaabbc","axaabbd","axaabc","axaad","axac","axd","aa","b"]
print answer(str)
