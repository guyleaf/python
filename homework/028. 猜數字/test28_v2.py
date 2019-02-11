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

def generate(): #製造1000-9999之數字
    return [list(map(int, "{0:0>4d}".format(i))) for i in range(10000)]

def main():
    maybe = generate()
    while True:
        guess = input().split(",")
        maybe = compare(list(map(int, guess[0])), guess[1], maybe) #製造之數字與輸入比較 相同?A?B留下
        if(len(maybe)==1): #剩餘1之後就是答案
            print("".join(str(i) for i in maybe[0]))
            break

def compare(guess, num, maybe): #製造之數字與輸入比較 相同?A?B留下
    counter = 0
    for i in range(len(maybe)): 
        A = B = 0
        tmp = guess.copy()
        tmp_maybe = maybe[i-counter].copy()
        for j in range(4):
            if(tmp[j-A]==tmp_maybe[j-A]):
                tmp.pop(j-A)
                tmp_maybe.pop(j-A)
                A += 1
        for j in set(tmp): #拿輸入做成判斷B用之數字 set()去除重複
            if(tmp.count(j)>tmp_maybe.count(j)): #以製造之數字為主 取數量小的(避免重複算到)
                B += tmp_maybe.count(j)
            else:
                B += tmp.count(j)
        if("{0}A{1}B".format(A, B)!=num):
            maybe.pop(i-counter)
            counter += 1
    return maybe

main()