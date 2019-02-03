"""
012. 線段計算
請算出a,b,c三條線在X軸上所涵蓋的長度(不含重複線段)
例如:a(x1,x2)表示a線段為X軸上點x1到點x2的線

輸入說明:
---------------
-1 (a的x1座標為 -1)
1 (a的x2座標為 1)
0 (b的x1座標為 0)
2 (b的x2座標為 2)
1 (c的x1座標為 1)
3 (c的x2座標為 3)
https://i.imgur.com/3RWOXvp.png

輸出說明:
---------------
4
"""

def main(): #main
    ax1 = int(input()) #線段a
    ax2 = int(input())
    bx1 = int(input()) #線段b
    bx2 = int(input())
    cx1 = int(input()) #線段c
    cx2 = int(input())
    sum = compute(ax1, ax2, bx1, bx2, cx1, cx2)
    space = compare(ax1, ax2, bx1, bx2, cx1, cx2)
    output(sum, space)

def compute(ax1, ax2, bx1, bx2, cx1, cx2):
    sum = (ax2-ax1)+(bx2-bx1)+(cx2-cx1) #計算線段總和
    return sum

def compare(ax1, ax2, bx1, bx2, cx1, cx2): #檢查有無重疊
    space1 = 0
    space2 = 0
    space3 = 0
    space4 = 0
    sign1 = 0
    sign2 = 0
    sign3 = 0
    sign4 = 0

    for j in range(ax1, ax2+1):
        #線段a-線段b
        if(j==bx1):
            sign1 = 1
        if(j==bx2 and sign1==1):
            space1 = bx2 - bx1
            sign1 = 0
        #線段a-線段c
        if(j==cx1):
            sign2 = 1
        if(j==cx2 and sign2==1):
            space2 = cx2 - cx1
            sign2 = 0
    if(sign1==1):
        space1= ax2 - bx1
    if(sign2==1):
        space2= ax2 - cx1
        sign3 = 1
	
    for j in range(bx1, bx2+1):
        #線段a-其他
        if(sign3==1 and j==cx2):
            space3 = cx2 - ax2
            sign3 = 0
        elif(sign3==1):
            space3 = bx2 - ax2
        #線段b-線段c
        if(sign2==0 and j==cx1):
            sign4 = 1
        if(j==cx2):
            space4 = cx2 - cx1
            sign4 = 0
    if(sign4==1):
        space4= bx2 - cx1
    return space1+space2+space3+space4

def output(sum, space): #輸出
    print('%d' %(sum-space))
main()