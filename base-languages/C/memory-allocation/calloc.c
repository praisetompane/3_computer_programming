/*
    Assign n blocks of memory of size_t size
    Memory blocks are initialised to 0
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int numberOfNumbers, sum = 0;

    printf("Please enter number of numbers: ");
    scanf("%d", &numberOfNumbers);

    int *numbers = (int *)calloc(numberOfNumbers, sizeof(int));
    
    if(numbers == NULL) {
        printf("Memory allocation unsuccefull");
        exit(1);
    }

    for(int i = 0; i < numberOfNumbers; i++) {
        printf("Please provide a number: ");
        scanf("%d", numbers + i);
    }

    for(int i = 0; i < numberOfNumbers; i++) {
        sum += *(numbers + i);
    }
    
    printf("Total sum of the numbers is: %d\n", sum);
    return 0;
}