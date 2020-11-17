from termcolor import colored, cprint
import random

def main():
    global a

    per = 0
    m = "start"
    massage = "oopss"
    print(colored("Выберете сложность","magenta",attrs=['bold']))
    print((colored("Для того чтобы выбрать 'Лёгко' введите [0]","magenta",attrs=['bold'])))
    print((colored("Для того чтобы выбрать 'Сложно' введите [1]","magenta",attrs=['bold'])))
    level = int(input(""))
    if level == 0: massage = "Лёгкий режим"
    if level == 1: massage = "Сложный режим"
    print((colored("Вы выбрали","green",attrs=['bold'])),colored(massage,"magenta",attrs=['bold']),"\n")
    print(colored("первыми ходят x","magenta",attrs=['bold']))
    print((colored("Для того чтобы выбрать x введите [1]","magenta",attrs=['bold'])))
    print((colored("Для того чтобы выбрать o введите [2]","magenta",attrs=['bold'])))
    n = int(input(""))
    if n == 1: 
        m = "x"
        per += 1
    if n == 2: m = "o"
    print((colored("Вы выбрали","green",attrs=['bold'])),colored(m,"magenta",attrs=['bold']),"\n")
    a = [["_"]*3 for i in range(3)]
    for i in a:
        print(*i)
    
    flag = True
    br = True
    while flag and br:
        br = False
        sub = True
        if per%2 == 0:
            cprint('----Ход ИИ----','blue') 
            AI_move(per,m,level)
        if per%2 == 1:
            while sub:
                print("Куда хотите поставить",m,':')
                i,j = map(int, input().split())
                i -= 1
                j -= 1
                if a[i][j] == '_':
                    a[i][j] = m
                    sub = False
                else:
                    print(colored('Данное поле уже занято значком:','red'),a[i][j])
        for i in a:
            print(*i)
        state = scan()
        flag = state[0]
        br = state[1]
        win = state[2]
        per += 1
    if br == False and flag != False:
        cprint("Победителя нет",'yellow')
    if flag == False:
        print(colored("Победил",'green'),win)

def scan():
    """
    -Сканирует поле на предмет переполненности или выигрыша
    -Принимает поле(двоичный массив 3x3)
    -Возвращает флаг и победителя, если нашёлся
    """
    win = 0
    br = False
    flag = True
    for i in range(3):
        if scan_line([i,0],[i,1],[i,2]):
            win = a[i][0]
            flag = False
        if scan_line([0,i],[1,i],[2,i]):
            win = a[0][i]
            flag = False
    if scan_line([0,0],[1,1],[2,2]):
        win = a[0][0]
        flag = False
    if scan_line([0,2],[1,1],[2,0]):
        win = a[2][0]
        flag = False
    for i in a:
        for j in i:
            if j == '_':
                br = True
    y = [flag,br,win]
    return y
def scan_line(e1,e2,e3):
    result = False
    if a[e1[0]][e1[1]] == a[e2[0]][e2[1]] and a[e2[0]][e2[1]] == a[e3[0]][e3[1]] and a[e3[0]][e3[1]] != '_':
        result = True
    return result

def AI_move(per:int,m:str,level:int):
    """
    -Обработка поля программой 
    -Принимает шаг
    -Возвращает изменённое поле
    param per: move count
    param m: противник
    param level: уровень игры level 1 - сложный; 0 - лёгкий
    """
    value = "start" #значение ИИ в зависимости от параметра m
    #Первые 2 хода обрабатываем вручную, они ключевые
    if m == "o":
        value = "x"
        if level == 1:
            if per == 0:
                a[0][0] = "x"
                return
            elif per == 2:
                if a[2][0] == '_':
                    a[2][0] = 'x'
                elif a[2][2] == '_':
                    a[2][2] = 'x'
                return
    if m == "x":
        value = "o"
        if level == 1:
            if per == 2:
                if a[1][1] == "_": a[1][1] = "o"
                else: a[0][0] = "o"
                return
    #ходы дальше обрабатываются автоматически
    if (per >= 4 and level == 1) or level == 0:
        #обрабатываем критическую ситуацию(2 value)
        for i in range(3): #проверяем строки
            if scan_to_win([i,0],[i,1],[i,2],value,value):
                return
        for i in range(3): #проверяем столбцы
            if scan_to_win([0,i],[1,i],[2,i],value,value):
                return
        if scan_to_win([0,0],[1,1],[2,2],value,value):#проверяем главную диагональ
            return
        if scan_to_win([0,2],[1,1],[2,0],value,value):#проверяем побочную диагональ
            return

        #обрабатываем критическую ситуацию(2 m)
        for i in range(3): #проверяем строки
            if scan_to_win([i,0],[i,1],[i,2],m,value):
                return
        for i in range(3): #проверяем столбцы
            if scan_to_win([0,i],[1,i],[2,i],m,value):
                return
        if scan_to_win([0,0],[1,1],[2,2],m,value):#проверяем главную диагональ
            return
        if scan_to_win([0,2],[1,1],[2,0],m,value):#проверяем побочную диагональ
            return

        #проверяем случай когда 1 value и остальное пусто
        for i in range(3): #проверяем строки
            if scan_to_move([i,0],[i,1],[i,2],value,value):
                return
        for i in range(3): #проверяем столбцы
            if scan_to_move([0,i],[1,i],[2,i],value,value):
                return
        if scan_to_move([0,0],[1,1],[2,2],value,value):#проверяем главную диагональ
            return
        if scan_to_move([0,2],[1,1],[2,0],value,value):#проверяем побочную диагональ
            return

        #во всех остальных случаях значение ставится рандомно
        while True:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            if a[i][j] == '_':
                a[i][j] = value
                break


def scan_to_move(e1,e2,e3,s,m):#!!!!!!!!!!!! можно сделать рандом !!!!!!!!!!!!
    """
    -Проверяет ситуацию вида x__
    -Сканирует заданную линию на поле
    -Если ситуация, то делает ход
    -Возвращает флаг 
    -param s: значение которое ищем
    -param m: значение ИИ
    """
    result = False
    if a[e1[0]][e1[1]] == s and a[e2[0]][e2[1]] == '_' and a[e3[0]][e3[1]] == '_':
        a[e3[0]][e3[1]] = m
        result = True
    if a[e1[0]][e1[1]] == '_' and a[e2[0]][e2[1]] == s and a[e3[0]][e3[1]]  == '_':
        a[e3[0]][e3[1]] = m
        result = True
    if a[e1[0]][e1[1]] == '_' and a[e2[0]][e2[1]] == '_' and a[e3[0]][e3[1]] == s:
        a[e1[0]][e1[1]] = m
        result = True
    return result

def scan_to_win(e1,e2,e3,s,m):
    """
    -Проверяет ситуацию вида oo_ или xx_
    -Сканирует заданную линию на поле
    -Если ситуация "критическая", то делает ход
    -Возвращает флаг
    -param s: значение которое ищем
    -param m: значение ИИ 
    """
    result = False
    if a[e1[0]][e1[1]] == s and a[e2[0]][e2[1]] == s and a[e3[0]][e3[1]] == '_':
        a[e3[0]][e3[1]] = m
        result = True
    if a[e1[0]][e1[1]] == s and a[e2[0]][e2[1]] == '_' and a[e3[0]][e3[1]] == s:
        a[e2[0]][e2[1]] = m
        result = True
    if a[e1[0]][e1[1]] == '_' and a[e2[0]][e2[1]] == s and a[e3[0]][e3[1]] == s:
        a[e1[0]][e1[1]] = m
        result = True
    return result

main()
