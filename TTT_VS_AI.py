def main():
    from termcolor import colored, cprint

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
            a = AI_move(a,per)
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
        state = scan(a)
        flag = state[0]
        br = state[1]
        win = state[2]
        per += 1
    if br == False and flag != False:
        cprint("Победителя нет",'yellow')
    if flag == False:
        print(colored("Победил",'green'),win)

def scan(a):
    """
    -Сканирует поле
    -Принимает поле(двоичный массив 3x3)
    -Возвращает флаг
    """
    win = 0
    br = False
    flag = True
    for i in a:
        if (i[0] == i[1]) and (i[1] == i[2]) and i[0] != '_':
            win = i[0]
            flag = False
    for i in range(3):
        if (a[0][i] == a[1][i]) and (a[1][i] == a[2][i]) and a[2][i] != '_':
            win = a[0][i]
            flag = False
    if (a[0][0] == a[1][1]) and (a[1][1] == a[2][2]) and a[0][0] != '_':
        win = a[0][0]
        flag = False
    if (a[0][2] == a[1][1]) and (a[1][1] == a[2][0]) and a[2][0] != '_':
        win = a[0][0]
        flag = False
    for i in a:
        for j in i:
            if j == '_':
                br = True
    y = [flag,br,win]
    return y

def AI_move(a,per:int):
    """
    -Обработка поля программой 
    -Принимает поле и шаг
    -Возвращает изменённое поле
    param a: array
    param per: move count
    """
    #Первые 3 хода обрабатываем вручную, они ключевые
    if per == 0:
        a[0][0] = 'x'
        return a
    elif per == 2:
        if a[2][0] == '_':
            a[2][0] = 'x'
        elif a[2][2] == '_':
            a[2][2] = 'x'
        return a
    elif per == 4 and a[1][0] != '_' and (a[2][0] == '_' or a[2][2] == '_'):
        if a[2][0] == '_':
            a[2][0] = 'x'
        elif a[2][2] == '_':
            a[2][2] = 'x'
        return a
    #ходы дальше обрабатываются автоматически
    if True:
        #обрабатываем критическую ситуацию(2 'x')
        for i in range(3): #проверяем строки
            r = scan_string(a,i)
            count_x,count_,free_m = r[0],r[2],r[3]
            if count_ != 0:
                if count_x == 2:
                    a[i][free_m] = 'x'
                    return a
            else:
                continue
        for i in range(3): #проверяем столбцы
            r = scan_col(a,i)
            count_x,count_,free_m = r[0],r[2],r[3]
            if count_ != 0:
                if count_x == 2:
                    a[free_m][i] = 'x'
                    return a
            else:
                continue
        r = main_dia(a)#проверяем главную диагональ
        count_x,count_o,count_,free_m = r[0],r[1],r[2],r[3]
        if count_ != 0:
            if count_x == 2:
                a[free_m][free_m] = 'x'
                return a
        r = side_dia(a)#проверяем побочную диагональ
        count_x,count_o,count_,i,j= r[0],r[1],r[2],r[3],r[4]
        if count_ != 0:
            if count_x == 2:
                a[i][j] = 'x'
                return a

        #обрабатываем критическую ситуацию(2 'o')
        for i in range(3): #проверяем строки
            r = scan_string(a,i)
            count_o,count_,free_m = r[1],r[2],r[3]
            if count_ != 0:
                if count_o == 2:
                    a[i][free_m] = 'x'
                    return a
            else:
                continue
        for i in range(3): #проверяем столбцы
            r = scan_col(a,i)
            count_o,count_,free_m = r[1],r[2],r[3]
            if count_ != 0:
                if count_o == 2:
                    a[free_m][i] = 'x'
                    return a 
            else:
                continue
        r = main_dia(a)#проверяем главную диагональ
        count_x,count_o,count_,free_m = r[0],r[1],r[2],r[3]
        if count_ != 0:
            if count_o == 2:
                a[free_m][free_m] = 'x' 
                return a
        r = side_dia(a)#проверяем побочную диагональ
        count_x,count_o,count_,i,j= r[0],r[1],r[2],r[3],r[4]
        if count_ != 0:
            if count_o == 2:
                a[i][j] = 'x' 
                return a

        #проверяем случай когда 1 'x' и остальное пусто
        for i in range(3): #проверяем строки
            r = scan_string(a,i)
            count_x,count_o,count_,free_m = r[0],r[1],r[2],r[3]
            if count_ != 0:
                if count_x == 1 and count_o == 0:
                    a[i][free_m] = 'x'
                    return a
            else:
                continue
        for i in range(3): #проверяем столбцы
            r = scan_col(a,i)
            count_x,count_o,count_,free_m = r[0],r[1],r[2],r[3]
            if count_ != 0:
                if count_x == 1 and count_o == 0:
                    a[free_m][i] = 'x'
                    return a
            else:
                continue
        r = main_dia(a)#проверяем главную диагональ
        count_x,count_o,count_,free_m = r[0],r[1],r[2],r[3]
        if count_ != 0:
            if count_x == 1 and count_o == 0:
                a[free_m][free_m] = 'x'
                return a
        r = side_dia(a)#проверяем побочную диагональ
        count_x,count_o,count_,i,j= r[0],r[1],r[2],r[3],r[4]
        if count_ != 0:
            if count_x == 1 and count_o == 0:
                a[i][j] = 'x'
                return a

        #проверяем все остальные случаи
        for i in range(3): #проверяем строки
            r = scan_string(a,i)
            count_,free_m= r[2],r[3]
            if count_ != 0:
                a[i][free_m] = 'x'
                return a
            else:
                continue
        for i in range(3): #проверяем столбцы
            r = scan_col(a,i)
            count_,free_m = r[2],r[3]
            if count_ != 0:
                a[free_m][i] = 'x'
                return a
            else:
                continue
        r = main_dia(a)#проверяем главную диагональ
        count_x,count_o,count_,free_m = r[0],r[1],r[2],r[3]
        if count_ != 0:
            a[free_m][free_m] = 'x'
            return a
        r = side_dia(a)#проверяем побочную диагональ
        count_x,count_o,count_,i,j= r[0],r[1],r[2],r[3],r[4]
        if count_ != 0:
            a[i][j] = 'x'
            return a
    
