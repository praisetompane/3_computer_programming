/*
   Pointer that points to some non-existing memory location 
   "non-existing"? => non existing in the program's memory allocation from the Operating System.
*/

#include <stdlib.h>
#include <stdio.h>

int main() {
    printf("Allocate memory for one integer to ptr");
    int *ptr = (int *)malloc(sizeof(int));
    *ptr = 5;
    printf("Number set to ptr's  memory address: %d\n", *ptr);
    printf("ptr's memory address: %p\n", ptr);
    printf("Free the memory assinged to ptr\n");
    free(ptr);
    printf("ptr is dangling from this stage, because it still holds the memory address it had.");
    printf("BUT it does nto belong to the program anymore\n");
    printf("ptr's memory address: %p\n", ptr);

    //Best practice and solution:
    ptr = NULL;

    return 0;
}