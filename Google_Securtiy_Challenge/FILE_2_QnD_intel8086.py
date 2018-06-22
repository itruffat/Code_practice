import logging
from copy import deepcopy


# 	Explanation: 
# ---------------
#
# This is an extremely quick and dirty intel 8086 emulator.
#
# Since there are quite a few simplifications that can be taken with google's
# implementation (no real use of flags, no real use of small registries outside
# of nonzero tricks, etc.), this emulator only has the minimum required instructions.
#
# As such, it only does 4 operations (ror, xor, add, sub) and only uses 3 registries 
# (esi, ebp, edx) along with the stack.
#	 

# 	QnD emulator: 
# ---------------

class QnD_intel8086_like(object):
	def __init__(self):
		self.max_int = pow(2,32)
		self.stack = []
		self.regs = {"esi":0,"ebp":0,"edx":0, "stk": self.stack}
		#self.flags = {}
	
	def ror(self, reg, spaces):
		value = self[reg]
		treshold = 2 ** spaces
		left_side  = value // treshold
		right_side = value % treshold
		inverse_space = 32 - spaces
		shift = (2 ** inverse_space)
		right_side_shifted = right_side * shift 
		value = right_side_shifted + left_side
		self[reg] = value
	
	def adds(self, number1, number2):
		if isinstance(number2,str):
			number2 = self[number2]
		value = self[number1] + number2
		if value >= self.max_int:
			value -= self.max_int
		self[number1] = value

	def subs(self, number1, number2):
		if isinstance(number2,str):
			number2 = self[number2]
		value = self[number1] - number2
		if value < 0:
			value += self.max_int 
		self[number1] = value

	def xor(self, number1, number2):
		if isinstance(number2,str):
			number2 = self[number2]
		value = self[number1] ^ number2
		self[number1] = value
		
	def __getitem__(self, key):
		if key[:4] == "stk-":
			key = int(key[4:])
			return self.regs["stk"][key]
		else:
			return self.regs[key]
		
	def __setitem__(self, key, value):
		if key[:4] == "stk-":
			key = int(key[4:])
			self.regs["stk"][key] = value
		elif key == "stk":
			while self.stack: self.stack.pop()
			self.stack += value 
		else:
			self.regs[key] = value
			
	def stack_positions(self):
		for x in range(len(self.stack)):
			yield "stk-" + str(x)
		raise StopIteration  
			
	def unpack_stack(self):
		hexify = lambda x : lambda y: ''.join(['0' for _ in range(x - len(hex(y)[2:]))]) + hex(y)[2:] 
		hex_stack = list(map(hexify(8),self.stack))
		unpacked_stack = []
		for xs in reversed(hex_stack):
			unpacked_stack.append("")
			for p in range(len(xs)-1,0,-2):
				unpacked_stack[-1] += (xs[p-1] + xs[p]).upper()
		print(unpacked_stack)
		return unpacked_stack

	def clone(self):
		newclone = QnD_intel8086_like()
		newclone.max_int = self.max_int
		newclone.stack = deepcopy(self.stack)
		newclone.regs  = self.regs(self.regs)
		newclone.regs["stk"] = newclone.stack 
		return newclone


# 	Auxiliary functions: 
# ---------------

def number_is_ascii(i, q = 1):
	ascii_min = int16("0x20")
	ascii_max = int16("0x7E")
	for x in range(q):
		ti = i%256
		if ti < ascii_min or ascii_max < ti:
			return False  
		i= i//256
	return True
	
int16     = lambda x:  int(x,16)	


# 	Main Google Function: 
# ---------------

hardcoded_values = ["0xe06cafbd", "0xde8d7d56", "0x47874e62", "0x65974452", "0x7e8d424b", "0x3e59ec52", "0xab38aea6", "0x504d26ed",  "0x1e674b49", "0x254da584", "0x5449681c", "0xa19b108e", "0xada96c07"]

def simplifiedGoogleCode(hardcoded_values, first_esi, force_ascii_stack = True):
	x86 = QnD_intel8086_like()
	x86["esi"] = first_esi
	x86["edx"] = 0
	x86["ebp"] = int16("0x474f4f47")
	x86["stk"] = list(map(lambda x:int16(x),hardcoded_values))
	for stk in x86.stack_positions():
		x86.xor(stk,"esi")
		x86.adds("edx",4)
		x86.xor("ebp","esi")
		x86.ror("ebp",3) 
		x86.subs("ebp","edx")
		x86.xor("esi","ebp")
		if force_ascii_stack and not number_is_ascii(x86[stk],4):
			return None 
	return x86.unpack_stack()

simplifiedGoogleCode(hardcoded_values,int16("0xc001c0de"),True)