def scan_string(a,i):
    """
    -Принимает поле и номер строки
    -Считывает все данные строки
    -Возвращает считанные данные
    """
    count_x = 0
    count_o = 0
    count_ = 0
    free_m = 0
    for j in range(3):
        if a[i][j] == 'x':
            count_x += 1 
        if a[i][j] == 'o':
            count_o += 1
        if a[i][j] == '_':
            count_ += 1
            free_m = j
    r = [count_x,count_o,count_,free_m]
    return r

def scan_col(a,i):
    """
    -Принимает поле и номер столбца
    -Считывает все данные столбца
    -Возвращает считанные данные
    """
    count_x = 0
    count_o = 0
    count_ = 0
    free_m = 0 
    for j in range(3):
        if a[j][i] == 'x':
            count_x += 1 
        if a[j][i] == 'o':
            count_o += 1
        if a[j][i] == '_':
            count_ += 1
            free_m = j
    r = [count_x,count_o,count_,free_m]
    return r

def main_dia(a):
    """
    -Принимает поле
    -Считывает все данные главной диагонали
    -Возвращает считанные данные
    """
    count_x = 0
    count_o = 0
    count_ = 0
    free_m = 0 
    for i in range(3): 
        if a[i][i] == 'x':
            count_x += 1 
        if a[i][i] == 'o':
            count_o += 1
        if a[i][i] == '_':
            count_ += 1
            free_m = i
    r = [count_x,count_o,count_,free_m]
    return r

def side_dia(a):
    i = j = 0
    count_x = 0
    count_o = 0
    count_ = 0
    if a[0][2] == 'x':
        count_x += 1 
    if a[0][2] == 'o':
        count_o += 1
    if a[0][2] == '_':
        count_ += 1
        i = 0 
        j = 2
    if a[1][1] == 'x':
        count_x += 1 
    if a[1][1] == 'o':
        count_o += 1
    if a[1][1] == '_':
        count_ += 1
        i = 1
        j = 1
    if a[2][0] == 'x':
        count_x += 1 
    if a[2][0] == 'o':
        count_o += 1
    if a[2][0] == '_':
        count_ += 1
        i = 2
        j = 0
    r = [count_x,count_o,count_,i,j]
    return r

main()
