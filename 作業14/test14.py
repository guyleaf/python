import math
def main():
    hr = []
    min = []
    for i in range(6):
        a, b = map(int, input().split(":"))
        hr.append(a)
        min.append(b)
    check(hr, min)
def check(hr, min):
    c = []
    for i in range(0,6,2):
        if(hr[i]>=24 or hr[i]<0 or min[i]>=60 or min[i]<0):
            print('error')
        elif(hr[i+1]>=24 or hr[i+1]<0 or min[i+1]>=60 or min[i+1]<0):
            print('error')
        else:
            space = compute(hr, min, i)
            total = fee(space)
            output(total)
def compute(hr, min, i):
    a = (hr[i+1]*60+min[i+1])-(hr[i]*60+min[i])
    return a
def fee(space):
    quotient = space // 30
    remainder = space % 30
    if(quotient<4 or (quotient==4 and remainder==0)):
        a = quotient*30
    elif(quotient<8 or (quotient==8 and remainder==0)):
        a = (quotient-4)*40 + math.ceil(remainder / 30)*40 + 4*30
    else:
        a = (quotient-8)*60 + math.ceil(remainder / 30)*60 + 280
    return a
def output(total):
        print('%d' %total)	
main()