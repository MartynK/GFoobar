# Marton Kiss 2015 - mrkmarton@gmail.com
# Problem by Google Foobar found on Github / rstuart85

"""
Backward and forward
The sign outside reads: Name no one man.

"Escape. We must escape." Staring at the locked door of his cage, Beta Rabbit, spy and brilliant mathematician,
has a revelation. "Of course! Name no one man - it's a palindrome! Palindromes are the key to opening this lock!"

To help Beta Rabbit crack the lock, write a function answer(n) which returns the smallest positive integer base b,
at least 2, in which the integer n is a palindrome. The input n will satisfy "0 <= n <= 1000."

Palindrome
==========
To help Beta Rabbit crack the lock, write a function answer(n) which returns the
smallest positive integer base b, at least 2, in which the integer n is a
palindrome. The input n will satisfy "0 <= n <= 1000".
Test cases
==========
Inputs:
    (int) n = 0
Output:
    (int) 2
Inputs:
    (int) n = 42
Output:
    (int) 4
Given a number n, return a base b where the number represented in that base is a palindrome.
"""

def check_palindrome(n):
	# Takes lists. if you want to serve strings, simply add: "n = str(n)"
	no_digits = len(n)
	# Now check	if it's a palindrome. If = 1: it is a palindrome
	palindrome = 1
	count = 0
	for i in n:
		if count >= no_digits/2: break
		if n[no_digits-count-1] != i: palindrome = 0
		count += 1
		
	return palindrome
	
def change_base(n,base):
	#Takes two numbers. Outputs list in reverse order.
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
	
def answer(n):
	for i in range(2,n+2):
		if check_palindrome(change_base(n,i)) == 1: return i
	return -1
	
###############

print answer(41)