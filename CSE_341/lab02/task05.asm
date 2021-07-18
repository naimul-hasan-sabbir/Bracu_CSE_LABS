data segment 
    a db "The sum of $ "
    b db " and $ "
    c db " is $"
ends

stack segment
    dw 128 dup(0)
ends

code segment
    start:
    
    mov ax,data
    mov ds,ax
    mov es,ax
    
    ; (a) number problem
    mov dl,03FH ;the ascii value of "?"  
    mov ah,2
    int 21h
    
    ;(b) number problem
    ;mov dl,0AH
    ;mov ah,2
    ;int 21h
    
    mov ah,1
    int 21h
    mov bh,al
    mov cl,bh
    
    mov ah,1
    int 21h
    mov bl,al
    
    mov dl,bh
    add bh,bl
    sub bh,030H
    
    mov dl, 0AH
    mov ah , 2
    int 21h
    
    mov dl,0DH
    int 21h
    mov dl,0AH
    int 21h
    
    lea dx,a
    mov ah,9
    int 21h
    
    mov dl,cl
    mov ah,2
    int 21h
    
    lea dx,b
    mov ah,9
    int 21h
    
    mov dl,bl
    mov ah,2
    int 21h
    
    lea dx,c
    mov ah,9
    int 21h
    
    mov dl,bh
    mov ah,2
    int 21h
 ends
     
    
