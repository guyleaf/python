"""
034. 數獨
在9格寬×9格高的大九宮格中有9個3格寬×3格高的小九宮格
，每一列與每一行的數字均須包含 1～9，不能缺少，也不
能重複。每一小九宮格(3*3的九宮格)的數字均須包含 1～
9，不能缺少，也不能重複。
輸入一組測試資料為9x9的矩陣,判斷九宮格數字是不是一個
數獨的正解。

輸入說明 ：
輸入九列數據，每一列輸入為9個整數分別由空格分開。
輸出說明 ：
輸出Yes or No代表九宮格數字是不是一個數獨的正解。
----------------------
輸入範例
1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9 1
3 4 5 6 7 8 9 1 2
4 5 6 7 8 9 1 2 3
5 6 7 8 9 1 2 3 4
6 7 8 9 1 2 3 4 5
7 8 9 1 2 3 4 5 6
8 9 1 2 3 4 5 6 7
9 1 2 3 4 5 6 7 8
輸出範例
No
----------------------
輸入範例
1 9 3 2 6 5 4 7 8
7 8 2 3 1 4 9 5 6
4 5 6 9 7 8 1 3 2
2 3 4 8 5 1 6 9 7
9 6 5 4 3 7 2 8 1
8 7 1 6 9 2 3 4 5
3 1 9 5 8 6 7 2 4
5 2 7 1 4 3 8 6 9
6 4 8 7 2 9 5 1 3
輸出範例
Yes
"""

def input_function(): #輸入數獨圖形
    row = [] 
    for i in range(9):
        row.append(list(input().split(' ')))
    column = list(map(list, zip(*row)))
    return row, column

def check_big(row, column): #檢查整個數獨
    for i in range(9):
        for j in range(1, 10):
            if(row[i].count(str(j))!=1): #行
                return 0
            if(column[i].count(str(j))!=1): #列
                return 0
    return 1

def check_main(row, column): #檢查個別小九宮格數獨
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s_row = combination(row, column, i, j) #取小九宮格數獨
            if(not check_small(s_row)): #檢查重複
                return 0
    return 1

def check_small(s_row): #檢查個別小九宮格數獨
    for i in list(map(str, range(1, 10))): #產生1~9數字 拿來檢查有無重複
        if(s_row.count(i)>1): #如果數量>1 則錯誤
            return 0
    return 1

def combination(row, column, i, j): #取小九宮格數獨
    s_row = []
    for x in range(3):
        s_row.extend(row[i+x][j:j+3])
    return s_row

def main(): #main
    row, column = input_function() #輸入數獨圖形
    if(check_big(row, column)): #先檢查整個數獨
        if(check_main(row, column)): #檢查個別小九宮格數獨
            print('Yes')
        else:
            print('No')
    else:
        print('No')
main()