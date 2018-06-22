from itertools import chain
from copy import deepcopy

# 	Code generator using templates: 
# ---------------

# Explanation:
# ------------
# The idea was to create a piece of code that printed the stack.
# With the path of least resistance being to create code recyling small
# snippets iteratively, I made a class that quickly allowed me to do that.
#
# The class "code template" picks up a string and "resolves" it in two ways:
#
# A. Unloop: 
#		The object has a list of instances. For each instance, it repeats the string, replacing 
#		the numbered tags for their respective value. This makes repetition easy to write and debug.
# 		Example: 	<<String: "Add {0}, {1}" List: [W,X],[Y,Z] >>
#		Result:		<<"Add W, X 
#					   Add Y, Z" >> 
# B. Replace:
#		It replaces the missing tags with strings or "code templates". If it's a code template
#		it will also resolve itself before giving a result. This makes code segmentation easy.
 
class code_template(object):
	
	def __init__(self, body = ""):
		self.body = body
		self.dic = {}
		self.array = []
	
	def set_unlooping_vars(self,array):
		self.array = array
	
	def include(self,value,key):
		self.dic[key] = value
	
	def unloop_body(self):
		generated_body = self.body
		if self.array:
			generated_body = ""
			for line in self.array:
				if type(line) is not list:
					line = [line]
				generated_body += self.body.format(*line)
		return generated_body
	
	def resolve(self, final = True):
		new_dic = {}
		answer = self.unloop_body()
		for key,val in self.dic.items():
			if type(val) is not str:
				val = val.resolve(False)
			new_dic[key] = val
		answer = answer.format(**new_dic) 
		if final:
			answer = self.add_indent(answer)
		return answer
		
	def add_line(self, line, number):
		new_body = self.body.split("\n")
		new_body.insert(number, line)
		self.body = '\n'.join(new_body)
		
	def change_line(self, line, number):
		new_body = self.body.split("\n")
		new_body[number] = line
		self.body = '\n'.join(new_body)
	
	def add_indent(self, string): # This function properly indents the strings
		new_string = []
		for i in string.split("\n"):
			indent = ""
			if i[:7] != "section" and i[-1:] != ":":
				indent = "    "
			new_string.append(indent + i + "\n")
		new_string[-1] = new_string[-1][:-1]
		return ''.join(new_string)


# 	Original Google Function 
# (written with the code generator module): 
# ---------------

current_code = list((code_template() for _ in range(6)))				
main,prelude,back,forward, push_lines,post = current_code

main.include(prelude,"prelude")
main.include(back   ,"back"   )
main.include(forward,"forward")
main.include(post   ,"post"   )
back.include(push_lines, "plines")

main.body = \
"""{prelude}
jmp _forward
_back:
{back}
_forward:
call _back
{forward}
{post}"""

prelude.body = \
"""section	.text
global _start
_start:"""

back.body = \
"""pop edi
push byte 4
pop eax
cdq
mov ebx, edx
inc ebx
mov ebp, 0x474f4f47
{plines}mov ecx, esp
int 0x80
mov eax, ebx
int 0x80"""

forward.body = \
"""xor [esp+4],esi
add edx, 4
xor ebp, esi
ror ebp, 3
sub ebp, edx
xor esi, ebp
ret"""

post.body = \
""""""

push_lines.body = \
"""push {0}
call edi
"""

pushes = [	"0xe06cafbd", "0xde8d7d56", "0x47874e62", "0x65974452", 
			"0x7e8d424b", "0x3e59ec52", "0xab38aea6", "0x504d26ed", 
			"0x1e674b49", "0x254da584", "0x5449681c", "0xa19b108e",
			"0xada96c07"]

push_lines.set_unlooping_vars(pushes)

original_code = deepcopy(current_code)

# 	Google Function with write capabilities
# (written with the code generator module): 
# ---------------

dic = {}

for x in chain(range(ord('0'),ord('9')+1),range(ord('A'), ord('F')+1)):
	dic[chr(x)] = hex(x)[2:]
	
current_code += [code_template() for _ in range(2)]
print_function, compare_snippet = current_code[-2:]

print_function.include(compare_snippet,"compare")


print_function.body = \
"""_print_code:
pop eax
pop esi
push eax
mov eax, esi
ror eax, 24
mov esi, eax
and esi, 0x000000FF
push esi
ror eax, 24
mov esi, eax
and esi, 0x000000FF
push esi
ror eax, 24
mov esi, eax
and esi, 0x000000FF
push esi
ror eax, 24
mov esi, eax
and esi, 0x000000FF
push esi
xor esi, esi
call _start_comparing
call _start_comparing
call _start_comparing
call _start_comparing
ret  
_start_comparing:
pop eax
pop esi
push eax
{compare}
_finished_comparing:
mov [msg],ax
push edx
mov	edx, len
mov	ecx, msg
mov	ebx, 1	    
mov	eax, 4	    
int	0x80
pop edx        
ret

section	.data
;msg	db	'________',0xa
msg	db	'__'	
len	equ	$ - msg		
"""

compare_snippet.body = \
"""mov ax, {0}
cmp esi, {1}
je _finished_comparing
"""

ordered_ascii = []
for x in range(int("0xff",0) + 1):	
	n1, n2 = ("0" if x < 16 else "") + hex(x)[2:].upper()
	ordered_ascii.append(["0x" + dic[n2] + dic[n1],x])
compare_snippet.set_unlooping_vars(ordered_ascii)


back.change_line("{plines}jmp _post",7)
back.change_line("nop",8)
back.change_line("nop",9)
back.change_line("nop",10)

post.body = """_post:
call _print_code
dec edx
dec edx
dec edx
dec edx
cmp edx, 0
jne _post
mov eax, 0x1
int 0x80
{print_function}
"""

post.include(print_function, "print_function")

code_with_stack_printing = deepcopy(current_code)


# 	Print results 
# ---------------

del(current_code)

#print(original_code[0].resolve())
print(code_with_stack_printing[0].resolve())


