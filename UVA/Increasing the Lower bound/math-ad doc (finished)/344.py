#https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=162&page=show_problem&problem=280

###
### Config data
###

import os
from math import floor, ceil, log

example_test= """1
2
20
99
0"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()


fobject = None
pend = None

check_with_oracle = False

###
### Oracle Definition
###

def oracle_generate_answer(n):
	dic = {"i":0,"v":0,"x":0,"l":0,"c":0}
	for x in range(1, n+1):
		roman = list(roman_number(x))
		for k in dic.keys():
			dic[k] += roman.count(k)
	return(dic)


def roman_number(num): # Disclaimer: this was downloaded from stackoverflow
    num_map = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'), (90, 'xc'),
           (50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]
    answer = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                answer += r
                num -= i
    return answer

###
### Solution
###

def resolve(n):
	dic = {"i":[],"v":[],"x":[],"l":[],"c":[]}
	
	#i 
	dic["i"].append(int((n+1)/5) * 7)  		#every_i_until_last_4_or_9 
	dic["i"].append(sum(range(((n+1)%5)))) 	#i_leftovers_who_didnt_reach_4_or_9
	
	#v 
	dic["v"].append(int((n+6)/10))			#every_v_representing_4 
	dic["v"].append(int((n+1)/10) * 4)		#every_v_representing_from_5_to_9
	dic["v"].append(max(((n%10)%9)-4,0))	#v_leftovers_bigger_than_4_who_didnt_reach_9
	
	#x 
	dic["x"].append(int(n/50) * 70)			#every_x_in_a_block_of_50_except_9s
	dic["x"].append(int((n+1)/10))			#every_x_representing_9 
	dic["x"].append((sum(range(int((n%50)/10)))) * 10)	#every_x_from_blocks_of_10_smaller_than_the_current_one
	dic["x"].append(abs((((int((n%50)/10))%5 + 1)%5) - 1) * ((n % 50 % 10)+1)) #every_x_from_current_block_of_10 
	
	#l
	dic["l"].append(int(n/100) * 50) 		#every_l_from_blocks_of_100_smaller_than_the_current_one
	dic["l"].append(max((min((n%100),89)) - 39, 0)) #every_l_from_the_current_block_of_100
	
	#c
	dic["c"].append(max(n%100 - 89, 0))		#every_c_from_the_current_block_of_100_thats_representing_90
	dic["c"].append(((n%100) + 1) * int((n)/100))	#every_c_from_the_current_block_of_100_except_90s
	dic["c"].append(int((n)/100) * 10)		#every_c_from_blocks_of_100_smaller_than_the_current_one_representing_90
	dic["c"].append(sum(range(int(n/100))) * 100) 	#every_c_from_blocks_of_100_smaller_than_the_current_one_except_90s
	
	for key,val in dic.items():
		dic[key] = sum(val)
	return dic
			
###
### Oracle Confirmation
###

if check_with_oracle:
	for x in range(1, 301,1):
		if resolve(x) != oracle_generate_answer(x):
			print("\nValue:{}\n~~~~~~\nExpected:  {}\n--------- \n Result :  {}".format(x,oracle_generate_answer(x),resolve(x)))
			break

###
### Run
###
next_value = int(next(line))

while next_value != 0:
	dic = resolve(next_value)
	print("{inp}: {i} i, {v} v, {x} x, {l} l, {c} c".format(inp =next_value, **dic), end = pend)
	next_value = int(next(line))
