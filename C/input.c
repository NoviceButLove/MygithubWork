#include <stdio.h>
int main(void)
{
    int age;
    float assets;
    char pet[30];
    printf("Enter your age, assets, and favourite pet:\n");
    scanf("%d %f", &age, &assets);  // 这里要使用&
    scanf("%s", pet);  //这里不用，pet是字符串
    printf("%d $%.2f %s\n", age, assets, pet);
    return 0;
}