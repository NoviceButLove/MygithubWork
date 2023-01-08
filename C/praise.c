/*praise.c-- 使用不同类型的字符串*/
#include <stdio.h>
#define PRAISE "You are an extraordinary being"
#include <string.h>
int main(void)
{
    int letters;
    char name[40];
    printf("What's your name?\n");
    scanf("%s", name);  //interesting!#scanf only read the word before blank!
    letters = strlen(name);
    printf("Hello, %s.%s\n", name, PRAISE);
    printf("Your name has %d letters.", letters);
    
    //float.c--一些浮点型修饰符的组合
    const double RENT = -3852.99;
    printf("*%f*\n", RENT);
    printf("*%e*\n", RENT);
    printf("*%4.2f*\n", RENT);
    printf("*%3.1f*\n", RENT);
    printf("*%10.3f*\n", RENT);
    printf("*%10.3E*\n", RENT);
    printf("*%+4.2f*\n", RENT);
    printf("*%010.2f*\n", RENT);
    printf("----------------------\n");
    printf("**% d**% d**", 34, -34);
    return 0;
}
