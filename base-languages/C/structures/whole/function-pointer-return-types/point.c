#include <stdio.h>
#include <stdlib.h>

struct point {
    int x;
    int y;
    int z;
};

struct point * create_point(int x, int y, int z) {
    struct point *ptr = (struct point *)malloc(sizeof(struct point));
    ptr->x = x;
    ptr->y = y;
    ptr->z = z;

    return ptr;
}
void print(struct point *point) {
    printf("x: %d y: %d z: %d\n", point->x, point->y, point->z);
}

void scale(int scalar, struct point *value) {
    value->x *= scalar;
    value->y *= scalar;
    value->z *= scalar;
}

int main() {
    struct point *some_point = create_point(123, 456, 789);
    printf("Initial state\n");
    print(some_point);
    scale(2, some_point);
    printf("New state\n");
    print(some_point);
    return 0;
}