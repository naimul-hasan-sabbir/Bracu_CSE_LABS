data segment
    a db "ENTER THREE INITIALS : "
ends
stack segment
    dw   128  dup(0)
ends

code segment
start:
    mov ax, data
    mov ds, ax
    mov es, ax
    
    ;Printing Prompt
    lea dx, str
    mov ah, 9
    int 21h
    
    ;Taking Three Inputs
    mov ah,1 
    int 21h
    mov bh , al
    
    mov ah,1 
    int 21h
    mov bl , al
    
    mov ah,1 
    int 21h
    mov cl, al
    
    ;Printing
    mov dl, 0AH
    mov ah , 2
    int 21h
    mov dL,0DH 
    int 21h 
    mov dL,0AH 
    int 21h 
    
    mov dl,bh
    mov ah,2
    int 21h
    
    mov dl, 0AH
    mov ah , 2
    int 21h
    mov dL,0DH 
    int 21h 
    mov dL,0AH 
    int 21h 
    
    mov dl,bl
    mov ah,2
    int 21h 
    
    mov dl, 0AH
    mov ah , 2
    int 21h
    mov dL,0DH 
    int 21h 
    mov dL,0AH 
    int 21h 
    
    mov dl,cl
    mov ah,2
    int 21h
       
ends
    


