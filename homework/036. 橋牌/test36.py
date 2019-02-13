"""
036. 橋牌
撲克牌四種花色分別是黑桃、紅心、磚塊、梅花，定義 A~D。
撲克牌數字1~13，與四種花色共有52張牌。
編碼規則為數字+花色，例如 1A 表示黑桃 A、7C 表示磚塊 7，13D 表示梅花 K。
花色大小：黑桃>紅心>方塊>梅花
數字大小：2最小，A最大

輸入說明:
共有P1、P2、P3、P4
P1、P3一組，P2、P4一組
1. 每人先發13張牌
2. 先叫牌，由P1開始叫牌，叫到成局(決定王牌花色)為止，最多叫到3墩
3. 成局後出牌，由成局人的下一位(順時針)開始出牌，
所有人出完牌後開始比牌，此回合比牌最高者獲得一墩，
且成為下一輪出牌者，共玩三輪。
輸出說明:
由P1~P4依序輸出墩數，輸出獲勝組玩家。
錯誤狀況
1.叫牌未依照規則，則輸出ERROR
2.出牌時，第一位出牌的人決定花色，若是沒有同花色才能出別的花色，
若違反則輸出ERROR 。
3.出牌時出自己沒有的牌

Input :
2A 12B 1B 13D 11A 8A 10A 3D 1D 4D 10D 12A 3B
8B 1A 1C 13C 4A 9A 7B 7C 8C 12C 9D 12D 13B
10B 5C 5D 2D 4B 5B 9B 3C 9C 10C 7D 11D 8D
3A 2B 5A 2C 7A 6B 11B 4C 11C 6A 6C 6D 13A
1A //P1開始叫牌(順時針)
2D
2B
pass
pass
3C
pass
pass
pass //成局 王牌花色為C(磚塊)，成局人為P2，叫牌階段結束
10B 2B 12B 8B //P3(成局人下一位)出牌，所以出牌順序是P3 P4 P1 P2
11A 1A 5C 5A //P1(獲勝者)出牌，所以出牌順序是 P1 P2 P3 P4
5D 6D 3D 12D //P3(獲勝者)出牌，所以出牌順序是 P3 P4 P1 P2
說明:
第一局 10B 2B 12B 8B 大小順序為 2B <8B < 10B < 12B，此局P1獲勝，P1獲得一墩
第二局 11A 1A 5C 5A 大小順序為 5A < 11A < 1A <5C，此局P3獲勝，P3獲得一墩
第三局 5D 6D 3D 12D 大小順序為 3D < 5D < 6D < 12D，12D(王牌花色)最大，
此局P2獲勝，P2獲得一墩。
output :
1
1
1
0
P1 P3 //P2成局人隊伍墩數不足於3墩，所以另一隊(P1 P3)獲勝
---------------------------------------
input:
2A 12B 1C 13D 11A 8A 10A 6C 10C 4D 10D 13A 13C
8B 2B 7A 11C 4A 9A 7B 7C 5C 12C 9D 12D 13B
10B 8C 5D 6A 4B 5B 9B 5A 3C 9C 1D 7D 12A
3A 3B 2C 1A 6B 11B 4C 1B 2D 11D 3D 6D 8D
1C
1A
2D
2B
pass
pass
pass //P4贏 花色B(紅心)
8A 4A 12A 1A //P1 P2 P3 P4
2C 1C 5C 5A // P4 P1 P2 P3，P3手中還有花色Ｃ牌，違反出牌原則
2A 9A 12A 3A
output:
ERROR
--------------------------------------------
input:
2A 12B 1C 13D 11A 8A 10A 6C 10C 4D 10D 13A 13C
8B 2B 7A 11C 4A 9A 7B 7C 5C 12C 9D 12D 13B
10B 8C 5D 6A 4B 5B 9B 5A 3C 9C 1D 7D 12A
3A 3B 2C 1A 6B 11B 4C 1B 2D 11D 3D 6D 8D
1C
1A
2D
2B
2C //違反
pass
pass
pass
8A 4A 12A 1A
2C 1C 5C 5A
2A 9A 12A 3A
output:
ERROR
"""

def hand(): #輸入player個別手上的牌
    poker = [input().split() for i in range(4)]
    return poker

def say(): #叫牌
    num = 1 #目前P1叫牌
    count = 0 #數pass
    past = '' #前一位叫的牌
    while True:
        now = input() #輸入叫牌
        if(now=='pass'):
            if(past!=''): count += 1 #判斷前一位叫牌者 是否有叫牌
            else: return 0, num
        else:
            if((now[:-1]>past[:-1] or past[-1]>now[-1]) and now[:-1]<='3'): #檢查前一位與現在叫牌者是否違規
                past = now
                count = 0
            else:
                return 0, num
        if(count == 3): #連續3個pass之後 最後一位叫牌者成局
            return past, (num+2 if num <=2 else (num+2)%4) #回傳贏的牌及成局者
        num = (num+1)//5 + (num+1)%5 #輪到下一位player

def game(): #遊戲
    poker = hand() #發牌
    win, num = say() #叫牌
    if(win!=0):
        grade = play(poker, win[-1], num) #打牌
        output(grade, int(win[:-1]), num-1 if num!=1 else 4) if grade!=0 else print('ERROR') #輸出結果
    else:
        print('ERROR')

def play(poker, win, current): #打牌
    grade = [0, 0, 0, 0] #player分數
    for j in range(3): #三局
        counter = current #目前輪到誰
        now = input().split() #出牌
        now_suit = now[0][-1] #目前要出的花色
        suit = [i[-1] for i in now] #個別出牌的花色
        num = [int(i[:-1]) for i in now] #個別出牌的數字
        for i in range(4): #出牌
            if(not now[i] in poker[counter-1] or (now[i][-1] != now_suit and now_suit in [i[-1] for i in poker[counter-1]])): #檢查出錯牌or出沒牌
                return 0
            num[i] = 14 if(num[i]==1) else num[i] #一律1->14
            poker[counter-1].remove(now[i]) #刪除玩家手上已出牌的牌 
            counter = counter + 1 if(counter!=4) else 1 #player 1 ~ player 4
        if(suit.count(win)!=0): #先判斷花色是否有王牌
            for i in range(4):
                num[i] = 0 if suit[i] != win else num[i] #除了王牌花色其餘刪除
            current = (current + num.index(max(num)))%4 if (current + num.index(max(num)))%4!=0 else 4 #判斷誰贏
        else:
            for i in range(4):
                num[i] = 0 if suit[i] != now_suit else num[i] #除了目前要出的花色其餘刪除
            current = (current + num.index(max(num)))%4 if (current + num.index(max(num)))%4!=0 else 4 #判斷誰贏
        grade[current-1] += 1 #誰贏就+1分
    return grade

def output(grade, win, num): #輸出結果
    for i in grade: #player 1~4輸出分數
        print(i)
    if(num==1 or num==3): #看叫牌誰成局
        if(grade[0]+grade[2]>=win): #成局的那組需要大於等於最後叫牌的數字
            print('P1 P3')
        else:
            print('P2 P4')
    else:
        if(grade[1]+grade[3]>=win):
            print('P2 P4')
        else:
            print('P1 P3')
game()                                       