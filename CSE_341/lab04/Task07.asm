.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
a db "ODD$"
b db "EVEN$"

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

    mov ah, 1
    int 21h
    sub al, 30h
    mov ah, 0
    mov bl, 2
    div bl
    
   
    cmp ah, 1
    je ODD
    
    
    ;EVEN
    ;new line
    ; even func
    mov dx, 10
    mov ah, 2
    int 21h
    mov dx, 13
    mov ah, 2
    int 21h
    
    lea dx, b
    mov ah, 9
    int 21h
    jmp EXIT
    
    
    
    ODD:
    ;new line
    ; odd func
    mov dx, 10
    mov ah, 2
    int 21h
    mov dx, 13
    mov ah, 2
    int 21h
    
    lea dx, a
    mov ah, 9
    int 21h
    jmp EXIT
    
    
    EXIT:

    
    
    
    



 

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  

