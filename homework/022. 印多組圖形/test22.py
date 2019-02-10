"""
022. 印多組圖形
輸入第一個整數，決定輸出圖形種類，
輸入第二個整數，決定輸出的行數。
..1
.121
12321
.121
..1
7531357
.53135
..313
...1

輸入說明：
每一組兩個數字，輸入-1結束所有輸入。
第一個正整數，1為菱形數字，2為三角形數字，其餘輸入均為不合法。
第二個正整數為行數 N， 第一種圖形合法輸入 N 為奇數，1<=N<=18，
第二種圖形合法輸入，1<=N<=5，其餘輸入均為不合法。
不合法輸入，則輸出 E。

輸出說明：
每個圖形之間需留空行
請參考範例輸出。

Sample Input1:
1 9
1 13
-1
Sample Output:
....1
...121
..12321
.1234321
123454321
.1234321
..12321
...121
....1
......1
.....121
....12321
...1234321
..123454321
.12345654321
1234567654321
.12345654321
..123454321
...1234321
....12321
.....121
......1

Sample Input2:
1 22
1 5
-1
Sample Output:
E
..1
.121
12321
.121
..1

Sample Input:
---------------
2 5
2 4
2 2
2 12
-1
Sample Output:
--------------
975313579
.7531357
..53135
...313
....1
7531357
.53135
..313
...1
313
.1
E
"""

def main():
    string = 0 #輸入暫存用
    switch = [] #記錄各組選擇圖形
    row = [] #記錄各組圖形行數
    choose = num = 0 #choose為選擇要印出的圖形 num為要輸出的行
    n = 0 #總共n組圖形
    while True:
        string = input()
        if(string == '-1'):
            break
        choose, num = map(int, string.split())
        switch.append(choose)
        row.append(num)
        n += 1

    for i in range(n): #0~n-1 
        identify = check(switch[i], row[i]) #檢查輸入規則
        if(identify and switch[i]==1): #選擇圖形1
            case1(row[i])
            print()
        elif(identify and switch[i]==2): #選擇圖形2
            case2(row[i])
            print()
        else: #皆輸入錯誤 輸出E
            print('E')
            print() #換行

def check(switch, row):
    if((switch!=1) and (switch!=2)): #圖形種類
        return 0
    elif((switch==1) and ((row<1 or row>18) or (row%2==0))): 
    #圖形1限定行數 1~18 並且為積數
        return 0
    elif((switch==2) and (row<1 or row>5)):
    #圖形2限定行數 1~5
        return 0
    return 1
    
def case1(n): #圖形1
    n = n // 2
    for i in range(n+1):
        case1_diaplaytop(n, i) #上
    for i in range(n):
        case1_displaydown(n, i) #下
        
def case2(n): #圖形2
    for i in range(n):
        case2_display(n, i)
        
def case1_diaplaytop(n, i):
    for j in range(n-i):
        print('.', end='')
    for j in range(i+1):
        print(j+1, end='')
    for j in range(i):
        print(i-j, end='')
    print() #換行
    
def case1_displaydown(n, i):
    for j in range(i+1):
        print('.', end='')
    for j in range(1, n-i+1):
        print(j, end='')
    for j in range(n-i-1, 0, -1):
        print(j, end='')
    print() #換行
    
def case2_display(n, i):
    for j in range(i):
        print('.', end='')
    for j in range(n-i, 0, -1):
        print(2*j-1, end='')
    for j in range(1, n-i):
        print(2*j+1, end='')
    print() #換行
main()