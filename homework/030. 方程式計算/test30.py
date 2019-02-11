"""
030. 方程式計算
寫一個 function 輸入 XY 座標系統的兩個座標 (x1, y1), (x2, y2)；
輸出兩個座標經過的 XY 方程式 y=mx+b;
m=(y1-y2)/(x1-x2)
b=(x2y1-x1y2)/(x2-x1)
void f1_m(int x1, int y1, int x2, int y2, double m, double b);

寫一個 function 輸入 XY 座標系統的兩個座標 (x1, y1), (x2, y2)；
輸出兩個座標經過的 XY 方程式 y=m1/m2x+b1/b2;
m1=(y1-y2), m2=(x1-x2),
b1=(x2y1-x1y2), b2=(x2-x1),
void f2(int x1, int y1, int x2, int y2, int m1, int m2, int b1, int b2);
-------------
輸入說明:
XY的兩個座標 x1, y1, x2, y2，均為整數。
輸出說明:
(1) y=mx+b,
m, b 計算至小數第二位。
(2) y=mx+b
m, b 以分數表達，分數不需要化簡。
=>方程式有可能沒有 x 項，或沒有 y 項。
=>沒有 x 項則 y=b，沒有 y 項則 x = -b/m。
=>若m,b為整數，則使用整數表達。
不合法的輸入則輸出Error!
-------------
輸入範例:
3 4 -3 0
輸出範例:
y=0.67x+2
y=4/6x+2
-------------
輸入範例:
3.3 4 -3 0
輸出範例:
Error!
-------------
輸入範例:
1 0 0 1
輸出範例:
y=-x+1
y=-x+1
"""

def main():
    try: #例外處理 輸入不是數字的情況
        x1, y1, x2, y2 = map(int, input().split())
        f1_m(x1, y1, x2, y2)
        f2(x1, y1, x2, y2)
    except ValueError:
        print('Error!')
        
def f1_m(x1, y1, x2, y2): #m, b 計算至小數第二位
    try:
        m = (y1-y2)/(x1-x2)
        b = (x2*y1-x1*y2)/(x2-x1)
        if(m==0 and abs(x2*y1-x1*y2)%abs(x2-x1)==0):
            print('y=%d' %b)
        elif(m==0):
            print('y=%.2f' %b)
        elif((y1-y2)/(x1-x2)==-1 and abs(x2*y1-x1*y2)%abs(x2-x1)==0):
            print('y=-x%+d' %(b))
        elif((y1-y2)/(x1-x2)==-1):
            print('y=-x%+.2f' %(b))
        elif(abs(y1-y2)%abs(x1-x2)==0 and abs(x2*y1-x1*y2)%abs(x2-x1)==0):
            print('y=%dx%+d' %(m, b))
        elif((y1-y2)%(x1-x2)==0):
            print('y=%dx%+.2f' %(m, b))
        elif(abs(x2*y1-x1*y2)%abs(x2-x1)==0):
            print('y=%.2fx%+d' %(m, b))
        else:
            print('y=%.2fx%+.2f' %(m, b))
    except ZeroDivisionError:
            print('x=%d' %x1)
            
def check(m1, m2, b1, b2): #判斷負數 一律放至分子
    if(b1>0 and b2<0):
        b1 = -1 * b1
        b2 = abs(b2)
    elif(b1<0 and b2<0):
        b1 = abs(b1)
        b2 = abs(b2)
    if(m1>0 and m2<0):
        m1 = -1 * m1
        m2 = abs(m2)
    elif(m1<0 and m2<0):
        m1 = abs(m1)
        m2 = abs(m2)
    return m1, m2, b1, b2

def f2(x1, y1, x2, y2): #m, b 以分數表達，分數不需要化簡
    try:
        m1 = (y1-y2)
        m2 = (x1-x2)
        b1 = (x2*y1-x1*y2)
        b2 = (x2-x1)
        m1, m2, b1, b2 = check(m1, m2, b1, b2) #判斷負數 一律放至分子
        if((m1/m2)==0 and abs(b1)%abs(b2)==0):
            print('y=%d' %(b1/b2))
        elif((m1/m2)==0):
            print('y=%d/%d' %(b1, b2))
        elif(m1/m2==-1 and abs(b1)%abs(b2)==0):
            print('y=-x%+d' %(b1/b2))
        elif(m1/m2==-1):
            print('y=-x%+d/%d' %(b1, b2))
        elif(abs(m1)%abs(m2)==0 and abs(b1)%abs(b2)==0):
            print('y=%dx%+d' %(m1/m2, b1/b2))
        elif((y1-y2)%(x1-x2)==0):
            print('y=%dx%+d/%d' %(m1/m2, b1, b2))
        elif(abs(x2*y1-x1*y2)%abs(x2-x1)==0):
            print('y=%d/%dx%+d' %(m1, m2, b1/b2))
        else:
            print('y=%d/%dx%+d/%d' %(m1, m2, b1, b2))
    except ZeroDivisionError:
            print('x=%d' %x1)
main()
