/*
    change size of memory block without losing data
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
 int numberOfNumbers, sum = 0;

    printf("Please enter number of numbers: ");
    scanf("%d", &numberOfNumbers);

    int *numbers = (int *)malloc(sizeof(int) * numberOfNumbers);
    
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
    
    printf("Current sum of the numbers is: %d\n", sum);
    printf("I have apetite for more summing :)\n");
    printf("Please provide another %d numbers\n", numberOfNumbers);

    numbers = realloc(numbers, sizeof(int) * (numberOfNumbers + numberOfNumbers));
    if(numbers == NULL) {
        printf("Failed to allocate additional memory, sorry :(\n");
        exit(1);
    }
    for(int i = 0; i < numberOfNumbers; i++) {
        printf("Please provide a number: ");
        scanf("%d", numbers + i);
    }

    for(int i = 0; i < numberOfNumbers; i++) {
        sum += *(numbers + i);
    }

    printf("Current sum of the numbers is: %d\n", sum);
    return 0;
}