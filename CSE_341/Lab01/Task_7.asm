

X db 20
Y db 8
Z db 7
; number 1 problem 
mov al,X
mov bl,Y
Mul bl  ; multipilaction with x and y(x*y) 

; number 2 problem
MOV ax,20
MOV bl,y
DIV bl  ; division between 20 and y(20/8)

; number 3 problem
mov al,X
mov bl,Y
Mul bl
mov cl,z
div cl   ; x*y/z






