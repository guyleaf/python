"""
018. 階層與質因數
求階層(N!)值總和，0< N < 1000

輸入說明:
輸入一個整數N
------------------
輸出說明:
依序每一行輸出小於 N 的質因數，以及其階層值，以逗號隔開。
最後一行是所有階層值總和。
輸入錯誤，包括小數點、負數、字元或其他不合法的輸入，
輸出 E。
------------------

input :
10
output:
2,2
5,120
122
-----------------
input :
12
output:
2,2
3,6
8
-----------------
input :
30
output:
2,2
3,6
5,120
128
-----------------
input :
-1
output:
E
------------------
input
10.2
output:
E
------------------
input
a.2
output:
E
------------------
input
11.a2
output:
E
"""

import math
def main(): #main
    num = input() #輸入正整數
    if(num.isdecimal() and num!='1'): #檢查是否正整數(除了1)
        prime_factor = findprime_factor(int(num))
        level_output(prime_factor)
    else:
        print('E')

def findprime_factor(num): #找出質因數
    prime_factor = [] #質因數
    if(num%2==0): #檢查有無2為質因數
        prime_factor.append(2)
    for i in range(3,num+1): #3~num 階層
        for j in range(2,i): #2~i 因數迴圈
            if(i % j==0): #階層內判斷是否為質數
                sign = 1
                break
            else:
                sign = 0
        if(sign==0 and num%i==0): #判斷是否為質因數
            prime_factor.append(i)
    return prime_factor
    
def level_output(prime_factor): #階層輸出
    total = 0
    for i in prime_factor:
        total += math.factorial(i) #factorial計算階層值並總和
        print('%d,%d' %(i, math.factorial(i)))
    print(total)
    
main()