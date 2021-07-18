;declaring variables 

A db 30
B db 20
C db 10

mov al,A  ;set value of A to al
mov bl,B  ;set value of B to bl
mov cl,C

sub bl,al ;subtracting A from B(B-A)
mov al,bl

mov al,A
add al,1

NEG al

mov al,A
mov bl,B
inc bl    ;inreasing value of B by 1
add al,bl
mov cl,al

mov al,A
dec al    ; decreasing the value of A by 1
mov bl,B
sub bl,al
mov al,bl




