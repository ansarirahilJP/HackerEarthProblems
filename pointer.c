#include <stdio.h>
int main()
{
    // printf() displays the string inside quotation
    // printf("Hello, World!\n");
    int a;
    a = 5;
    int *p;
    p = &a;
    printf("%p\n", p);
    return 0;
}