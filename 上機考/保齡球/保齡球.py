def main(): #保齡球
    grade = []
    total = 0
    all = 0
    for i in range(10):
        grade.append(tuple(map(int, input().split())))
    for i in range(9):
        if(grade[i][0]==10):
            total = strike(grade, i)
            all += total
            print('%d' %total, end=' ')
        elif(sum(grade[i])==10):
            total = spare(grade, i)
            all += total
            print('%d' %total, end=' ')
        else:
            total = sum(grade[i])
            all += total
            print('%d' %total, end=' ')
    total = sum(grade[9])
    all += total
    print('%d' %total)
    print('%d' %all)

def strike(grade, i):
    if(i==8):
        if(grade[9][0]==10):
            total = (10 + 10 + (grade[9][2] if grade[9][2]!=0 else grade[9][3]))
        else:
            total = (10 + sum(grade[i+1][:2]))
    elif(grade[i+1][0]==10):
        total = 10 + 10 + grade[i+2][0]
    else:
        total = 10 + sum(grade[i+1])
    return total

def spare(grade, i):
    total = 10 + grade[i+1][0]
    return total
main()