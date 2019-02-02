"""
007. 求平均數、變異數以及標準差
請輸入五個數字，分別計算出平均數、變異數、標準差，
並精確到小數點後第二位(註，之後的小數捨去)。

變異數參考公式：
Σ(Xi-μ)^2/N
標準差參考公式：
(Σ(Xi-μ)^2/N)^(0.5)
平均數參考公式：
μ=Σ(Xi)/N

例如：1 2 8 9 10
變異數：14.00
> Σ(Xi-μ)^2=(1-6)^2+(2-6)^2+(8-6)^2+(9-6)^2+(10-6)^2
=25+16+4+9+16=70
700./5.0=14.00
標準差：3.74
> 14^(0.5) = 3.74165
取兩位小數 = 3.74
平均值：6.00
> (1+2+8+9+10)/5.0 = 6.00

輸入說明：
---------------
輸入五個整數
輸出說明：
---------------
變異數
標準差
平均值
輸出到小數點第二位 print("%.2f" %x);

測試案例(Test Case)資料：
Input：
1 2 8 9 10
Output：
14.00
3.74
6.00
"""

import math
def main(): #main
    data = input().split()
    avg = average(data)
    var = variance(avg, data)
    st = standard(var)
    output(var, st, avg)

def output(var, st, avg):
    print('%.2f' %var) #標準差
    print('%.2f' %st) #變異數
    print('%.2f' %avg) #平均數

def average(data): #平均數
    avg = (int(data[0])+int(data[1])+int(data[2])+int(data[3])+int(data[4]))/5
    return avg

def variance(avg, data): #變異數
    var = (int(data[0])-avg)**2+(int(data[1])-avg)**2+(int(data[2])-avg)**2+(int(data[3])-avg)**2+(int(data[4])-avg)**2
    return var/5

def standard(var): #標準差
    st = math.sqrt(var)
    return st
main()