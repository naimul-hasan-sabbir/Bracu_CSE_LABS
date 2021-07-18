; general register(source) & general register(destination)
add al,ah
add bx,cx

sub al,ah
sub bx,cx

; general register(source) & general register(destination)
x db 2
add x,al
add x,bh

sub x,al
sub x,bh

; memory location(source) & general register(destination)
y db 6
add al,y
add cl,y

sub al,y
sub cl,y 


