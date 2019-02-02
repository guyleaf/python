"""
002. 一元二次方程式
一元二次方程式，aX^2 + bx + c = 0，輸入a, b, c, 求 方程式的兩個實根。
---------------
輸入說明
第一個數(int) a
第二個數(int) b
第三個數(int) c
---------------
輸出說明
第一個實根 x1 = ((-b)+sqrt(b*b-4*a*c))/(2*a)
第二個實根 x2 = ((-b)-sqrt(b*b-4*a*c))/(2*a)
x1, x2 輸出到小數點第一位
print("%.1f" %x1);
---------------
Input
1
-2
1
Output
1.0
1.0
"""

import math
def getx(a, b, c): #求根
    x1 = ((-b) + (math.sqrt(b**2-4*a*c))) / (2*a)
    x2 = ((-b) - (math.sqrt(b**2-4*a*c))) / (2*a)
    return x1, x2
	
def main(): #main
    a = int(input())
    b = int(input())
    c = int(input())
    x1, x2 = getx(a, b, c)
    output(x1, x2)

def output(x1, x2): #輸出
    print('%.1f' %x1)
    print('%.1f' %x2)
	
main()