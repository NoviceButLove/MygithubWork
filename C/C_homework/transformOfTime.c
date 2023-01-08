#include <stdio.h>
#include <string.h>

int main(void)
{
    //使用string.h库调用strlen()
    printf("Please enter your local time:\n");
    /*time 实现存储输入 length 实现判断格式 plus  实现计算  
    first、second…… 等实现存储数字用于输出*/
    char time[5]; // 定义字符数组, 目标是前4个，长度5用于存储‘\n’
    int length, first, second, third, forth, plus;  // 定义整型变量
    scanf("%4s", time); 
    length = strlen(time);  // 识别总共输入多少字符
    if (length>5)
    {  // 如果超过5个，则不符合格式
        printf("Wrong formulation of number!");
    }
    else 
    {  // 用变量存储每一个字符值
        first = (int)time[0] -48; //ASCLL码转换
        if (length == 1)
        {  // 只输入一个，即表示分
            printf("Now UTC is  **00:0%d**\n", first);
            printf("Then UTC is **16:0%d**", first);
        }
        else if ((length == 2)&&(first != 0))
        { // 输入两个，表示分
            second = (int)time[1] - 48;
            if ((first>=0)&&(first <6))
            {  //确保格式正确
                printf("Now BJT is  **00:%d%d**\n", first, second);
                printf("Then UTC is **16:%d%d**", first, second);
            }
            else
            {
                printf("Wrong number");
            }
        }
        else if ((length == 3)&&(first != 0))
        { // 输入三个，表示几时几分
            second = (int)time[1]-48;
            third = (int)time[2]-48;
            if ((second >= 0)&&(second < 6))
            { // 确保格式
                if (first < 9)
                {
                    printf("Now BJT is  **%d:%d%d**\n", first, second, third);
                    printf("Then UTC is **%d:%d%d**",\
                    first -  8 + 24, second, third);
                }
                else 
                {
                    printf("Now BJT is  **0%d:%d%d**\n", first, second, third);
                    printf("Then UTC is **0%d:%d%d**", first - 8, second, third);
                }
            }
            else
            {
                printf("Wrong number");
            }
        }
           
        else if ((length == 4)&&(first != 0))
        {
            second = (int)time[1] - 48;
            third = (int)time[2] - 48;
            forth = (int)time[3] - 48;
            if ((((first > 0)&&(first < 3))&&((second >= 0)\
            &&(second < 4)))&&((third >= 0)&&(third < 6)))  // 使符合23:59的限制
            {
                plus = 10*first + second;  
                printf("Now BJT is  **%d:%d%d**\n", plus, third, forth);
                printf("Then UTC is **%d:%d%d**", plus - 8, third, forth);
            }
            else
            {
                printf("Wrong number");
            }
        }
    }   
         return 0;
} 

    