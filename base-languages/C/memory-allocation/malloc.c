#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = (int *)malloc(sizeof(int) * 1);
    
    if(ptr == NULL) {
        printf("Memory allocation unsuccefull");
        exit(1);
    }

    *ptr = 5;

    printf("Number stored: %d\n", *ptr);
    return 0;
}