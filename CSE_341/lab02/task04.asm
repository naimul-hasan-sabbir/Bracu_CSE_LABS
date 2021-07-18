data segment
    a db "Enter an uppercase letter : "
ends

stack segment
    dw   128  dup(0)
ends

code segment
    start:
    ; set segment registers 
    mov ax,data
    mov ds,ax
    mov es,ax
    
    lea dx,a
    mov ah,9
    int 21h
    
    mov ah,1
    int 21h
    
    mov dl,0AH
    mov ah,2
    int 21h
    
    add al,32
    
    mov dl,al
    mov ah,2
    int 21h
ends



