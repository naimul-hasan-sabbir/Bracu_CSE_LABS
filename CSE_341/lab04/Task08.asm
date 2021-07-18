.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
a db "Vowel$"
b db "Consonant$"

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

    mov ah, 1
    int 21h
    mov bl, al
    ;For A
    cmp bl, 'A'
    je VOWEL
    cmp bl, 'a'
    je VOWEL
    
    ;For E
    cmp bl, 'E'
    je VOWEL
    cmp bl, 'e'
    je VOWEL
    
    ;For I
    cmp bl, 'I'
    je VOWEL
    cmp bl, 'i'
    je VOWEL
    
    
    ;For 0 
    cmp bl, 'O'
    je VOWEL
    cmp bl, 'o'
    je VOWEL
    
    
    ;For U
    cmp bl, 'U'
    je VOWEL
    cmp bl, 'u'
    je VOWEL
    
    ;CONSONANT
    ;new line & cret
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
    
    VOWEL:
    ;new line & cret
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
  

