#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <locale.h>
#include <Windows.h>

char a[9];
size_t per=0;


int main(){
    size_t i,j;
    char massage[15],m[2];
    int n,level;
    bool flag = true,br = true;
    
    if( SetConsoleCP(CP_UTF8) == 0 || SetConsoleOutputCP(CP_UTF8) == 0){
            printf("Error!\n");
        }
    printf("Выберете сложность\nДля того чтобы выбрать 'Лёгко' введите [0]\nДля того чтобы выбрать 'Сложно' введите [1]\n");
    scanf("%d",&level);
    printf("%d",level);
    return 0;
}