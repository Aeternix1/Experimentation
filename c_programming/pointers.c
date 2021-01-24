#include <stdio.h>
#include <stdlib.h>

int sum_array (int *array, int size);

int main (int argc, char *argv[]) 
{
    int a[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; 
    printf("%d\n", sum_array(a,10));
    return 0;
} 

int sum_array (int *array, int size) 
{
    int sum = 0;
    for (int i = 0; i < size; i++) { 
        sum = sum + array[i];
    }
    return sum;
}
