#include <stdio.h>

/*
    We should large structs by reference to converse memory.
*/
struct point {
    int x;
    int y;
    int z;
};

void print(struct point *point) {
    printf("x: %d y: %d z: %d\n", point->x, point->y, point->z);
}

int main() {
    struct point sun_position = {1000000, 1000, 50000000};
    struct point earth_position = {90000, 1323, 9999};

    print(&sun_position);
    print(&earth_position);
    return 0;
}
