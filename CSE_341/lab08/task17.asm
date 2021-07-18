.model


.stack 100h

.data
num db 20
primes db 2,3,5,7,11,13,17,19 ; list of primes to be checked
array dw 20 dup(?)
.code
main proc
mov ax,@data
mov ds,ax
mov es,ax

mov ah,1
int 21h

mov bl,al
sub bl,30h
call checkPrime
call print

mov ax,4c00h
int 21h


ret
main endp

checkPrime proc
    
    check:        ; checking in loop
    mov bh,00h
    mov cx,bx  ; number of primes to check
    mov si,0
    xor ch,ch
    mov al,[num]
    div array[si]
    
    inc si
    
    cmp ah,0
    jne skip
    
    jmp check 
    
    ret
checkPrime endp

print proc      ;printing the primes
    
    
    ret
print endp