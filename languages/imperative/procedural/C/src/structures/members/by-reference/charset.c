#include <stdio.h>
#include <stdlib.h>

struct charset {
    int code;
    char character;
};


void keyValue(char *character, int *code) {
    scanf("%c %d", character, code);
}

int main() {
    struct charset charsetvalue;
    printf("Please provide me a character and it's code: ");
    keyValue(&charsetvalue.character, &charsetvalue.code);

    printf("Character: %c Code: %d\n", charsetvalue.character, charsetvalue.code);

    return 0;
}