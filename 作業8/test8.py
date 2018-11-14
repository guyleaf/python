import math
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    T, sign = TT(a, b, c)
    x11, x12, x21, x22 = compute(T, a, b, c, sign)
    output(sign, x11, x12, x21, x22)
def TT(a, b, c):
    a = b**2-4*a*c
    if(a>=0):
        T = math.sqrt(a)
        return T, 1
    else:
        T = math.sqrt(-a)
        return T, -1
	
def compute(T, a, b, c, sign):
        x11 = (-b)/(2*a)
        x12 = T/(2*a)
        x21 = (-b)/(2*a)
        x22 = T/(2*a)
        return x11, x12, x21, x22

def output(sign, x11, x12, x21, x22):
    if(sign>0):
        print('%.1f' %(x11+x12))
        print('%.1f' %(x21-x22))
    else:
        print("%.1f+%.1fi" %(x11, x12)) 
        print("%.1f-%.1fi" %(x21, x22))
main()