#include <stdio.h>
#include <stdlib.h>  
#include <string.h>

#define TRUE 1
#define FALSE !(TRUE)

//Understanding dynamic memory allocation
int main () { 

    //Create an array of user specified size 
    int size, count;
    //This pointer points to the start of the block of memory allocated
    int *array;
    
    printf("How many values do you want to hold? ");
    scanf("%d", &size); 
    array = malloc(size * sizeof(int)); 


    //Store input into the array 
    printf("Insert values to be stored\n"); 
    int i = 0;
    while (i < size) { 
        scanf("%d", &array[i]);
        i++;
    } 


    //Print out the array
    count = 0;
    while (count < size) { 
        printf("value[%d] = %d\n ", count, array[count]);
        count++;
    } 

    //Adding more values   
    char prompt;
    printf("Do you need to add more values?\nEnter Y or N:\n");  
    scanf("\n%c", &prompt); 
    
    int addSize;
    if (prompt == 'Y') { 

        printf("How many new values do you want to add?\n"); 
        scanf("%d", &addSize);  //I don't want to lose data
        int size = size + addSize;
        array = realloc(array, size * sizeof(int)); //Increase the size
        
        printf("Insert values to be stored\n"); 
        i = size - addSize; 
        while (i < size) { 
            scanf("%d", array[i]); 
            i++;
        }

        //Print out the array
        count = 0;
        while (count < size) { 
            printf("value[%d] = %d\n ", count, array[count]);
            count++;
        }
        
    } else if (prompt == 'N') { 
        "Thank you!";
    }

    free(array); 
}
