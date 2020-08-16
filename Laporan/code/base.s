
.data
	str:	.asciiz "hello world 1234567890"

.text
.globl main
main:
    la      $s1,str     # s1 points to the string

    lw		$s2, 0($s1)	
    lw		$s3, 4($s1)	
    lw		$s4, 8($s1)	
    lw		$s5, 16($s1)
    lw		$s6, 20($s1)
    
    
    