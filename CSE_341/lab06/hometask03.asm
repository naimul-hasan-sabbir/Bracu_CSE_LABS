data segment
    x db 3 dup<?>
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
    mov cx,3
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
    
    
    mov ah,2
    mov si,0
    mov cx,2
    output:
    inc si
    loop output
    mov dl,x[si]
    int 21h
    
    
    
    

ends

end start

