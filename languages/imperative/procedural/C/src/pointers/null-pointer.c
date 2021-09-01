/*
    A pointer that does not point to any memory address/locations.
    Represents an invalid pointer.

    When the NULL value is assinged to a pointer, then the pointer is considered a 
    NULL pointer

    Use cases:
        1. Initialise a pointer when it's not yet assinged a valid memory address yet. 
            It's good paractice to do so.
        
        2. Handle error when using malloc
            malloc return NULL when momory not available

    Some Facts on NULL pointer
        1. The value of NULL is 0, but this 0 is written in the context of pointers. It is NOT equivalent to 
            integer 0
        2. Size of NULL depends on the platform

    
    BEST practices
        1. Initialise unassinged pointers to NULL
        2. Perform NULL check before deferencing any pointer(sound familiar to Java?)
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = NULL; //ptr is a NULL pointer
    printf("%d\n", ptr);

    //error handling
    void *address;

    address = malloc(sizeof(int)*2);
    if(address == NULL) 
        printf("Failed to allocate memory");
    else
        printf("Memory successfully memory");

    return 0;
}