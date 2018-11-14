def main():
    string = 0
    switch = []
    row = []
    space1 = space2 = 0
    n = 0
    while True:
        string = input()
        if(string == '-1'):
            break
        space1, space2 = map(int, string.split())
        switch.append(space1)
        row.append(space2)
        n += 1
    for i in range(n):
        identify = check(switch[i], row[i])
        if(identify and switch[i]==1):
            case1(row[i])
            print()
        elif(identify and switch[i]==2):
            case2(row[i])
            print()
        else:
            print('E')
            print()
def check(switch, row):
    if((switch!=1) and (switch!=2)):
        return 0
    elif((switch==1) and ((row<1 or row>18) or (row%2==0))):
        return 0
    elif((switch==2) and (row<1 or row>5)):
        return 0
    return 1
def case1(n):
    n = n // 2
    for i in range(n+1):
        case1_diaplaytop(n, i)
    for i in range(n):
        case1_displaydown(n, i)
def case2(n):
    for i in range(n):
        case2_display(n, i)
def case1_diaplaytop(n, i):
    for j in range(n-i):
        print('.', end='')
    for j in range(i+1):
        print(j+1, end='')
    for j in range(i):
        print(i-j, end='')
    print()
def case1_displaydown(n, i):
    for j in range(i+1):
        print('.', end='')
    for j in range(1, n-i+1):
        print(j, end='')
    for j in range(n-i-1, 0, -1):
        print(j, end='')
    print()
def case2_display(n, i):
    for j in range(i):
        print('.', end='')
    for j in range(n-i, 0, -1):
        print(2*j-1, end='')
    for j in range(1, n-i):
        print(2*j+1, end='')
    print()
main()