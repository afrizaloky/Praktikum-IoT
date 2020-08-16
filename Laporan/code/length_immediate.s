.data
	str:	.asciiz "hello world"
	ans:	.asciiz "Length is "
	endl:	.asciiz "\n"	   

        .text
        .globl main
main:                	# execution starts here

        la $t2,str		# t2 points to the string
        li $t1,0        	# t1 holds the count
		
nextCh: lb $t0,($t2)		# get a byte from the string
	beqz $t0,strEnd 	# zero means end of string
	add $t1, $t1,1		# increment count
	add $t2, 1		# move pointer one character
	j nextCh		# go round the loop again

strEnd: 
	la $a0,ans		# System call 
	li $v0,4		# to print out
        syscall         	# the string message

	move $a0,$t1		# copy the count to a0
	li $v0,1		# System call 1 
	syscall			# to print the length worked out

	la $a0,endl		# syscall to print out
	li $v0,4		# a newline
	syscall

	
	li $v0,10
	syscall			# Bye!

