; MOV examples

;general register & genral register
MOV al,ah
MOV ax,bx

; general register & segment register
MOV DS,al
MOV ds,bl

; general register & memeory location
x db 7
MOV x,bl

; memory location & genral register
MOV ax,8921
MOV ch,3

mov al,3
mov ch,4

; memory location & segment register
A db 3
mov cs,A
mov ds,A

B dw 18
mov cs,B
mov ss,B

; segment register as source
mov al,cs
mov bh.ds

x db 2
mov x,cs
mov x,ds
 





