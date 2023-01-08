#include <stdio.h>
int main(void)
{
    int integer, g, s, b;
    printf("enter a integer range from 100 to 999:\n");
    scanf("%d", &integer);
    g = integer/ 100;
    s = (integer - 100*g)/ 10;
    b = integer - 100* g - 10* s;
    printf("reverse number is:%d%d%d", b, s, g);
}