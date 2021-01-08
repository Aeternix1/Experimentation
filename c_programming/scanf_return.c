//Program used to experiment with scanf
#include <stdio.h>
#include <stdlib.h>

int main () { 
    
    //Testing the return values of scanf 
    /*char *name;*/
    int age; 
    /*float WAM; */
    int n;

    /*printf("Enter your name, age and WAM into stdin\n"); */
    /*n = scanf("%ms %d %f", &name, &age, &WAM);*/
    /*printf("%s, %d, %f\n", name, age, WAM);*/
    /*printf("The number of scanned values was: %d\n", n);*/

    n = scanf("Hello     %d\n", &age);
    printf("%d\n", age);
    printf("The number of scanned values was: %d\n", n) ;

    /*free(name);*/

}
