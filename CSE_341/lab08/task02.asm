.model
     
    factorial macro x 
        mov ah,9
        int 21h
        
        
        
        mov ah,1
        int 21h
        
        
        mov ah,00h
        
        
        sub ax,30h
        mov cx,ax
        dec cx
        mov bx,ax
        dec bx
        
        start:
        mul bx
        dec bx
        loop start
        
        ;printing the factorial value macro
        print ax
             
  
    endm
    
    print macro y
        
        
        mov bx,16
        xor cx,cx ;repetitions
        
        analyse:
        xor dx,dx ;Clear DX for division
        div bx
        push dx  ; push reminder in stack
        inc cx
        cmp y,0  ;break conditions
        jne analyse
        
        write:
        pop dx     ; pop out from stack the reminder
        add dl,"0"     
        cmp dl,"9"     ;is dl digit?
        jbe SHORT show
        add dl,7
        
        show:
        mov ah,2
        int 21h
        loop write
     
     endm
     
     ;linefeed macro
        ;mov ah,2
        ;mov dl,0Ah
        ;int 21h
        
        ;mov dl,0Ah
        ;int 21h
     
     ;endm   
        
        
        
        
        

.stack 100h
.data

a dw 'input the number: $'
b dw 'output : $'

.code

mov ax,@data
mov ds,ax
mov es,ax
 

factorial b

mov ax,4c00h
int 21h
