#include <stdio.h>

struct student {
    char name[50];
    int age;
    int roll_no;
    float marks;
};

void print_student(char name[], int age, int roll_no, float marks) {
    printf("%s %d %d %.2f \n", name, age, roll_no, marks);
}

int main() {
    struct student s1 = {"Nick", 16, 50, 72.5};
    print_student(s1.name, s1.age, s1.roll_no, s1.marks);
    return 0;
}