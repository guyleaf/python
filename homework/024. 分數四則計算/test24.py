"""
024. 分數四則計算
(若為 C 語言此題不使用陣列，必須使用指標)
此題自訂 add function，計算兩個分數相加。

function input
--------------------
n1: 第一個數的分子
d1: 第一個數的分母
n2: 第二個數的分子
d2: 第二個數的分母
function output
------------------------------
numerator: 相加結果的分子
deniminator: 相加結果的分母
此題自訂multiply function 定義，計算兩個分數相乘。

function input
--------------------
n1: 第一個數的分子
d1: 第一個數的分母
n2: 第二個數的分子
d2: 第二個數的分母
function output
------------------------------
numerator: 相乘結果的分子
deniminator: 相乘結果的分母
--------------------

輸入說明:
----------------------------
輸入二行，每一行代表一個分數
----------------
輸出說明:
---------------------------
輸出分數相加結果
輸出分數相減結果
輸出分數相乘結果
輸出分數相除結果
若有輸入分數的分母或分子為0，則輸出ERROR。
若分數大於1，則分數部分要加括號，如一又六分之一輸出為1(1/6)
若為負數，負號在最前面。
若輸出為0，則顯示0
輸出的結果必須化簡為最簡分數
----------------
Sample input:
----------------
1/2
2/3
----------------
Sample output:
----------------
1(1/6)
-1/6
1/3
3/4
----------------
Sample input:
----------------
0/2
2/3
----------------
Sample output:
----------------
ERROR
ERROR
ERROR
ERROR
"""

def main(): #分數四則運算(含輸入負數判斷)
    n1, d1 = map(int,input().split('/'))
    n2, d2 = map(int, input().split('/'))
    if not(n1 == 0 or n2 == 0 or d1 == 0 or d2==0): #檢查是否輸入皆不為零
        n1, d1, n2, d2 = check(n1, d1, n2, d2) #判斷負數 分母為負數皆移至分子
        numerator, deniminator = add_function(n1, d1, n2, d2) #加法
        output(numerator, deniminator) #輸出
        numerator, deniminator = substract_function(n1, d1, n2, d2) #減法
        output(numerator, deniminator) #輸出
        numerator, deniminator = multiply_function(n1, d1, n2, d2) #乘法
        output(numerator, deniminator) #輸出
        numerator, deniminator = divide_function(n1, d1, n2, d2) #除法
        output(numerator, deniminator) #輸出
    else:
        print('ERROR\nERROR\nERROR\nERROR')

def output(numerator, deniminator):
    space = 0 #儲存整數
    numerator, deniminator = simplify(numerator, deniminator) #分數化簡
    if(abs(numerator) % deniminator ==0): #整除
        print('%d' %(numerator // deniminator))
    elif(numerator < 0 and abs(numerator) > deniminator): #負的假分數
        space = abs(numerator) // deniminator
        numerator = abs(numerator) - (deniminator * space)
        print('-%d(%d/%d)' %(space, numerator, deniminator)) #輸出負的帶分數
    elif(numerator > deniminator): #正的假分數
        space = numerator // deniminator
        numerator -= (deniminator * space)
        print('%d(%d/%d)' %(space, numerator, deniminator)) #輸出正的帶分數
    else:
        print('%d/%d' %(numerator, deniminator)) #輸出真分數

def check(n1, d1, n2, d2): #判斷負數
    if(d1 < 0):
        d1 = abs(d1)
        n1 = n1 * -1
    if(d2 < 0):
        d2 = abs(d2)
        n2 = n2 * -1
    return n1, d1, n2, d2

def add_function(n1, d1, n2, d2): #加法
    numerator = 0
    deniminator = 0
    if(d1==d2):
        numerator = n1 + n2
        deniminator = d1
    else:
        deniminator = d1 * d2
        numerator = n1 * d2 + n2 * d1
    return numerator, deniminator

def substract_function(n1, d1, n2, d2): #減法
    numerator = 0
    deniminator = 0
    if(d1==d2):
        numerator = n1 - n2
        deniminator = d1
    else:
        deniminator = d1 * d2
        numerator = n1 * d2 - n2 * d1
    return numerator, deniminator

def multiply_function(n1, d1, n2, d2): #乘法
    numerator = 0
    deniminator = 0
    numerator = n1 * n2
    deniminator = d1 * d2
    return numerator, deniminator

def divide_function(n1, d1, n2, d2): #除法
    numerator = 0
    deniminator = 0
    numerator = n1 * d2
    deniminator = d1 * n2
    if(deniminator<0):
        numerator = numerator - numerator*2
        deniminator = abs(deniminator)
    return numerator, deniminator

def simplify(numerator, deniminator): #分數化簡
    result = 0
    if(numerator % deniminator ==0): #整除
        return numerator, deniminator
    factor = find_factor(numerator, deniminator) #找出最大公因數
    numerator //= factor
    deniminator //= factor
    return numerator, deniminator

def find_factor(numerator, deniminator): #輾轉相除法
    factor = 0
    numerator = abs(numerator)
    while(min(numerator, deniminator)!=0):
        if(numerator > deniminator):
            numerator %= deniminator
        elif(numerator < deniminator):
            deniminator %= numerator
    factor = max(numerator, deniminator)
    return factor
main()