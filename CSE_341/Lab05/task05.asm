data segment
    ; add your data here!
    pkey db "press any key...$"
ends

stack segment
    dw   128  dup(0)
ends

code segment
start:
; set segment registers:
    mov ax, data
    mov ds, ax
    mov es, ax
    
    mov bx, 80H
    mov cl, 0
    
    repeat:
    cmp cl, 10
    je newline
    inc cl
    
    mov ah, 2
    mov dx, bx
    int 21h
    
    inc bx
    
    cmp bx, 0FFH
    je exit
    
    jmp repeat
    
    newline:
    mov dl, 0AH ; newline
    mov ah, 2
    int 21h
    
    mov dl, 13 ; carriage return to rest position
    mov ah, 2
    int 21h
    
    mov cl, 0
    
    jmp repeat
    
    exit:

ends

end start ; set entry point and stop the assembler