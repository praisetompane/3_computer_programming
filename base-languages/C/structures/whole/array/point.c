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

void scale(int universe, int scalar, struct point * values[] ) {
    for(int i = 0; i < universe; i++) {
        values[i]->x *= scalar;
        values[i]->y *= scalar;
        values[i]->z *= scalar;
    }
}

void clean_up(struct point * ptr) {
    free(ptr);
    ptr = NULL;
}

int main() {
    int universe = 2;
    struct point * some_point_1 = create_point(1, 2, 3);
    struct point * some_point_2 = create_point(4, 5, 6);
    struct point * points [] = {some_point_1, some_point_2};

    printf("Initial states\n");
    for(int i = 0; i < universe; i++) {
        print(points[i]);
    }
    
    scale(universe, 3, points);

    printf("New state\n");
    for(int i = 0; i < universe; i++) {
        print(points[i]);
    }

    clean_up(some_point_1);
    clean_up(some_point_2);
    return 0;
}