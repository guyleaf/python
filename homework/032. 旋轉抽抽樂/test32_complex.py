"""
032. 旋轉抽抽樂
小明有個N*M(１≦N≦10,1≦M≦10) 的抽抽樂矩陣, 裡面放著1~9號等獎項,
小明在走樓梯的時候不小心手滑讓抽抽樂滾走，
抽抽樂有三種滾動方式:向右轉90度,向左轉90度,向右轉180度,
請幫助小明找出目前的獎項排列。

輸入說明:
3 3 (矩陣大小為3*3)(數字間有空格)
123 (輸入矩陣內的獎項)(數字之間沒有空格)(數字可重複)
321
456
12321322 (滾動方式 1=:向右轉90度 ,2=向左轉90度, 3=向右轉180度)
輸出說明:
輸出旋轉後的矩陣。(數字間沒有空格)
不合法的輸入則輸出E。
------------測資--------------
input:
3 4
1234
3216
1397
12321233
output:
131
322
913
764
--------------------------------
input
1 10
123456789
3321
output:
E
--------------------------------
input
1 10
1234567893
123321313
output:
1
2
3
4
5
6
7
8
9
3
"""

def data(row_num, column_num): #輸入 取行跟列
    row = []
    column = []
    for i in range(row_num):
        row.append(list(map(int, input())))
    for j in range(column_num):
        column.append([row[i][j] for i in range(row_num)])
    return row, column
        
    
def check(rank): #先去除旋轉可抵銷之代號
    for i in range(1, 3): #代號1~2
        if(rank.count(str(i))==4): #去除可旋轉360度之代號
            rank.replace(str(i), '', 4)
    rank = rank.replace('3', '', (rank.count('3')//2)*2)  #去除可旋轉360度之代號
    num = min(rank.count('1'), rank.count('2')) #右旋與左旋 取最小個數(也就是可抵銷之個數)
    rank = rank.replace('1', '', num) #去除
    rank = rank.replace('2', '', num) #去除
    return rank

def main(): #main
    row_num, column_num= map(int, input().split()) #輸入 取行跟列
    try:
        if(1<=row_num<=10 and 1<=column_num<=10): #檢查行跟列之數量
            row, column = data(row_num, column_num) #輸入 取行跟列
            rank = input() #旋轉順序
            rank = check(rank) #先去除旋轉可抵銷之代號
            new = rotate_shape(row, column, rank) #開始旋轉
            output(new) #輸出圖形
        else:
            print('E')
    except:
        print('E')

def rotate_shape(row, column, rank): #開始旋轉 一次算完
    new, row, column = rotate_1(row, column, rank) #向右旋轉
    new, row, column = rotate_2(new, row, column, rank) #向左旋轉
    new = rotate_3(new, row, column, rank) #旋轉180度
    return new
    
def rotate_1(row, column, rank): #向右旋轉
    new = [] #最終旋轉結果
    #先算1的個數來判斷怎麼直接旋轉
    if(rank.count('1')==3):
        new.extend(list(reversed(column)))
        row, column = reset(new)
    elif(rank.count('1')==2):
        new.extend(list(reversed(row)))
        for i in range(len(new)):
            new[i].reverse()
        row, column = reset(new)
    elif(rank.count('1')==1):
        new.extend(column)
        for i in range(len(new)):
            new[i].reverse()
        row, column = reset(new)
    return new, row, column

def rotate_2(new, row, column, rank): #向左旋轉
    #先算2的個數來判斷怎麼直接旋轉
    if(rank.count('2')==3):
        new = column
        for i in range(len(new)):
            new[i].reverse()
        row, column = reset(new)
    elif(rank.count('2')==2):
        new = list(reversed(row))
        for i in range(len(new)):
            new[i].reverse()
        row, column = reset(new)
    elif(rank.count('2')==1):
        new = list(reversed(column))
        row, column = reset(new)
    return new, row, column

def rotate_3(new, row, column, rank): #旋轉180度
    #先算3的個數來判斷怎麼直接旋轉
    if(len(new)==0): #如果1、2皆不需要旋轉 則預設 行儲存之圖形
        new.extend(row)
    if(rank.count('3')==1):
        new = list(reversed(row))
        for i in range(len(new)):
            new[i].reverse()
        row, column = reset(new)
    return new

def reset(new): #重新取 行and列
    row = []
    row.extend(new)
    column = []
    for j in range(len(row[0])):
        column.append([row[i][j] for i in range(len(row))])
    return row, column

def output(new): #輸出圖形
    for i in new:
        for j in i:
            print(j, end='')
        print()
main()