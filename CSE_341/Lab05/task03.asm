data segment
    ; add your data here!
    pkey db "press any key...$"
ends

stack segment
    dw   128  dup(0)
ends

code segment
start:
; set segment registers:
    mov ax, data
    mov ds, ax
    mov es, ax

     
    mov cx, 5

    begin: 
     mov ah, 1
     int 21h
    loop begin
    
    mov ah,2
    mov dl,0Dh ; cret
    int 21h
    
    mov cx,5
    display:   
     mov ah, 2
     mov dl, 058H
     int 21h
    loop display
    
    end:
    
ends

end start ; set entry point and stop the assembler.




