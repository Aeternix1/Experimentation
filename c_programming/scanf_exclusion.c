#include <stdio.h>
#include <errno.h>
#include <stdlib.h> 


int main () { 
    
    //The following code is useful if you want to scan
    //Everything until the formatting breaks
    /*char *p;*/
    /*int n; */

    /*errno = 0; */
    /*printf("Please enter your name: ");*/
    /*n = scanf("%m[^]aeiouAEIOU]", &p); */
    /*if (n == 1) { */
        /*printf("%s\n", p);*/
        /*free(p);*/
    /*} else if (errno != 0) {*/
        /*perror("scanf");*/
    /*} else { */
        /*fprintf(stderr, "No matching characters\n");*/
    /*}*/

    char c; 
    scanf("%[a-z]", &c);
    printf("%c", c);

}
