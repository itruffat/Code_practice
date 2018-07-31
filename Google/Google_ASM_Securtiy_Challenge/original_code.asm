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
