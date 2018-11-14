def output(t):
    if(t==1): 
        print('not triangle')
    elif(t==2):
        print('equilateral triangle')
    elif(t==3):
        print('isosceles triangle')
    else:
        print('triangle')
def gettriangle(a, b, c):
    if((a>0 and b>0 and c>0) and ((a+b)>c and (a+c)>b and (b+c)>a)):
        if(a==b==c):
            return 2
        elif((a==b and (a**2+b**2)>c**2) or (a==c and (a**2+c**2)>b**2) or (c==b and (c**2+b**2)>a**2)):
            return 3
        else:
            return 4
    else:
        return 1
def main():
    a, b, c = map(int,input().split())
    #b = str.split(a)
    t = gettriangle(a, b, c)
    output(t)
main()