"""
015. 印圖形
請使用 while loop或for loop，
請使用 function。
第一個輸入意義為選擇三種圖形:
1 三角形方尖方面向右邊
2 三角形方尖方面向左邊
3 菱形
第二個輸入意義為畫幾行
(奇數，範圍為 3,5,7,9,....,21)

input
1 (第一種圖形，三角形尖方面向右邊)
9 (共 9 行)
--------------------------
output
*
**
***
****
*****
****
***
**
*
---------------------------
input
2 (第二種圖形，三角形尖方面向左邊)
5 (共 5 行)
---------------------------
output
..*
.**
***
.**
..*
--------------------------
input
3 (第三種圖形: 菱形 )
3 (共 3 行數)
輸出
.*
***
.*
"""

def main(): #main
    switch = int(input()) #選擇要印出的圖形
    num = int(input()) #num行
    if(switch==1):
        right(num) #尖端往右
    elif(switch==2):
        left(num) #尖端往左
    else:
        rhombus(num) #菱形

def right(num): #尖端往右
    n = num//2
    for i in range(n+1): #上半部
        for j in range(i+1):
            print('*',end="")
        print()
    for i in range(n): #下半部
        for j in range(n-i):
            print('*',end="")
        print()

def left(num): #尖端往左
    n = num//2
    for i in range(n+1): #上半部
        for j in range(n-i):
            print('.',end="")
        for j in range(i+1):
            print('*',end="")
        print()
    for i in range(n): #下半部
        for j in range(i+1):
            print('.',end="")
        for j in range(n-i):
            print('*',end="")
        print()

def rhombus(num): #菱形
    n = num//2
    for i in range(n+1): #上半部
        for j in range(n-i):
            print('.',end="")
        for j in range(i+1):
            print('*',end="")
        for j in range(i):
            print('*',end="")
        print()
    for i in range(n): #下半部
        for j in range(i+1):
            print('.',end="")
        for j in range(n-i):
            print('*',end="")
        for j in range(n-i-1):
            print('*',end="")
        print()
main()