# Marton Kiss 2015 - mrkmarton@gmail.com
# Problem by Google Foobar found on Github / rstuart85
# Fact: The first man who figured out that cowmilk is drinkeable was very very thirsty.

"""
Spy snippets
============
You've been recruited by the team building Spy4Rabbits, a highly advanced search engine used to help fellow agents
discover files and intel needed to continue the operations against Dr. Boolean's evil experiments. The team is known for
recruiting only the brightest rabbit engineers, so there's no surprise they brought you on board. While you're elbow
deep in some important encryption algorithm, a high-ranking rabbit official requests a nice aesthetic feature for the
tool called "Snippet Search."  While you really wanted to tell him how such a feature is a waste of time in this
intense, fast-paced spy organization, you also wouldn't mind  getting kudos from a leader. How hard could it be, anyway?
When someone makes a search, Spy4Rabbits shows the title of the page. Your commander would also like it to show a short
snippet of the page containing the terms that were searched for.
Write a function called answer(document, searchTerms) which returns the shortest snippet of the document, containing all
of the given search terms. The search terms can appear in any order.
The length of a snippet is the number of words in the snippet. For example, the length of the snippet "round fluffy
rabbit tails" is 4. (Hey, don't judge your colleagues for what they search in their spare time).
The document will be a string consisting only of lower-case letters [a-z] and spaces. Words in the string will be
separated by a single  space. A word could appear multiple times in the document. searchTerms will be a list of words,
each word comprised only of lower-case letters [a-z]. All the search terms will be distinct.
Search terms must match words exactly, so "hop" does not match "hopping".
Return the first sub-string if multiple sub-strings are shortest. For example, if the document is "world there hello
hello where world" and the search terms are ["hello", "world"], you must return "world there hello".
The document will be guaranteed to contain all the search terms.
The number of words in the document will be at least one, will not exceed 500, and each word will be 1 to 10 letters
long. Repeat words in  the document are considered distinct for counting purposes.
The number of words in searchTerms will be at least one, will not exceed 100, and each word will not be more than 10
letters long.
"""

####################

def make_list(words):
	return words.split(" ")

def look_4_complete(words,document,position):
	out = []
	set = []
	next = 0
	for i in range(position,len(document)):
		act_word = document[i]
		out += [act_word]
		if (act_word in words) == 1:
			if act_word not in set:
				set += [act_word]
				if next == 0 and len(set) != 1: next = i
				if len(set) == len(words): return out,next
			else:
				# If you have the same word "n" times, you only have to do the next
				# cycle involving the word from the last one.
				# Cannot do below with "and" because of IndexError
				if len(set) == 1:
					if document[i-1] == document[i]: next = i
	#reached EOF, still no complete list
	return -1
	
	
def answer(document,search_terms):
	document = make_list(document)
	search_terms = make_list(search_terms)
	
	# Using this var to detect if at least one word from search_terms is in document.
	position = -1
	for i in range(len(document)):
		if document[i] in search_terms:
			position = i
			break
	if position == -1: print "you are cheating... or I am WRONG!"

	# Based on the problem above, if going to extend sizes, please adjust accordingly.
	min = 500
	min_snippet = []
	
	while True:
		instance = look_4_complete(search_terms,document,position) #[0]: snippet; [1]: next word
		print search_terms,position,instance	#DEBUG INFO
		#Stopping criterion: end of document - cannot find all search terms until EOF
		if instance == -1: break
		#Going to call this two times so it looks nicer and is theoretically faster this way.
		cand = len(instance[0])
		if cand < min:
			min = cand
			min_snippet = instance[0]
		#Early stopping criterion: best possible solution
		if min == len(search_terms): return instance[0]
		position = instance[1]
	
	# Adjusting output to meet specifications
	out = ""
	for i in min_snippet:
		out += str(i)+" "
	# Getting rid of last space
	out = out[:-1]
	# I'm just getting silly here... The problem specified I have to return the snippet
	# in apostrophies...
	out = "\"" + out + "\""
	
	return out

#####################

print answer("dog world there fluffy bunny hello hello tails there world","hello world")