.MODEL SMALL
 
.STACK 100H

.DATA 

;variables 
a db "DIVISIBLE BY BOTH 5 & 11$"
b db "NOT DIVISIBLE BY BOTH 5 & 11$"

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here
    mov ax, 55
    mov bx, ax
    mov ch, 05h
    mov cl, 0Bh
    
    ;dividing by 5
    div ch
    cmp ah, 0
    jne NOTDIVISIBLE

    BYELEVEN:
    mov ax, bx
    div cl
    cmp ah, 0
    jne NOTDIVISIBLE

    ;DIVISIBLE:
    lea dx, a
    mov ah, 9
    int 21h
    jmp EXIT
    
    NOTDIVISIBLE:
    lea dx, b
    mov ah, 9
    int 21h
    jmp EXIT
    
    EXIT:
    

 

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  

