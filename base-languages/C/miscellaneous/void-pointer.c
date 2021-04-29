#include <stdio.h>

int main() {
    int n = 1;
    void *ptr;
    ptr = &n;
    printf("%d\n", *(int *)ptr); //need to cast a void pointer to pointer of the type you set it to point to.
    return 0;
}