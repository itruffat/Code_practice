# Google Security Challenge

I don't have a lot of information on how or where this challenge took place, all I was given was a picture of some x8086 code, and told I needed to find an answer. Just in case you are wonder, my guess is that the challenge is long over since no one (I know) who submitted an answer received a reply. 

## Challenge Code

Anyways, the code was the following:

```
section .text
    global _start
_start:
    jmp _forward
_back:
	pop edi
    push byte 4
    pop eax
    cdq
    mov ebx, edx
    inc ebx
    mov ebp, 0x474f4f47
    push 0xe06cafbd
    call edi
    push 0xde8d7d56
    call edi
    push 0x47874e62
    call edi
    push 0x65974452
    call edi
    push 0x7e8d424b
    call edi
    push 0x3e59ec52
    call edi
    push 0xab38aea6
    call edi
    push 0x504d26ed
    call edi
    push 0x1e674b49
    call edi
    push 0x254da584
    call edi
    push 0x5449681c
    call edi
    push 0xa19b108e
    call edi
    push 0xada96c07
    call edi
    mov ecx, esp
    int 0x80
    mov eax, ebx
    int 0x80
_forward: call _back
    xor [esp+4],esi
    add edx, 4
    xor ebp, esi
    ror ebp, 3
    sub ebp, edx
    xor esi, ebp
    ret
```

## Solution

* Step 1:

To solve this problem, the first part was to find "the puzzle", since I didn't know what had to be answered. At first glance the code looks like a shellcode injection. After all, it uses a lot of tricks common in shellcodes, like avoiding nulls by pushing values into the stack (_"push byte 4" + "pop eax"_ instead of _"mov eax 4"_) or calling the _"cdq"_ instruction (instead of _"mov edx 0"_).

However, upon further inspection it can be seen that after the algorithm is over, the main sycall being called is 0x4 ("write"), which is not the usually victim of shellcode attacks. While there are cases in which writting an string can lead to an attack ([Format String Attacks](https://www.owasp.org/index.php/Format_string_attack) comes to mind), I couldn't think of any exploit consisting of writting such short String in the "standard output". What's more, the output looked like absolute Giberish. (It was not ASCII, not x08086 code or anything else)

Everything seemed to point in the direction of a message that needed some "decryption". And since the variable ESI was never defined (but took place in the decryption of the hardcoded values), it was the most likely candidate to be the key.

* Step 2:

To have better understanding of how the pile evolved with different ESI values, I made two short Python programs: "Assembly code generator" and "QnD Intel8086". Feel free to look at their code and see what their do, but the TL;DR is that they both print the queue, one creates a program that does it natively in Assembly, the other one in Python3.

** Assembly code generator: it actually goes deeper than this challenge, and allows us to quickly create and modify x86 Assembly code in code. The main goal of this program is to easily concatenate different parts of code, and to allow the user to repeat lines with slight modifications. As such, creating programs with unrooled loops becomes pretty trivial. Which is what I wanted to do to create the stack printer, since there is little space for errors by hardcoding every possible print output.

** QnD Intel8086: emulates the required instructions in Python, while trying to modularize everything. It's incredibly straightforward, but it will be incredibly useful in the next section, since it allows us to painlessly test multiple values of ESI. 

* Step 3:

The last step was to design an ESI guesser. I asummed (correctly) that the answer was a message written in readable ASCII characters. Had that not been the case, I could have recycled this technic with a different definition of what a "legal output" meant. (for example, if the message had been more x86 instructions, "legal" would have meant numbers that could be decompilled into x86 instructions)

So, I took advantage of the fact that the output must be "legal" in every step. In this case, that meant the value of each byte should be somewhere between 0x20 and 0x7F. Looking at the first step, I statically checked which input created a valid output for that first step. This greatly reduced the input space (from 4 trillions to 81 billions), meaning I could look at each case. To speed up the process, I deceded to kill each case the step it generated an invalid output. This had a total run time of about 50 minutes in my computer.

To further improve this code, I decided to reduce the search space even further. While the whole spectrum of "legal" options would have given me a valid answer, more than half of the characters were unlikely to appear in the first step. So I reduced the space to only those characters that were likely to appear. I still got the answer, but this try took me less than 2 minutes.