def main():
    try:
        x1, y1, x2, y2 = map(int, input().split())
        f1_m(x1, y1, x2, y2)
        f2(x1, y1, x2, y2)
    except ValueError:
        print('Error!')
def f1_m(x1, y1, x2, y2):
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
            
def check(m1, m2, b1, b2):
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

def f2(x1, y1, x2, y2):
    try:
        m1 = (y1-y2)
        m2 = (x1-x2)
        b1 = (x2*y1-x1*y2)
        b2 = (x2-x1)
        m1, m2, b1, b2 = check(m1, m2, b1, b2)
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
