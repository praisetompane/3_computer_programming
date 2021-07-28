#include <stdio.h>
#include <stdlib.h>

struct point {
    int x;
    int y;
    int z;
    struct point * next;
};

struct point * create_point(int x, int y, int z) {
    struct point *ptr = (struct point *)malloc(sizeof(struct point));
    ptr->x = x;
    ptr->y = y;
    ptr->z = z;

    return ptr;
}

void clean_up(struct point * ptr) {
    free(ptr);
    ptr = NULL;
}
void print(struct point *point) {
    printf("x: %d y: %d z: %d\n", point->x, point->y, point->z);
}

struct point scale(int scalar, struct point value) {
    value.x += scalar;
    value.y += scalar;
    value.z += scalar;
    return value; // Where is this point variable living? Heap or Stack?
}

int main() {
    struct point *origin = create_point(0, 0, 0);
    struct point next_point = scale(1, *origin);
    origin->next = &next_point;

    printf("Printing from origin");
    print(origin);
    print(origin->next);

    clean_up(origin);
    return 0;
}