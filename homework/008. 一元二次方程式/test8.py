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