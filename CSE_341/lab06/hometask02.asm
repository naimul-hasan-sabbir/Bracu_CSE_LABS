data segment
    ;array size 5
    x db 5 dup<?>
    
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
    
    mov ah,1
    mov cx,5
    mov si,0
    
    input:
    int 21h
    mov x[si],al
    inc si
    loop input
    
    
    mov cl,x
    sub cl,30h
    dec cl
    
    loop3:
    mov ch,x
    sub ch,30h
    dec ch
    
    mov si,0
    
    loop2:
    mov al,x[si]
    ;sub al,30h
    inc si
    cmp al,x[si]
    jc loop1
    XCHG al,x[si]
    XCHG x[si-1],al
    
    loop1:
    dec ch
    jnz loop2
    dec cl
    jnz loop3
    
    ;printing new line
    mov dl,0Ah
    mov ah,2
    int 21h
    
    ;creg return
    mov dl,13
    mov ah,2
    int 21h
    
    
    mov ah,2
    mov si,0
    mov cx,5
    
    display:
    mov dl,x[si]
    int 21h
    inc si
    loop display
    
    ; sir please first input 5,4,3,2,1 as 5 numbers 
    
ends

end start ; set entry point and stop the assembler.

