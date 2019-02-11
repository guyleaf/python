"""
028. 猜數字
程式的使用者設定一個答案 X，四位數，0~9不重複。
程式的使用者輸入 4 位數字，以及這些 4 位數與答案 X 的相似程度。
程式必須根據相似程度資料，輸出使用者設定的答案 X。

相似程度的規則
(1) Yi 中有 1 位數字跟答案 X 一樣，且所在位置相同，例如千位對千位，或百位對百位，記為 1A。
若 2 位都有這情況，就是2A。
例如 X=1234，Y1=1856，兩者都有 1 ，位置都在千位，因此相似程度是 1A。
(2) Yi 中有 1 位數字跟答案 X 一樣，但所在位置不同，記為 1B。
若 2 位都有這情況，就是2B。
例如 X=1234，Y1=8561，兩者都有 1，但位置不同，所以是 1B。
(3) 以上兩條規則以 (1)優先，之後再考慮 (2)。
(4) 輸入至猜出答案為止

----------------------------------------------------------------------------------

輸入範例說明:
每一行輸入 4 位數字 Yi，以及相似程度 ?A?B。
假設使用者設定的答案是 4237
輸入
1968,0A0B 數字都沒有對，所以相似程度為 0A0B。
7052,0A2B 有 2 個數字對 (7, 2) ，但位置不對，相似程度為 0A2B。
2347,1A3B 有 1 個數字對且位置對 (7)， 3 個數字對 (2, 3, 4)，相似程度為1A3B。
3427,1A3B 有 1 個數字對且位置對 (7)， 3 個數字對 (3, 4, 2)，相似程度為1A3B。
2473,0A4B 4 個數字對，位置不對。
輸出範例說明:
4237 輸出使用者設定的答案

Sample Input
1968,0A0B
7052,0A2B
2347,1A3B
3427,1A3B
2473,0A4B
Sample Output
4237
"""

def create(): #製造1000-9999之數字
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    A = []
    B = []
    #A = [i for i in range(0, 10000) if Filter(i)]
    for i in range(10000):
        x1 = i%10
        x2 = (i%100 - x1)//10
        x3 = (i%1000 - x1)//100
        x4 = (i%10000 - x1)//1000
        if x4!=x3 and x4!=x2 and x4!=x1 and x3!=x2 and x3!=x1 and x2!=x1:
            B.append([x4, x3, x2, x1])
    return B

def identify(num, guess, result): #製造之數字與輸入比較 相同?A?B留下
    new = []
    count = 0
    for i in range(len(result)):
        A = 0
        B = 0
        copy_num = []
        copy_list = []
        copy_num.extend(num)
        copy_list.extend(result[i])
        for j in range(4):
            if(result[i][j]==num[j]):
                copy_list.pop(j-A)
                copy_num.pop(j-A)
                A +=1
        for x in copy_num:
            if(copy_list.count(x)>0):
                B +=1
        del copy_list, copy_num
        if(guess[0]!=str(A) or guess[2]!=str(B)):
            new.append(i)
    for i in new:
        result.pop(i-count)
        count += 1
    return result

def main():
    group = [] 
    result = create()
    for i in range(5):
        num, guess = input().split(',') #數字與?A?B
        if('4A0B' in guess):  #判斷是否有4A0B 直接輸出答案
            for j in num:
                print(j, end='')
            print()
            break
        num = list(map(int, num))
        result = identify(num, guess, result) #製造之數字與輸入比較 相同?A?B留下
        if(len(result)==1):
            for j in result[0]:
                print(j, end='')
            print()
            break
main()