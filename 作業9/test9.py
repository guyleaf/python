def main():
    x = int(input())
    y = int(input())
    z = int(input())
    sum = compute(x, y, z)
    print('%d' %sum)
def compute(x, y, z):
    if(x<=10):
        a = 380*x
    elif(x<=20):
        a = 380*x*0.9
    elif(x<=30):
        a = 380*x*0.85
    else:
        a = 380*x*0.8

    if(y<=10):
        b = 1200*y
    elif(y<=20):
        b = 1200*y*0.95
    elif(y<=30):
        b = 1200*y*0.85
    else:
        b = 1200*y*0.8

    if(z<=10):
        c = 180*z
    elif(z<=20):
        c = 180*z*0.85
    elif(z<=30):
        c = 180*z*0.8
    else:
        c = 180*z*0.7
    return a+b+c
main()