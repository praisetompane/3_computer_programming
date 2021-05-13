/*
    Change size of memory block without losing data
    Need to account for current block size in new size parameter
    Copies content of old block
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
 int numberOfNumbers, sum = 0;

    printf("Please enter number of numbers: ");
    scanf("%d", &numberOfNumbers);

    int *numbers = (int *)malloc(sizeof(int) * numberOfNumbers);
    
    printf("Address stored in *numbers: %p\n", numbers);

    if(numbers == NULL) {
        printf("Memory allocation unsuccefull");
        exit(1);
    }

    for(int i = 0; i < numberOfNumbers; i++) {
        printf("Please provide a number: ");
        scanf("%d", numbers + i);
    }
    printf("Summing the numbers...\n");
    for(int i = 0; i < numberOfNumbers; i++) {
        printf("Adding: %d\n", *(numbers + i));
        sum += *(numbers + i);
    }
    
    printf("Current sum of the numbers is: %d\n", sum);
    printf("I have apetite for more summing :)\n");
    printf("Please provide another %d numbers\n", numberOfNumbers);
    
    int totalNumbers = numberOfNumbers + numberOfNumbers;
    numbers = realloc(numbers, sizeof(int) * (totalNumbers));

    printf("Address stored in *numbers: %p\n", numbers);
    if(numbers == NULL) {
        printf("Failed to allocate additional memory, sorry :(\n");
        exit(1);
    }
    for(int i = 0; i < numberOfNumbers; i++) {
        printf("Please provide a number: ");
        scanf("%d", numbers + i);
    }
    printf("Summing again, yummy \n");
    for(int i = 0; i < numberOfNumbers; i++) {
        printf("Adding: %d\n", *(numbers + i));
        sum += *(numbers + i);
    }
    printf("Here is the list of all the numbers \n");
    for(int i = 0; i < totalNumbers; i++) {
        printf("%d", *(numbers + i));
    }
    printf("\n");    
    printf("Current sum of the numbers is: %d\n", sum);
    return 0;
}