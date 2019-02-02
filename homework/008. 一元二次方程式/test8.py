"""
008. 一元二次方程式
一元二次方程式，aX^2 + bx + c = 0，輸入a, b, c, 求 方程式的兩個實/虛根。
T = sqrt(b*b-4*a*c)
第一個根， x1 = (-b+T)/(2*a)
第二個根， x2 = (-b-T)/(2*a)
#若為 C 語言，本題須 #include < math.h >

---------------
輸入說明：
第一個數 a
第二個數 b
第三個數 c

---------------
輸出說明：
當 T>=0
輸出x1, x2為實根，輸出到小數點第一位 print("%.1f" %x1);

當 T<0
輸出x1 , x2為虛根，輸出到小數點第一位
print("%.1f+%.1fi" %(x11, x12))
print("%.1f-%.1fi" %(x21, x22))

若x11或x21為0.0時，不須輸出正負號

測試案例(Test Case)資料：
Input：
1
-2
1
Output：
1.0
1.0
---------------
Input：
1
2
2
Output：
-1.0+1.0i
-1.0-1.0i
"""

import math
def main(): #main
    a = int(input())
    b = int(input())
    c = int(input())
    T, sign = TT(a, b, c)
    x11, x12, x21, x22 = compute(T, a, b, c, sign)
    output(sign, x11, x12, x21, x22)

def T(a, b, c): #求判別式
    a = b**2-4*a*c
    if(a>=0):
        T = math.sqrt(a)
        return T, 1 #T, 正數or負數
    else:
        T = math.sqrt(-a)
        return T, -1
	
def compute(T, a, b, c, sign): #求出根
    x11 = (-b)/(2*a)
    x12 = T/(2*a)
    x21 = (-b)/(2*a)
    x22 = T/(2*a)
    return x11, x12, x21, x22

def output(sign, x11, x12, x21, x22): #輸出
    if(sign>0):
        print('%.1f' %(x11+x12))
        print('%.1f' %(x21-x22))
    else:
        print("%.1f+%.1fi" %(x11, x12)) 
        print("%.1f-%.1fi" %(x21, x22))
main()