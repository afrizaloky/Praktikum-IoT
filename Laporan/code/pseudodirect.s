
.text
.globl main
main:

    li $t0, 3
    li $t1,5
    li $t2, 0 #counter   
    li $t3, 2
    

loop:beq $t2,10,End # Looping 10x
	add $t1, $t1,$t0		
    addi $t3, $t3, -1

	addi $t2,$t2,1	#increnment
	j loop
End: 
	li $v0,10
	syscall	# Bye!