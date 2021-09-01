#include <stdio.h>

/*
    Use cases:
        1. Allocate memory for any data type without knowing type(e.g. malloc or calloc)
*/
int main() {
    int n = 1;
    void *ptr;
    ptr = &n;
    printf("%d\n", *(int *)ptr); //need to cast a void pointer to pointer of the type you set it to point to.
    return 0;
}