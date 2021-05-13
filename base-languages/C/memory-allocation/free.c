/*
    release memory allocated in heap
*/

#include <stdlib.h>
#include <stdio.h>

int *getinput(int size) {
    int *ptr = (int *)malloc(sizeof(int) * size); //Interesting => This memory will stay allocated
    printf("Enter %d numbers: ", size);

    for (int i = 0; i < size; i++) {
        scanf("%d", ptr + i);
    }

    return ptr;
}

int main() {
    int sum = 0;
    int size = 5;
    int *ptr = getinput(size);
    
    for(int i = 0; i < size; i++) {
        sum += *(ptr + i);
    }
    
    printf("Sum is: %d", sum);
    free(ptr);
    ptr = NULL;
    
    return 0;
}