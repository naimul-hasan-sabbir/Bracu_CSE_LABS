.model

reverse macro
    mov cl,00
    mov ah,1
    mov bx,'#'
    
    push bx
    
    read:
    int 21h
    
    cmp al,13
    je display
    mov bl,al
    push bx
    jmp read
    
    display:
    pop bx
    cmp bl,'#'
    je exit
    mov ah,2
    jmp continue
    
    continue:
    mov dl,bl
    int 21h
    jmp display
    
    exit:
    mov ah,04ch
    int 21h
    
    
    
     
         endm

.stack 100h
.data

;a dw "abc$" 

.code

mov ax,@data
mov dx,ax
mov es,ax


reverse



mov ax,4c00h
int 21h

