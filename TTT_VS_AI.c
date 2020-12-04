#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <locale.h>
#include <Windows.h>

void scan(bool *,bool *,char *);
bool scan_line(int,int,int,int,int,int);

char a[3][3]; /*Поле*/
size_t per=0; /*Ход*/


int main(){
    size_t i,j,co[] = {4,4};
    char m,win,state[3];
    int n = 2,level = 2,result;
    bool flag = TRUE,br = TRUE,sub = TRUE;
    
    if( SetConsoleCP(CP_UTF8) == 0 || SetConsoleOutputCP(CP_UTF8) == 0) printf("Error!\n");

    while(sub){
        printf("Выберете сложность\nДля того чтобы выбрать 'Лёгко' введите [0]\nДля того чтобы выбрать 'Сложно' введите [1]\n");
        scanf("%d",&level);
        fflush(stdin);
        if(level == 1 || level == 0){
            sub = FALSE;
        }
        else{
            printf("Error!--Введено неверное значение.Попробуйте снова.\n\n");
        }
    }
    sub = TRUE;
    if(level == 0) printf("Вы выбрали Лёгкий режим.\n\n");
    if(level == 1) printf("Вы выбрали Сложный режим.\n\n");

    while(sub){
        printf("первыми ходят x\nДля того чтобы выбрать 'x' введите [0]\nДля того чтобы выбрать 'o' введите [1]\n");
        scanf("%d",&n);
        fflush(stdin);
        if(n == 1 || n == 0){
            sub = FALSE;
        }
        else{
            printf("Error!--Введено неверное значение.Попробуйте снова.\n\n");
        } 
    }
    sub = TRUE;
    if(n == 0){
        m = 'x';
        per += 1;
    }
    if(n == 1) m = 'o';
    printf("Вы выбрали '%c'\n\n",m);
    
    for(i=0;i < 3;i++){
        for(j=0;j < 3;j++) a[i][j] = '_';
    }
    for(i=0;i < 3;i++){
        for(j=0;j < 3;j++) printf(" %c ",a[i][j]);
        printf("\n");
    }

    while(flag && br){
        br = false;
        if(per%2 == 0){
            printf("----Ход ИИ----\n");
            /*AI_move(m,level)*/
        }
        if(per%2 == 1){
            while(sub){
                co[0] = 4;
                co[1] = 4;
                printf("Куда хотите поставить '%c':",m);
                for(i=0;i<2;i++) scanf("%zu",&co[i]);
                fflush(stdin);
                if(co[0] > 3 || co[1] > 3){
                    printf("Error!--Введено неверное значение.Попробуйте снова.\n\n");
                    continue;
                }
                if(a[co[0]-1][co[1]-1] != '_'){
                    printf("Данное поле уже занято значком:'%c'\n\n",a[co[0]-1][co[1]-1]);
                    continue;
                }
                else{
                    a[co[0]-1][co[1]-1] = m;
                    sub = FALSE;
                }
            }
            sub = TRUE;
        }
        scan(&flag,&br,&win);
        for(i=0;i < 3;i++){
            for(j=0;j < 3;j++) printf(" %c ",a[i][j]);
            printf("\n");
        }
        per += 1; 
    }
    if(br == false && flag != false) printf("Победителя нет");
    if(flag == false) printf("Победил '%c'",win);

    return 0;
}

void scan(bool *flag,bool *br,char *win){
    for(int i = 0; i < 3; i++){
        if(scan_line(i,0,i,1,i,2)){//для строк
            *win = a[i][0];
            *flag = false;
        }
    }
    for(int i = 0; i < 3; i++){
        if(scan_line(0,i,1,i,2,i)){//для столбцов
            *win = a[0][i];
            *flag = false;
        }
    }
    if(scan_line(0,0,1,1,2,2)){
        *win = a[0][0];
        *flag = false;
    }
    if(scan_line(0,2,1,1,2,0)){
        *win = a[2][0];
        *flag = false;
    }
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if(a[i][j] == '_'){
                *br = true;
            }
        }
    }
}

bool scan_line(int e10,int e11,int e20,int e21,int e30,int e31){
    bool result = false;
    if(a[e10][e11] == a[e20][e21] && a[e20][e21] == a[e30][e31] && a[e30][e31] != '_') result = true;
    return result;
}