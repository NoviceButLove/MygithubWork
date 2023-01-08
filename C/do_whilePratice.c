#include <stdio.h>
int main(void)
{
    const int secret_code = 13;  //声明不可变 的变量
    int code_entered;
    do
    {
        printf("To enter the ");
        scanf("%d", &code_entered);
    } while (code_entered != secret_code);
    printf("Congratulations!");
    return 0;
    
}