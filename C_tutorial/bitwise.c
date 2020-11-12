#include <stdio.h>
#include <stdlib.h>  
#include <stdint.h> 
#include <limits.h>

//In order to understand left and right shift operations
int main () { 
   
    printf("Understanding left shift operations\n");
    uint8_t a = 0x80;    
    a = a << 1;
    printf("The original value of a is: %#x\n", a);
    printf("The value of a after left shifting is %#x\n", a);  

    printf("Understanding right shift operations\n"); 
    int8_t b = 0x40; 
    printf("The original value of b is: %#x\n", b);
    b = b >> 1; 
    printf("The value after right shifting is %#x\n", b);


    

}
