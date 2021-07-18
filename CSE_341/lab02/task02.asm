data segment
    ;pkey db "press any key...$" 
    a db "Enter First Value:$"
    b db "Enter Second Value:$"
    c db "Summation:$"
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
    
    ; first number
    lea dx,a
    mov ah,9
    int 21h
    
    ; first number input taking
    mov ah,1
    int 21h
    mov bh,al
    
    mov dl,0AH
    mov ah,2 ; showing first input number
    int 21h
    mov dl,13
    int 21h
    
    ; second number 
    lea dx,b
    mov ah,9
    int 21h
    
    ; second number input taking
    mov ah,1
    int 21h
    mov bl,al
    
    sub bh,030h
    sub bl,030h
    
    add bh,bl
    add bh,030h
    
    mov dl,0AH
    mov ah,2
    int 21h
    mov dl,13
    int 21h
    
    ;summation
    
    lea dx,c
    mov ah,9
    int 21h
    
    mov dl,bh
    mov ah,2
    int 21h
    
    
    