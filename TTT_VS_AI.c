#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdbool.h>
#include <locale.h>
#include <Windows.h>
#include <time.h>


void scan(bool *,bool *,char *);
bool scan_line(char,char,char);
int AI_move();
bool scan_to_move(char *, char *, char *);
bool scan_to_win(char *,char *,char *,char);



char a[3][3]; /*Поле*/
size_t per=0; /*Ход*/
char m/*соперник*/,value/*ИИ*/;
int level = 2;/*уровень игры*/

int main(){
    size_t i,j,co[] = {4,4};
    char win,state[3];
    int n = 2,result;
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
            AI_move();
        }
        if(per%2 == 1){
            while(sub){
                co[0] = 4;
                co[1] = 4;
                printf("Куда хотите поставить '%c':",m);
                for(i=0;i<2;i++) scanf("%zu",&co[i]);
                fflush(stdin);
                if(co[0] > 3 || co[1] > 3 || co[0] < 1 || co[0] < 1){
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
        if(scan_line(a[i][0],a[i][1],a[i][2])){//для строк
            *win = a[i][0];
            *flag = false;
        }
    }
    for(int i = 0; i < 3; i++){
        if(scan_line(a[0][i],a[1][i],a[2][i])){//для столбцов
            *win = a[0][i];
            *flag = false;
        }
    }
    if(scan_line(a[0][0],a[1][1],a[2][2])){
        *win = a[0][0];
        *flag = false;
    }
    if(scan_line(a[0][2],a[1][1],a[2][0])){
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

bool scan_line(char el1,char el2,char el3){
    bool result = false;
    if(el1 == el2 && el2 == el3 && el3 != '_') result = true;
    return result;
}

int AI_move(){
    if(m == 'o'){
        value = 'x';
        if(level == 1){
            if(per == 0){
                a[0][0] = 'x';
                return 0;
            }
            if(per == 2){
                if(a[2][0] == '_') a[2][0] = value;
                else a[2][2] = value;
                return 0;
            }
        }
    }
    if(m == 'x'){
        value = 'o';
        if(level == 1){
            if(per == 2){
                if(a[1][1] == '_') a[1][1] = value;
                else a[0][0] = value;
                return 0;
            }
        }
    }
    if((per >= 4 && level == 1) || (level == 0)){
        //обрабатываем критическую ситуацию(2 value)
        for(int i = 0; i < 3; i++){
           if(scan_to_win(&a[i][0],&a[i][1],&a[i][2],value)){//для строк
                return 0;
            }
        }
        
        for(int i = 0; i < 3; i++){
            if(scan_to_win(&a[0][i],&a[1][i],&a[2][i],value)){//для столбцов
                return 0;
            }
        }
        if(scan_to_win(&a[0][0],&a[1][1],&a[2][2],value)){
            return 0;
        }
        if(scan_to_win(&a[0][2],&a[1][1],&a[2][0],value)){
            return 0;
        }
        //обрабатываем критическую ситуацию(2 m)
        for(int i = 0; i < 3; i++){
            if(scan_to_win(&a[i][0],&a[i][1],&a[i][2],m)){//для строк
                return 0;
            }
        }
        for(int i = 0; i < 3; i++){
            if(scan_to_win(&a[0][i],&a[1][i],&a[2][i],m)){//для столбцов
                return 0;
            }
        }
        if(scan_to_win(&a[0][0],&a[1][1],&a[2][2],m)){
            return 0;
        }
        if(scan_to_win(&a[0][2],&a[1][1],&a[2][0],m)){
            return 0;
        }
        //проверяем случай когда 1 value и остальное пусто
        for(int i = 0; i < 3; i++){
            if(scan_to_move(&a[i][0],&a[i][1],&a[i][2])){//для строк
                return 0;
            }
        }
        for(int i = 0; i < 3; i++){
            if(scan_to_move(&a[0][i],&a[1][i],&a[2][i])){//для столбцов
                return 0;
            }
        }
        if(scan_to_move(&a[0][0],&a[1][1],&a[2][2])){
            return 0;
        }
        if(scan_to_move(&a[0][2],&a[1][1],&a[2][0])){
            return 0;
        }
        //во всех остальных случаях значение ставится рандомно
        srand(time(NULL));
        while(true){
            int i = rand()%3, j = rand()%3;
            if(a[i][j] == '_'){
                a[i][j] = value;
                return 0;
            }
        }
    }
    printf("ERROR! AI_move\n");
    return 1;
}

bool scan_to_win(char *el1,char *el2,char *el3,char val){
    bool result = false;
	if (*el1 == *el2 && *el1 == val && *el3 == '_'){
		*el3 = value;
		result = true;
	}
	if (*el1 == *el3 && *el1 == val && *el2 == '_'){
		*el2 = value;
		result = true;
    }
	if (*el2 == *el3 && *el2 == val && *el1 == '_'){
		*el1 = value;
		result = true;
    }
    return result;
}

bool scan_to_move(char *el1, char *el2, char *el3){
	bool result = false;
	size_t i;
	srand(time(NULL));
	i=rand()%2;	
	if (*el1 == value && *el2 == '_' && *el3 == '_') {
		if (i==0) *el2 = value;
		else *el3 = value;
		result = true;
	}
	if (*el2 == value && *el1 == '_' && *el3 == '_') {
		if (i == 0) *el1 = value;
		else *el3 = value;
		result = true;
	}
	if (*el3 == value && *el1 == '_' && *el2 == '_') {
		if (i == 0) *el1 = value;
		else *el2 = value;
		result = true;
	}
	return result;
}