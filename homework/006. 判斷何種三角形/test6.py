"""
006. 判斷何種三角形
當三個邊長能構成三角形時，再判斷該三角形是否為正三角形，若否，則判斷是否為等腰三角形：
1. 不能成為三角形：任兩邊和不大於第三邊，或任一邊長不大於0。
2. 正三角形：三個邊相等。
3. 等腰三角形：任兩邊相等，平方和大於第三邊的平方。
4. 一般三角形：非正三角形與等腰三角形。
此題必須寫一個運算的function
int getTriangle(int a, int b, int c);

輸入說明：
---------------
輸入三個整數邊長

輸出說明：
---------------
1. 不能成為三角形：輸出 not triangle。
2. 正三角形：輸出 equilateral triangle。
3. 等腰三角形：輸出 isosceles triangle。
4. 一般三角形：輸出 triangle。

測試案例(Test Case)資料：
Input：
4 1 1
Output：
not triangle
---------------
Input：
3 3 3
Output：
equilateral triangle
---------------
Input：
3 2 3
Output：
isosceles triangle
---------------
Input：
7 8 9
Output：
triangle
"""

def output(t): #輸出
    if(t==1): 
        print('not triangle')
    elif(t==2):
        print('equilateral triangle')
    elif(t==3):
        print('isosceles triangle')
    else:
        print('triangle')

def gettriangle(a, b, c): #判斷圖形
    if((a>0 and b>0 and c>0) and ((a+b)>c and (a+c)>b and (b+c)>a)):
        if(a==b==c):
            return 2
        elif((a==b and (a**2+b**2)>c**2) or (a==c and (a**2+c**2)>b**2) or (c==b and (c**2+b**2)>a**2)):
            return 3
        else:
            return 4
    else:
        return 1

def main(): #main
    a, b, c = map(int,input().split())
    t = gettriangle(a, b, c)
    output(t)
main()