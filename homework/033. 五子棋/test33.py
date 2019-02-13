"""
033. 五子棋
檢查10*10五子棋可以構成5個連為一線的位置。
1表示有放棋子，0表示沒有放旗子。
----------------------------------
輸入說明
輸入10*10的資料
-----------------------------
輸出說明
可構成5個連為一線的位置。例如
0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 1 1 1 1
0 0 0 0 1 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 0 0 1 0 0 0 0 0 0
可以增加5個連為一線，以下圖表示。
0 0 0 0 0 0 x 0 1 0
0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 x 1 1 1 1
0 0 0 0 1 0 1 0 0 0
0 0 0 x 0 0 x 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 x 1 1 1 1 x 0 0 0
0 0 0 1 0 0 0 0 0 0
其位置為
0 6
3 5
5 3
5 6
8 1
8 6
---------------------
SampleInput:
0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 1 1 1 1
0 0 0 0 1 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 0 0 1 0 0 0 0 0 0
Sample Output:
0 6
3 5
5 3
5 6
8 1
"""

def input_function(): #輸入
    row = []
    column = []
    for i in range(10):
        row.append(list(input().split(' '))) #取行
    column = list(map(list, zip(*row))) #取列
    slash_left = []
    slash_right = []
    for x in range(0,6):#取左斜數值
        slash_left.append([row[i][j] for i, j in zip(range(x, 10), range(10))])
    for x in range(1,6):#取左斜數值
        slash_left.append([column[i][j] for i, j in zip(range(x, 10), range(10))])
    for x in range(0,6):#取右斜數值
        slash_right.append([row[i][9-j] for i, j in zip(range(x, 10), range(10))])
    for x in range(1,6):#取右斜數值
        slash_right.append([column[9-i][j] for i, j in zip(range(x, 10), range(10))])
    return row, column, slash_left, slash_right

def find_x(row, column, slash_left, slash_right): #找出可連成一條線之空格
    column_new = []
    row_new = []
    slash_new = []
    for i in range(10): #第0~9行
        row_new = find_row(row, i, row_new) #行
        column_new = find_column(column, i, column_new) #列
        slash_new = find_slash_right(slash_right, i, slash_new) #右斜
        slash_new = find_slash_left(slash_left, i, slash_new) #左斜
    slash_new = find_slash_right(slash_right, 10, slash_new)
    slash_new = find_slash_left(slash_left, 10, slash_new)
    return row_new, column_new, slash_new

def find_row(row, i, row_new): #找出行能連成一條線之空格
    if(row[i].count('1')<4): #如果第i行的1不超過4 直接跳過
        return row_new
    for j in range(6): #5個為一組 總共5組
        if(row[i][j:j+5].count('1')==4): #當前組別之中有4個1 則找出其中為0之空格
            row_new.append((i, row[i][j:j+5].index('0')+j)) #紀錄
    return row_new

def find_column(column, i, column_new): #找出列能連成一條線之空格
    if(column[i].count('1')<4):
        return column_new
    for j in range(6):
        if(column[i][j:j+5].count('1')==4):
            column_new.append((column[i][j:j+5].index('0')+j, i))
    return column_new

def find_slash_right(slash_right, i, slash_new): #找出右斜能連成一條線之空格
    if(slash_right[i].count('1')<4):
        return slash_new
    for j in range(len(slash_right[i])-4): #一樣5個為一組 總共len(slash_right[i])-4組 j指初始index
        if(slash_right[i][j:j+5].count('1')!=4): #先去除不足4個1或超過4個1
            continue
#--------------以下都是組別已有4個1--------------------
        elif(i>=6):
            x = slash_right[i][j:j+5].index('0')+j #空格index(5個一組)+j(目前第幾個index)
            slash_new.append((x, 9-(x+i%5)))
        else:
            x = slash_right[i][j:j+5].index('0')+j
            slash_new.append((x+i, 9-x))
    return slash_new

def find_slash_left(slash_left, i, slash_new): #找出左斜能連成一條線之空格
    if(slash_left[i].count('1')<4): 
        return slash_new
    for j in range(len(slash_left[i])-4): #一樣5個為一組 總共len(slash_right[i])-4組
        if(slash_left[i][j:j+5].count('1')!=4): #先去除不足4個1或超過4個1
            continue
#--------------以下都是組別已有4個1--------------------
        elif(i>=6):
            x = slash_left[i][j:j+5].index('0')+j #空格index(5個一組)+j(目前第幾個index)
            slash_new.append((x, x+i%5))
        else:
            x = slash_left[i][j:j+5].index('0')+j
            slash_new.append((x+i, x))
    return slash_new

def check(row_new, column_new, slash_new): #去除重複之座標
    new = []
    new = list(set(row_new) | set(column_new) | set(slash_new))
    new.sort()
    return new

def output(new): #輸出
    for i in new:
        for j in i:
            print(j, end=' ')
        print()
        
def main(): #main
    row, column, slash_left, slash_right = input_function() #輸入
    row_new, column_new, slash_new = find_x(row, column, slash_left, slash_right) #找出可連成一條線之空格
    new = check(row_new, column_new, slash_new) #去除重複之座標
    output(new) #輸出

main()