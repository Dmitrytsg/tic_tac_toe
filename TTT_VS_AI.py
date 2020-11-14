from termcolor import colored, cprint
import random

def main():
    global a
    a = [["_"]*3 for i in range(3)]
    for i in a:
        print(*i)
    m = "start"
    per = 0
    flag = True
    br = True
    while flag and br:
        br = False
        sub = True
        if per%2 == 0:
            cprint('----Ход ИИ----','blue') 
            AI_move(per)
        if per%2 == 1: 
            m = 'o'
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

def AI_move(per:int):
    """
    -Обработка поля программой 
    -Принимает шаг
    -Возвращает изменённое поле
    param a: array
    param per: move count
    """
    #Первые 2 хода обрабатываем вручную, они ключевые
    if per == 0:
        a[0][0] = 'x'
        return
    elif per == 2:
        if a[2][0] == '_':
            a[2][0] = 'x'
        elif a[2][2] == '_':
            a[2][2] = 'x'
        return
    #ходы дальше обрабатываются автоматически
    else:
        #обрабатываем критическую ситуацию(2 'x')
        for i in range(3): #проверяем строки
            if scan_to_win([i,0],[i,1],[i,2],"x"):
                return
        for i in range(3): #проверяем столбцы
            if scan_to_win([0,i],[1,i],[2,i],'x'):
                return
        if scan_to_win([0,0],[1,1],[2,2],'x'):#проверяем главную диагональ
            return
        if scan_to_win([0,2],[1,1],[2,0],'x'):#проверяем побочную диагональ
            return

        #обрабатываем критическую ситуацию(2 'o')
        for i in range(3): #проверяем строки
            if scan_to_win([i,0],[i,1],[i,2],"o"):
                return
        for i in range(3): #проверяем столбцы
            if scan_to_win([0,i],[1,i],[2,i],'o'):
                return
        if scan_to_win([0,0],[1,1],[2,2],'o'):#проверяем главную диагональ
            return
        if scan_to_win([0,2],[1,1],[2,0],'o'):#проверяем побочную диагональ
            return

        #проверяем случай когда 1 'x' и остальное пусто
        for i in range(3): #проверяем строки
            if scan_to_move([i,0],[i,1],[i,2],"x"):
                return
        for i in range(3): #проверяем столбцы
            if scan_to_move([0,i],[1,i],[2,i],'x'):
                return
        if scan_to_move([0,0],[1,1],[2,2],'x'):#проверяем главную диагональ
            return
        if scan_to_move([0,2],[1,1],[2,0],'x'):#проверяем побочную диагональ
            return

        #во всех остальных случаях значение ставится рандомно
        while True:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            if a[i][j] == '_':
                a[i][j] = 'x'
                break


def scan_to_move(e1,e2,e3,s):#!!!!!!!!!!!! можно сделать рандом !!!!!!!!!!!!
    """
    -Проверяет ситуацию вида x__
    -Сканирует заданную линию на поле
    -Если ситуация, то делает ход
    -Возвращает флаг 
    """
    result = False
    if a[e1[0]][e1[1]] == s and a[e2[0]][e2[1]] == '_' and a[e3[0]][e3[1]] == '_':
        a[e3[0]][e3[1]] = 'x'
        result = True
    if a[e1[0]][e1[1]] == '_' and a[e2[0]][e2[1]] == s and a[e3[0]][e3[1]]  == '_':
        a[e3[0]][e3[1]] = 'x'
        result = True
    if a[e1[0]][e1[1]] == '_' and a[e2[0]][e2[1]] == '_' and a[e3[0]][e3[1]] == s:
        a[e1[0]][e1[1]] = 'x'
        result = True
    return result

def scan_to_win(e1,e2,e3,s):
    """
    -Проверяет ситуацию вида oo_ или xx_
    -Сканирует заданную линию на поле
    -Если ситуация "критическая", то делает ход
    -Возвращает флаг 
    """
    result = False
    if a[e1[0]][e1[1]] == s and a[e2[0]][e2[1]] == s and a[e3[0]][e3[1]] == '_':
        a[e3[0]][e3[1]] = 'x'
        result = True
    if a[e1[0]][e1[1]] == s and a[e2[0]][e2[1]] == '_' and a[e3[0]][e3[1]] == s:
        a[e2[0]][e2[1]] = 'x'
        result = True
    if a[e1[0]][e1[1]] == '_' and a[e2[0]][e2[1]] == s and a[e3[0]][e3[1]] == s:
        a[e1[0]][e1[1]] = 'x'
        result = True
    return result

main()
