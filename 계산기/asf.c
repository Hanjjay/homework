#include <stdio.h>

float add(int a, int b){
    return a + b ;
}

float minus(int a, int b){
    return a - b;
}

float multiply(int a, int b){
    return a * b;
}

float division(int a, int b){

    return (float)a / (float)b ;
}

int verification(char _sign){
    if (_sign == '+' || _sign == '-' || _sign == '*' || _sign == '/')
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
    

}



float calculate(char a , int b, int c){

    if (a == '+'){
        return add(b,c);
    }
    else if (a == '-')
    {
        return minus(b,c);
    }
    else if (a == '*')
    {
        return multiply(b,c);
    }
    else if (a == '/')
    {
        return division(b,c);
    }
    
    
    return 0;
}



int main(void){

    int num1;
    int num2;
    char sign[2];
    float output;
    int ver;

    printf("첫번째 입력값:");
    scanf("%d",&num1);

    printf("두번째값 입력:");
    scanf("%d",&num2);

    printf("부호 입력:");
    scanf("%s",sign);

    ver = verification(sign[0]);

    if (ver == 0){
        return printf("잘못된 자료형입니다. \n");
    }

    output = calculate(sign[0],num1,num2);

    printf("결과:%f \n",output);




    // printf("1st num: %d, second num: %d, sign is: %s \n\n", num1, num2, sign); // test code
    // float a = 1.0f/2.0f;
    // printf("%f \n\n", a); // test code
    return 0;
}