from termcolor import colored, cprint


def for_x(a,per:int):
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
    else:
        for i in range(3): #проверяем строки на критическую ситуацию(2 'x')
            count_x = 0
            count_o = 0
            count_ = 0
            y = 0
            for j in range(3):
                if a[i][j] == 'x':
                    count_x += 1 
                if a[i][j] == 'o':
                    count_o += 1
                if a[i][j] == '_':
                    count_ += 1
                    y = j
            if count_ != 0:
                if count_x == 2:
                    a[i][y] = 'x'
                    return a
            else:
                continue
        for i in range(3): #проверяем столбцы на критическую ситуацию(2 'x')
            count_x = 0
            count_o = 0
            count_ = 0
            y = 0
            for j in range(3):
                if a[j][i] == 'x':
                    count_x += 1 
                if a[j][i] == 'o':
                    count_o += 1
                if a[j][i] == '_':
                    count_ += 1
                    y = j
            if count_ != 0:
                if count_x == 2:
                    a[y][i] = 'x'
                    return a
            else:
                continue

        #проверяем главную диагональ на критическую ситуацию(2 'x')
        count_x = 0
        count_o = 0
        count_ = 0
        y = 0
        for i in range(3): 
            if a[i][i] == 'x':
                count_x += 1 
            if a[i][i] == 'o':
                count_o += 1
            if a[i][i] == '_':
                count_ += 1
                y = i
        if count_ != 0:
            if count_x == 2:
                a[y][y] = 'x'
                return a
        #проверяем побочную диагональ на критическую ситуацию(2 'x')
        count_x = 0
        count_o = 0
        count_ = 0
        y = 0
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
        if count_ != 0:
            if count_x == 2:
                a[i][j] = 'x'
                return a

        #проверяем на критическую ситуацию(2 'o')
        for i in range(3): #проверяем строки
            count_x = 0
            count_o = 0
            count_ = 0
            y = 0
            for j in range(3):
                if a[i][j] == 'x':
                    count_x += 1 
                if a[i][j] == 'o':
                    count_o += 1
                if a[i][j] == '_':
                    count_ += 1
                    y = j
            if count_ != 0:
                if count_o == 2:
                    a[i][y] = 'x'
                    return a
            else:
                continue
        for i in range(3): #проверяем столбцы
            count_x = 0
            count_o = 0
            count_ = 0
            y = 0
            for j in range(3):
                if a[j][i] == 'x':
                    count_x += 1 
                if a[j][i] == 'o':
                    count_o += 1
                if a[j][i] == '_':
                    count_ += 1
                    y = j
            if count_ != 0:
                if count_o == 2:
                    a[y][i] = 'x'
                    return a 
            else:
                continue
        #проверяем главную диагональ
        count_x = 0
        count_o = 0
        count_ = 0
        y = 0
        for i in range(3): 
            if a[i][i] == 'x':
                count_x += 1 
            if a[i][i] == 'o':
                count_o += 1
            if a[i][i] == '_':
                count_ += 1
                y = i
        if count_ != 0:
            if count_o == 2:
                a[y][y] = 'x' 
                return a
        #проверяем побочную диагональ
        count_x = 0
        count_o = 0
        count_ = 0
        y = 0
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
        if count_ != 0:
            if count_o == 2:
                a[i][j] = 'x' 
                return a

        #проверяем случай когда 1 'x' и остальное пусто
        for i in range(3): #проверяем строки
            count_x = 0
            count_o = 0
            count_ = 0
            y = 0
            for j in range(3):
                if a[i][j] == 'x':
                    count_x += 1 
                if a[i][j] == 'o':
                    count_o += 1
                if a[i][j] == '_':
                    count_ += 1
                    y = j
            if count_ != 0:
                if count_x == 1 and count_o == 0:
                    a[i][y] = 'x'
                    return a
            else:
                continue
        for i in range(3): #проверяем столбцы
            count_x = 0
            count_o = 0
            count_ = 0
            y = 0
            for j in range(3):
                if a[j][i] == 'x':
                    count_x += 1 
                if a[j][i] == 'o':
                    count_o += 1
                if a[j][i] == '_':
                    count_ += 1
                    y = j
            if count_ != 0:
                if count_x == 1 and count_o == 0:
                    a[y][i] = 'x'
                    return a
            else:
                continue
        #проверяем главную диагональ
        count_x = 0
        count_o = 0
        count_ = 0
        y = 0
        for i in range(3): 
            if a[i][i] == 'x':
                count_x += 1 
            if a[i][i] == 'o':
                count_o += 1
            if a[i][i] == '_':
                count_ += 1
                y = i
        if count_ != 0:
            if count_x == 1 and count_o == 0:
                a[y][y] = 'x'
                return a
        #проверяем побочную диагональ
        count_x = 0
        count_o = 0
        count_ = 0
        y = 0
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
        if count_ != 0:
            if count_x == 1 and count_o == 0:
                a[i][j] = 'x'
                return a

        #проверяем все остальныые случаи
        for i in range(3): #проверяем строки
            count_x = 0
            count_o = 0
            count_ = 0
            y = 0
            for j in range(3):
                if a[i][j] == 'x':
                    count_x += 1 
                if a[i][j] == 'o':
                    count_o += 1
                if a[i][j] == '_':
                    count_ += 1
                    y = j
            if count_ != 0:
                a[i][y] = 'x'
                return a
            else:
                continue
        for i in range(3): #проверяем столбцы
            count_x = 0
            count_o = 0
            count_ = 0
            y = 0
            for j in range(3):
                if a[j][i] == 'x':
                    count_x += 1 
                if a[j][i] == 'o':
                    count_o += 1
                if a[j][i] == '_':
                    count_ += 1
                    y = j
            if count_ != 0:
                a[y][i] = 'x'
                return a
            else:
                continue
        #проверяем главную диагональ
        count_x = 0
        count_o = 0
        count_ = 0
        y = 0
        for i in range(3): 
            if a[i][i] == 'x':
                count_x += 1 
            if a[i][i] == 'o':
                count_o += 1
            if a[i][i] == '_':
                count_ += 1
                y = i
        if count_ != 0:
            a[y][y] = 'x'
            return a
        #проверяем побочную диагональ
        count_x = 0
        count_o = 0
        count_ = 0
        y = 0
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
        if count_ != 0:
            a[i][j] = 'x'
            return a

a = [["_"]*3 for i in range(3)]
for i in a:
    print(*i)
flag = True
br = True
per = 0
while flag and br:
    br = False
    sub = True
    if per%2 == 0: 
        cprint('----Ход ИИ----','blue')
        a = for_x(a,per)
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
        win = a[0][2]
        flag = False
    for i in a:
        for j in i:
            if j == '_':
                br = True
    per += 1
if br == False and flag != False:
    cprint("Победителя нет",'yellow')
if flag == False:
    print(colored("Победил",'green'),win)