from time import time
from FILE_2_QnD_intel8086 import *

# 	Auxiliary functions: 
# ---------------

#divide a 64 bits number (in hex) into a list of 4 16 bits numbers in hex 
hex_div   = lambda x: [(x[2+y*2:4+y*2]) for y in range(len(x[2:])//2)  ]
#transform a 64 bits number (in hex) into a list of 4 ASCII chars 
hex_chr   = lambda x: [chr(int16("0x{}".format(y))) for y in hex_div(x)]


# 	Guessing First-ESI: 
# --------------- 
#
# We could technically bruteforce every potential value of ESI and filter
# only the ASCII legal results. However, that would take far too long.
# To make things faster, the right answer is to work with an smaller search space.
#
# My first meassure was to ensure that the result of the first use of the ESI 
# operation would always result in an ASCII legal value. That still leaves us 
# with a huge search space (81 billions cases), but far more constrained and 
# feasable than inspecting the whole space. (4 trillion cases) 
#
# Getting an answer from this search space took me about 50 minutes.
# 
# Any reduction of the search space beyond that can lead potentially lead to a
# miss, since any omitted character could be part of the final answer.
#
# However, it makes sense to at least make a few attempts with smaller search
# spaces in parallel. For example, using constrains like "has no symbols", 
# "only lowercase" or "no uppercase". That's because those cases can be  
# completely in trivial time (since the algorithm has exponential complexity).
#
# In this case, by looking at "no symbols, no uppercase", I could get the answer
# in less than 90 seconds.

def explore_search_space(search_space):
	for byte_0 in search_space[0]:
		i0 = byte_0 * pow(16, 6) 
		for byte_1 in search_space[1]:
			i1 = i0 + byte_1 * pow(16, 4)
			for byte_2 in search_space[2]:
				i2 = i1 + byte_2 * pow(16, 2)
				for byte_3 in search_space[3]: 
					yield(i2 + byte_3)

def filter_search_space_after_xor(xor_mask, search_space, filter_criterion): 
	characters = list(map(int16,hex_div(xor_mask)))
	chosen_candidates    = [list() for _ in range(4)]
	for x in range(4):
		for pc in search_space[x]:
			if filter_criterion(pc ^ characters[x]):
				chosen_candidates[x].append(pc)
	return chosen_candidates

def search(search_space):
	file_output  = open("output.txt","w")
	case = 0
	for esi in explore_search_space(search_space):
		answer = simplifiedGoogleCode(hardcoded_values, esi, True)
		if answer is not None:
			text = ''.join(list(map(lambda y: ''.join(hex_chr("0x" + y)), answer)))
			print("Case[{}]+ESI[{}]:\nText:{}\nStack:{}".format(case,esi,text,answer))
			print("Case[{}]+ESI[{}]:\nText:{}\nStack:{}".format(case,esi,text,answer), file = file_output)
		case+=1
	print("Ended after case[{}]".format(case))
	file_output.close()

				
# 	Filter Criterions: 
# ---------------

def char_is_ascii(char):
	return number_is_ascii(char)

def char_is_not_symbol(char):
	symbol_ascii_chars = list(map(ord,["\\", "/", "|", "~","`","'",'"',"!","?","*","&","^","%","$","#","=","<",">",":",";","_","(",")","[","]","{","}","+","-",".",","]))
	return char not in symbol_ascii_chars
	
def char_is_not_upper(char):
	return chr(char).lower() == chr(char)


# 	Running the code: 
# ---------------

full_search_space = [list(range(int16("0xFF")+1)) for _ in range(4)]
# I AM UNAWARE HOW LONG IT WOULD TAKE TO MAKE THIS SEARCH
reduced_search_space = filter_search_space_after_xor(hardcoded_values[0],full_search_space, char_is_ascii)
# DOING THE SEARCH HERE WOULD TAKE ME ABOUT 50 MINUTES
reduced_search_space = filter_search_space_after_xor(hardcoded_values[0],reduced_search_space, char_is_not_symbol)
reduced_search_space = filter_search_space_after_xor(hardcoded_values[0],reduced_search_space, char_is_not_upper)
# AND HERE ABOUT 90 SECONDS
search(reduced_search_space)
