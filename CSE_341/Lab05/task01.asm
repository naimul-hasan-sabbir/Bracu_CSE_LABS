; multi-segment executable file template.

data segment
    ; add your data here!
    
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

    ; add your code here
    mov cx , 80   
    mov ah , 2
    mov dl , '*'
    
    shuru:
        int 21h
        
    loop shuru      
        
ends

end start ; set entry point and stop the assembler.
© 2021 GitHub, Inc.