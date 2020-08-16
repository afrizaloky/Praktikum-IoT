
.data
	str:	.asciiz "hello world 1234567890"

.text
.globl main
main:
    la      $s1,str		    # s1 points to the string

    lw		$s2, 0($s1)		# 
    lw		$s3, 4($s1)		# 
    lw		$s4, 8($s1)		# 
    lw		$s5, 16($s1)		# 
    lw		$s6, 20($s1)		# 
    
    
    # lw		$s3, 8($s1)		# 
    
    
    

    # # la $s1,str		# s1 points to the string
    # lb $t0,($s1)

    # add $s1, $s1,1
    # lb $t1,($s1)
    
	# lw $t1,8($t0)
	# lw $t1,16($t0)
    # add		$t0, $t1, $t2		# $t0 = $t1 + $t2
