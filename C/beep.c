/*2023 Jan 1st 测试*/
#include <stdio.h>
#define MSCDS 1000
int main(void)
{
    // 我想来声beep
    char beep = '\007';
    printf("%c", beep);
    //下面是类型演示
    // //“”表示字符串，‘’表示字符常量
    // float aboat = 32000.0;
    // double abet = 2.14e9;
    // long double dip = 5.32e-5;
    // printf("%f can be written %e\n", aboat, aboat);
    // printf("And it's %h in hexadecimal, powers of 2 notation\n",
    //         aboat);
    // printf("%f can be written %e\n", abet, abet);
    // // printf("%lf can be written %Le\n", dip, dip);  //这行输出有问题
    printf("%d", MSCDS);
    return 0;
}
