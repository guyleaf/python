def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    x, y, z = compute(a, b, c, d, e)
    compare(x, y, z)
    
def compute(a, b, c, d, e):
    x = a*0.08+b*0.139+c*0.135+d*1.128+e*1.483
    y = a*0.07+b*0.130+c*0.121+d*1.128+e*1.483
    z = a*0.06+b*0.108+c*0.101+d*1.128+e*1.483
    return x, y, z
def compare(x, y, z):
    if(x<=183):
        print('%d' %183)
        print('183')
    elif(y<=383):
        if(x-183<=383 and (x-183)<=(z-983)):
            print('%d' %x)
            print('183')
        else:
            print('%d' %383)
            print('383')
    elif(z<=983):
        if((x-183)<=(y-383) and (x-183)<=983):
            print('%d' %x)
            print('183')
        elif((y-383)<=(x-183) and (y-383)<=983):
            print('%d' %y)
            print('383')
        else:
            print('%d' %983)
            print('983')
    elif((x-183)<=(y-383) and (x-183)<=(z-983)):
        print('%d' %x)
        print('183')
    elif((y-383)<=(x-183) and (y-383)<=(z-983)):
        print('%d' %y)
        print('383')
    else:
        print('%d' %z)
        print('983')
main()