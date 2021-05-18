#include <stdio.h>

struct point {
    int x;
    int y;
};

void print(struct point point) {
    printf("x: %d y: %d \n", point.x, point.y);
}

int main() {
    struct point sun_position = {1000000, 1000};
    struct point earth_position = {90000, 1323};

    print(sun_position);
    print(earth_position);
    return 0;
}
