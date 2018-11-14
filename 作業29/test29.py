from math import ceil, floor
def main():
    num = float(input())
    if(num<0 and floor(num)==ceil(num)):
        num = int(num) * -11
        print('%d' %search(num))
    elif(num<0):
        num, fraction = map(int, str(num).split('.'))
        print('%d' %search(fraction))
    elif(int(num)==0 or int(num)==1):
        print('%d' %search(1000))
    elif(2<=int(num)<=1000):
        print('%d' %search(int(num)))
    else:
        print('Error!')

def search(num):
    for i in range(num, 0, -1):
        for j in range(2, num//2+1):
            if(i%j==0):
                i = 0
                break
        if(i!=0):
            return i
main()