#include <stdio.h>
#include <stdlib.h>  
#include <stdint.h>

//Program takes in a value from stdin and multiplies it by 2048
//It does this using bit operations alone 
//By adding 11 (using bit operations) to the bit string

int main (int argc, char **argv) {  
    uint8_t n = atoi(argv[1]);  
    
    uint16_t eleven = 0x000B; 
    uint16_t sum = 0x0000; 
    
    //Run XOR
    sum = eleven ^ n;
    printf("%d\n", sum); 
    
    //Find indexes where carries occur
    //Store in variable 
    


}

