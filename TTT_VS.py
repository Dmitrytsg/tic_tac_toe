from termcolor import colored, cprint

a = [["_"]*3 for i in range(3)]
for i in a:
    print(*i)
flag = True
br = True
per = 0
while flag and br:
    br = False
    sub = True
    if per%2 == 0: m = 'x'
    if per%2 == 1: m = 'o'
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
        win = a[0][0]
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