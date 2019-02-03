"""
020. 十進制轉換
(若為 C 語言，請使用一個 loop 和 function call)
給予一個十進位整數，請撰寫一程式可以將此十進位整數轉換為指定的進制的整數。

輸入說明:
輸入分為兩部份，包括指定的進制數
(2 ~ 16)
與十進位整數(0 ~ 1000000000)
輸出說明:
經轉換後的新進位制的整數( y )
不合法的輸入則輸出E

input:
16 1234
output:
4D2
----------------------
Input:
8 56456456
Output:
327272410
-----------------------
Input:
11 17489465
Output:
9966104
-----------------------
Input:
4 17489
Output:
10101101
"""

import math
def main(): #main
    try:
        base, num = map(int, input().split()) #輸入進制, 十進制數值
        if(2<=base<=16 and 0<=num<=1000000000): #檢查進制數值
            convert_output(base, num)
        else:
            print('E')
    except:
        print('E')
        
def convert_output(base, num): #轉換
    list_base = []
    n = 0
    while num!=0 or n>0:
        if(num!=0): #檢查是否轉換完成
            x = num % base #取餘數
            x = hex(x).replace('0x','').upper() #轉換成16進制並大寫並把0x去除
            num = num // base #取商數
            n += 1 #有幾位數
            list_base.append(x)
        else:
            n = output(n, list_base) 
    print()
    
def output(n, list_base): #輸出
    n -= 1
    print('%s' %list_base[n], end='')
    return n
    
main()