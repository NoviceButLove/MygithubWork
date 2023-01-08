/* 打印我的年龄，转换为天数 */
#include <stdio.h>

void days_age(void);
int main(void)
{
    days_age();
    return 0;
}
void days_age(void)
{
    int day , age;
    printf("Please enter your age:\n");
    scanf("%d", &age);
    day = age*365;
    printf("%d", day);
    printf("The day of your age is %d", day);
    return;
}
