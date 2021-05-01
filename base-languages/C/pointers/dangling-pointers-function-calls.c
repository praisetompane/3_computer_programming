#include <stdio.h>

int * func(){
    int n = 5;
    /*
        Function is popped from program's stack and all its local memory deallocated
        from the program after the return statement.
    */
    return &n;
}

int main() {
    int *ptr = NULL;
    /*
        This makes ptr dangling, because the memory address returned
        by fnc does not belong to the program anymore.
    */
    ptr = func(); 
    //Only coincidentally works as OS has not reassinged it to another program
    printf("Value in ptr's memory:%d\n", *ptr); 
    return 0;
}