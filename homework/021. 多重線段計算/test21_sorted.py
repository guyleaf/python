"""
021. 多重線段
請使用一個 while loop 和 function call
C 語言此題不使用陣列。
Python 此題不使用 List。
給定一些線段，求這些線段所覆蓋的長度，注意，重疊的部分只能算一次。

輸入說明 ：
第一列有一個正整數 n:
代表共有 n 組測試案例。
接下來每一組測試案例的第一列是一個整數 m
表示此測試案例有m個線段，
接著的m列每一列是一個線段的兩端點，
每一個端點是一個整數介於0~60000之間，
端點之間以一個空格區隔，線段個數不超過 5000。

-----------------------------
輸出說明 ：
針對每一組測試案例，輸出其覆蓋的長度，每組測試案例輸出一列。
不合法的輸入則輸出E

Input:
2 (共有2組次是案例)
2 (此組測試案例有2個線段)
0 1
2 3
3 (此組測試案例有3個線段)
0 20
10 30
40 50
Output:
2
40
-------------
Input:
3
3
10 111
150 3450
160 180
2
100 180
150 3333
1
150 150
Output:
3401
3233
0
--------------
Input:
1
2
150 320
160 190
Output:
170
"""
def main():
    group = [] #紀錄輸入[[第一組], [第二組]...]
    result = [] #記錄各組線段計算總長度
    addnum = []  #紀錄各組num個線段
    i = 0
    n = int(input()) #n組線段
    if(n<0):
        print('E')
        return
        
    while(i<n): #第i組線段 0~n-1
        num = int(input()) #num個線段
        group.append([num]) #加到group(two dimension)
        group[i].extend(ip(num)) #加入該組線段範圍
        addnum.append(num)
        total = compute(group[i]) #計算該組總長度
        result.append(total)
        i += 1
    
    for i in range(n):
        checknum = check(group[i], addnum[i]) #檢查該組是否符合規則
        if(checknum==-1):
            print('E')
        elif(checknum==1):
            print('%d' %result[i])

def ip(num): #輸入線段範圍
    register = [] #暫存用
    counter = 0
    for i in range(num): #num個線段
        register.append(list(map(int, input().split()))) #輸入線段範圍
    register = sorted(register) #sort可去除計算totalleft，只計算totalright(因為線段預設長度以第一個線段為準)
    for i in range(num): #two dimension -> one dimension
        register.extend(register[i-counter])
        register.pop(i-counter)
        counter +=1
    return register #one dimension

def check(group, num): #檢查該組是否符合規則
    if not(len(group)== num*2+1): #檢查總長度
        return -1
    elif(group[0]<0 or group[0]>5000): #檢查該組輸入線段個數
        return -1
    for i in range(1, len(group)-1, 2):
        if((group[i]>group[i+1]) or group[i]<0 or group[i+1]<0 or group[i]>60000 or group[i+1]>60000): #檢查線段範圍
            return -1
    return 1

def compute(group): #計算總長度
    total = group[2] - group[1] #預設總長度=第一個線段
    for i in range(3, len(group)-1, 2): #從第二個線段開始
        total += compare(group, i) 
    return total

def compare(group, i):
    totalright = 0
    for j in range(1, i, 2): #index=0是線段個數
        #與i前面的線段比較，如果第i個線段head和線段tail(i+1)都在i前面的線段之間，則回傳0，已經被覆蓋到，不用多計算
        if((group[i]>=group[j]) and (group[i]<=group[j+1]) and (group[i+1]<=group[j+1])): 
            return 0
    for j in range(1, i, 2):
        #判斷第i個線段head有小於第j個線段tail(大於則直接皆無覆蓋到i) 以及 第i個線段tail要大於第j個線段tail
        if((group[i]<group[j+1]) and (group[i+1]>group[j+1])):
            totalright = group[i+1] - group[j+1]
            #第i個線段head-第j個線段head 
            #(只需計算最後一個成立的就可，因為前面線段也會覆蓋到其他前面線段，類似標記的動作)
            #     -----__
            #   ---------__
            # -------------       (_為totalrigjt)
    if(totalright==0): #如果第i個線段皆無覆蓋到i前面的線段，則長度為第i個線段本身長度
        total = group[i+1] - group[i]
        return total
    return totalright
main()