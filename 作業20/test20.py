import math
def main():
    base, num = map(int, input().split())
    if(2<=base<=16 and 0<=num<=1000000000):
        convert_output(base, num)
    else:
        print('E')
def convert_output(base, num):
    list_base = []
    n = 0
    while num!=0 or n>0:
        if(num!=0):
            x = num % base
            x = hex(x).replace('0x','').upper()
            num = num // base
            n += 1
            list_base.append(x)
        else:
            n = output(n, list_base)
    print()
def output(n, list_base):
    n -= 1
    print('%s' %list_base[n], end='')
    return n
main()