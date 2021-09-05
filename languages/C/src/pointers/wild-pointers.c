/*
    Pointers that are uninitiliased, thus points to memory the prgram does not own.
    Using it before allocating it can can unexpected behaviour.
*/

#include <stdio.h>

int main() {
    int *ptr;
    *ptr = 9; //This could fail as ptr is a wild pointer
    printf("ptr's value: %d\n", *ptr);
    return 0;
}

