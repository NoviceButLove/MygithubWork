#include <stdio.h>
#include <string.h>

int main(void)
{
    //ʹ��string.h�����strlen()
    printf("Please enter your local time:\n");
    /*time ʵ�ִ洢���� length ʵ���жϸ�ʽ plus  ʵ�ּ���  
    first��second���� ��ʵ�ִ洢�����������*/
    char time[5]; // �����ַ�����, Ŀ����ǰ4��������5���ڴ洢��\n��
    int length, first, second, third, forth, plus;  // �������ͱ���
    scanf("%4s", time); 
    length = strlen(time);  // ʶ���ܹ���������ַ�
    if (length>5)
    {  // �������5�����򲻷��ϸ�ʽ
        printf("Wrong formulation of number!");
    }
    else 
    {  // �ñ����洢ÿһ���ַ�ֵ
        first = (int)time[0] -48; //ASCLL��ת��
        if (length == 1)
        {  // ֻ����һ��������ʾ��
            printf("Now UTC is  **00:0%d**\n", first);
            printf("Then UTC is **16:0%d**", first);
        }
        else if ((length == 2)&&(first != 0))
        { // ������������ʾ��
            second = (int)time[1] - 48;
            if ((first>=0)&&(first <6))
            {  //ȷ����ʽ��ȷ
                printf("Now BJT is  **00:%d%d**\n", first, second);
                printf("Then UTC is **16:%d%d**", first, second);
            }
            else
            {
                printf("Wrong number");
            }
        }
        else if ((length == 3)&&(first != 0))
        { // ������������ʾ��ʱ����
            second = (int)time[1]-48;
            third = (int)time[2]-48;
            if ((second >= 0)&&(second < 6))
            { // ȷ����ʽ
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
            &&(second < 4)))&&((third >= 0)&&(third < 6)))  // ʹ����23:59������
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

    