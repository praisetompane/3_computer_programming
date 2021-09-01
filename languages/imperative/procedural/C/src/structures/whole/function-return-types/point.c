#include <stdio.h>

struct point {
    int x;
    int y;
    int z;
};

void print(struct point point) {
    printf("x: %d y: %d \n", point.x, point.y);
}

struct point scale(int scalar, struct point value) {
    value.x *= scalar;
    value.y *= scalar;
    value.z *= scalar;
    return value;
}

int main() {
    struct point some_point = {123, 456, 789};
    printf("Initial state\n");
    print(some_point);
    struct point scaled = scale(2, some_point);
    printf("New state\n");
    print(scaled);
    return 0;
}