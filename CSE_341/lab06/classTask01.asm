data segment
    ; add your data here!
    a db ?
    x db a dup<?>
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
	
	
    ;input length
    
    mov ah, 1
    int 21h  
    mov a, al
         
             
    mov ah, 1
    mov si, 0
    mov bl,30h
    
    
    
    begin:
    cmp a, bl
    je begin2
    int 21h         ; input name
    mov x[si], al
    inc si
    inc bl
    jmp begin
    
    
    begin2:
    ;printing newLine
    mov dl, 0AH
    mov ah, 2
    int 21h
    
    ;printing creg return
    mov dl, 13
    mov ah, 2
    int 21h
    
    mov ah, 2
    mov si, 0
    mov bl,30h
    jmp begin3
    
    begin3:
    cmp a, bl
    je exit
    mov dl, x[si]   ;display the name
    int 21h
    inc si
    inc bl
    jmp begin3        
              
    exit:
                
    ; exit to operating system.
ends

end start ; set entry point and stop the assembler.