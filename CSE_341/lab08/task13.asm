.model

.stack 100h

.data

a dw '(4+(5*8))$'

.code

main proc
    mov ax,@data
    mov ds,ax
    mov es,ax
    
    
    lea bx,a
    call traversePush
    call checkBalance
    
    
    mov ax,4c00h
    int 21h

main endp

traversePush proc
    
    push bx  ; pushing into stack
    
    ret
traversePush endp

checkBalance proc
    pop bx
    check:
    cmp bx,040h  ; comparing "(" & ")" 
    je print
    
    xor bx,bx
    jmp check
    
    
    print:
    mov dl,007h  ; for beep
    mov ah,2
    int 21h
    
    ret
    
checkBalance endp