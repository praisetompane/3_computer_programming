#include <stdlib.h>

int main() {
    int var;
    int *ptr = NULL; //Initialise it to a NULL pointer
    int *ptr2 = (int *)malloc(sizeof(int)); //Explicitly allocate memory to it
    int *ptr3 = &var; //Allocate it an existing variables memory address(Becareful with this one)

    return 0;
}