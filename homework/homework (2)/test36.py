def hand():
    poker = [input().split() for i in range(4)]
    return poker

def say(): #叫牌
    num = 1 #目前P1叫牌
    count = 0 #數pass
    check = '' #判斷與前面叫牌的大小
    while True:
        now = input()
        if(now=='pass'):
            if(check!=''): count += 1
            else: return 0, num
        else:
            if((now[:-1]>check[:-1] or check[-1]>now[-1]) and now[:-1]<='3'):
                check = now
                count = 0
            else:
                return 0, num
        if(count == 3):
            return check, (num+2 if num <=2 else (num+2)%4)
        num = (num+1)//5 + (num+1)%5

def game(): #遊戲
    poker = hand() #發牌
    win, num = say() #叫牌
    if(win!=0):
        grade = play(poker, win[-1], num) #打牌
        output(grade, int(win[:-1]), num-1 if num!=1 else 4) if grade!=0 else print('ERROR') #輸出結果
    else:
        print('ERROR')

def play(poker, win, current): #打牌
    grade = [0, 0, 0, 0]
    for j in range(3):
        counter = current
        now = input().split()
        now_suit = now[0][-1]
        suit = [i[-1] for i in now]
        num = [int(i[:-1]) for i in now]
        for i in range(4):
            if(not now[i] in poker[counter-1] or (now[i][-1] != now_suit and now_suit in [i[-1] for i in poker[counter-1]])):
                return 0
            num[i] = 14 if(num[i]==1) else num[i]
            poker[counter-1].remove(now[i]) #刪除玩家手上的牌
            counter = counter + 1 if(counter!=4) else 1
        if(suit.count(win)!=0):
            for i in range(4):
                num[i] = 0 if suit[i] != win else num[i]
            current = (current + num.index(max(num)))%4 if (current + num.index(max(num)))%4!=0 else 4
        else:
            for i in range(4):
                num[i] = 0 if suit[i] != now_suit else num[i]
            current = (current + num.index(max(num)))%4 if (current + num.index(max(num)))%4!=0 else 4
        grade[current-1] += 1
    return grade

def output(grade, win, num): #輸出結果
    for i in grade:
        print(i)
    if(num==1 or num==3):
        if(grade[0]+grade[2]>=win):
            print('P1 P3')
        else:
            print('P2 P4')
    else:
        if(grade[1]+grade[3]>=win):
            print('P2 P4')
        else:
            print('P1 P3')
game()                                       