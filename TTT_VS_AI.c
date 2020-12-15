#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdbool.h>
#include <locale.h>
#include <Windows.h>
#include <time.h>


int scan(bool *,bool *,char *);
bool scan_line(char,char,char);
int AI_move();
int scan_to_move(char *, char *, char *);
int scan_to_win(char *,char *,char *,char);


 
char a[3][3]; /*Поле*/
size_t per=0; /*Ход*/
char m/*соперник*/,value/*ИИ*/;
int level=2;/*уровень игры*/

int main(){
    system("CLS");
    size_t i,j,co[2];
    char win;
    int user_choice = 2;
    bool flag = TRUE,br = TRUE,user_br = TRUE,sub = TRUE;

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
        scanf("%d",&user_choice);
        fflush(stdin);
        if(user_choice == 1 || user_choice == 0){
            sub = FALSE;
        }
        else{
            printf("Error!--Введено неверное значение.Попробуйте снова.\n\n");
        } 
    }
    sub = TRUE;
    if(user_choice == 0){
        m = 'x';
        per += 1;
    }
    if(user_choice == 1) m = 'o';
    printf("Вы выбрали '%c'\n\n",m);
    
    printf("Ставьте свой знак по аналогии с примером:\nПоставим 'x' в: 1 1\n");
    for(i=0;i < 3;i++){
        for(j=0;j < 3;j++) a[i][j] = '_';
    }
    a[0][0] = 'x';
    for(i=0;i < 3;i++){
        for(j=0;j < 3;j++) printf(" %c ",a[i][j]);
        printf("\n");
    }
    printf("Поставим 'x' в: 2 3\n");
    a[1][2] = 'x';
    for(i=0;i < 3;i++){
        for(j=0;j < 3;j++) printf(" %c ",a[i][j]);
        printf("\n");
    }
    printf("\n\n");

    for(i=0;i < 3;i++){
        for(j=0;j < 3;j++) a[i][j] = '_';
    }
    for(i=0;i < 3;i++){
        for(j=0;j < 3;j++) printf(" %c ",a[i][j]);
        printf("\n");
    }

    while(flag && br && user_br){
        if(per%2 == 0){
            printf("----Ход ИИ----\n");
            if(AI_move() != 0){
                printf("ERROR! Func: AI_move\n");
                return 1;
            }
        }
        if(per%2 == 1){
            if(level == 1) printf("Режим: сложный | ");
            if(level == 0) printf("Режим: лёгкий | ");
            printf("Вы играете за: '%c'\n",m);
            while(sub){
                co[0] = 4;
                co[1] = 4;
                printf("Куда хотите поставить '%c' (Чтобы выйти введите 5 5):",m);
                for(i=0;i<2;i++) scanf("%zu",&co[i]);
                fflush(stdin);
                if(co[0] == 5 && co[1] == 5){
                    user_br = false;
                    break;    
                }
                if(co[0] > 3 || co[1] > 3 || co[0] < 1 || co[1] < 1){
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
        for(i=0;i < 3;i++){
            for(j=0;j < 3;j++) printf(" %c ",a[i][j]);
            printf("\n");
        }
        if(scan(&flag,&br,&win) != 0){
            printf("ERROR! Func: scan, with argument %d\n",scan(&flag,&br,&win));
            return 1;
        }
        per += 1; 
    }
    if(!user_br) printf("Игра завершена");
    if(!br && flag) printf("Победителя нет");
    if(!flag) printf("Победил '%c'",win);
    return 0;
}

int scan(bool *flag,bool *br,char *win){
    if(flag == NULL) return 1;
    if(br == NULL) return 2;
    if(win == NULL) return 3;

    *br = false;
    for(size_t i = 0; i < 3; i++){
        if(scan_line(a[i][0],a[i][1],a[i][2])){//для строк
            *win = a[i][0];
            *flag = false;
        }
    }
    for(size_t i = 0; i < 3; i++){
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
    for(size_t i = 0; i < 3; i++){
        for(size_t j = 0; j < 3; j++){
            if(a[i][j] == '_'){
                *br = true;
            }
        }
    }
    return 0;
}

bool scan_line(char el1,char el2,char el3){
    bool result = false;
    if(el1 == el2 && el2 == el3 && el3 != '_') result = true;
    return result;
}

int AI_move(){
    int result;
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
        for(size_t i = 0; i < 3; i++){//для строк
            result = scan_to_win(&a[i][0],&a[i][1],&a[i][2],value);
            if(result && result != 1 && result != 2 && result != 3){
                return 0;
            }
            else if(result == 1 || result == 2 || result == 3){
                printf("ERROR! Func: scan_to_win\n");
                return 1;
            }
        }
        
        for(size_t i = 0; i < 3; i++){//для столбцов
            result = scan_to_win(&a[0][i],&a[1][i],&a[2][i],value);
            if(result && result != 1 && result != 2 && result != 3){
                return 0;
            }
            else if(result == 1 || result == 2 || result == 3){
                printf("ERROR! Func: scan_to_win\n");
                return 1;
            }
        }

        result = scan_to_win(&a[0][0],&a[1][1],&a[2][2],value);
        if(result && result != 1 && result != 2 && result != 3){
            return 0;
        }
        else if(result == 1 || result == 2 || result == 3){
            printf("ERROR! Func: scan_to_win\n");
            return 1;
        }

        result = scan_to_win(&a[0][2],&a[1][1],&a[2][0],value);
        if(result && result != 1 && result != 2 && result != 3){
            return 0;
        }
        else if(result == 1 || result == 2 || result == 3){
            printf("ERROR! Func: scan_to_win\n");
            return 1;
        }
        //обрабатываем критическую ситуацию(2 m)
        for(size_t i = 0; i < 3; i++){//для строк
            result = scan_to_win(&a[i][0],&a[i][1],&a[i][2],m);
            if(result && result != 1 && result != 2 && result != 3){
                return 0;
            }
            else if(result == 1 || result == 2 || result == 3){
                printf("ERROR! Func: scan_to_win\n");
                return 1;
            }
        }
        
        for(size_t i = 0; i < 3; i++){//для столбцов
            result = scan_to_win(&a[0][i],&a[1][i],&a[2][i],m);
            if(result && result != 1 && result != 2 && result != 3){
                return 0;
            }
            else if(result == 1 || result == 2 || result == 3){
                printf("ERROR! Func: scan_to_win\n");
                return 1;
            }
        }

        result = scan_to_win(&a[0][0],&a[1][1],&a[2][2],m);
        if(result && result != 1 && result != 2 && result != 3){
            return 0;
        }
        else if(result == 1 || result == 2 || result == 3){
            printf("ERROR! Func: scan_to_win\n");
            return 1;
        }

        result = scan_to_win(&a[0][2],&a[1][1],&a[2][0],m);
        if(result && result != 1 && result != 2 && result != 3){
            return 0;
        }
        else if(result == 1 || result == 2 || result == 3){
            printf("ERROR! Func: scan_to_win\n");
            return 1;
        }

        //проверяем случай когда 1 value и остальное пусто
        for(size_t i = 0; i < 3; i++){//для строк
            result = scan_to_move(&a[i][0],&a[i][1],&a[i][2]);
            if(result && result != 1 && result != 2 && result != 3){
                return 0;
            }
            else if(result == 1 || result == 2 || result == 3){
                printf("ERROR! Func: scan_to_move\n");
                return 1;
            }
        }

        for(size_t i = 0; i < 3; i++){//для столбцов
            result = scan_to_move(&a[0][i],&a[1][i],&a[2][i]); 
            if(result && result != 1 && result != 2 && result != 3){
                return 0;
            }
            else if(result == 1 || result == 2 || result == 3){
                printf("ERROR! Func: scan_to_move\n");
                return 1;
            }
        }

        result = scan_to_move(&a[0][0],&a[1][1],&a[2][2]);
        if(result && result != 1 && result != 2 && result != 3){
            return 0;
        }
        else if(result == 1 || result == 2 || result == 3){
            printf("ERROR! Func: scan_to_move\n");
            return 1;
        }

        result = scan_to_move(&a[0][2],&a[1][1],&a[2][0]);
        if(result && result != 1 && result != 2 && result != 3){
            return 0;
        }
        else if(result == 1 || result == 2 || result == 3){
            printf("ERROR! Func: scan_to_move\n");
            return 1;
        }
        //во всех остальных случаях значение ставится рандомно
        srand(time(NULL));
        while(true){
            size_t i = rand()%3, j = rand()%3;
            if(a[i][j] == '_'){
                a[i][j] = value;
                return 0;
            }
        }
    }
    return 1;
}

int scan_to_win(char *el1,char *el2,char *el3,char val){
    if(el1 == NULL) return 1;
    if(el2 == NULL) return 2;
    if(el3 == NULL) return 3;
    int result = 0;
	if (*el1 == *el2 && *el1 == val && *el3 == '_'){
		*el3 = value;
		result = 5;
	}
	if (*el1 == *el3 && *el1 == val && *el2 == '_'){
		*el2 = value;
		result = 5;
    }
	if (*el2 == *el3 && *el2 == val && *el1 == '_'){
		*el1 = value;
		result = 5;
    }
    return result;
}

int scan_to_move(char *el1, char *el2, char *el3){
    if(el1 == NULL) return 1;
    if(el2 == NULL) return 2;
    if(el3 == NULL) return 3;
	int result = 0;
	size_t i = rand()%2;
	srand(time(NULL));
	if (*el1 == value && *el2 == '_' && *el3 == '_') {
		if (i == 0) *el2 = value;
		else *el3 = value;
		result = 4;
	}
	if (*el2 == value && *el1 == '_' && *el3 == '_') {
		if (i == 0) *el1 = value;
		else *el3 = value;
		result = 4;
	}
	if (*el3 == value && *el1 == '_' && *el2 == '_') {
		if (i == 0) *el1 = value;
		else *el2 = value;
		result = 4;
	}
	return result;
}