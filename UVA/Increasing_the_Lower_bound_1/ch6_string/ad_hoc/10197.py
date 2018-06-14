# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=204&page=show_problem&problem=1138
###
### Config data
###-

import os
from math import *
from copy import deepcopy

example_test= """falar talk
compor compose
andar walk"""

exec(open("../../_auxiliary/input_iterators.py").read())

line = input_iter(True, "")
#line = string_iter()

fobject = None
pend = None

check_with_oracle = False

###
### Oracle Definition
###
	
def oracle_generate_answer(n):
	return None

###
### Solution
###
		
pronouns = ["eu", "tu", "ele/ela", "n"+ chr(243) + "s", "v" + chr(243) + "s", "eles/elas"]
pronouns = list(map(lambda s: s + " " * (10 - len(s)), pronouns))		

x    = {"ar":"a" , "er":"e" , "ir":"e"}
xis  = {"ar":"ais", "er":"eis", "ir":"is"}
xmos = {"ar":"amos", "er":"emos", "ir":"imos"}


def resolve(port,eng):
	answer = []
	answer.append("{} (to {})".format(port,eng))
	
	body = port[:-2]
	tail = port[-2:]
	if tail not in ["ar","er","ir"]:
		answer.append("Unknown conjugation")
	else:
		answer.append(pronouns[0] + body + "o"			)
		answer.append(pronouns[1] + body + x[tail] + "s")
		answer.append(pronouns[2] + body + x[tail]		)
		answer.append(pronouns[3] + body + xmos[tail]	)
		answer.append(pronouns[4] + body + xis[tail]	)
		answer.append(pronouns[5] + body + x[tail] + "m")
	return answer 
		
###
### Oracle Confirmation
###


if check_with_oracle:
	pass
			
### Run
###

port, eng = next(line).split()
for answer in resolve(port,eng):
	print(answer)
		
while True:
	try:
		port, eng = next(line).split()
	except StopIteration:
		break
	except Exception as e:
		raise e
	print("")
	for answer in resolve(port,eng):
		print(answer)
