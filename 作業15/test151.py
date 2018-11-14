def main():
    num = int(input())
    result = display(num)
    output(result)
def display(num):
    a = ['', 'I', 'II', 'III']
    b = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    i = num//10
    j = num%5
    if(num%10==4):
        return b[i]+'IV'
    elif(num%10==9):
        return b[i]+'IX'
    elif(num%10>=5):
        return b[i]+'V'+a[j]
    else:
        return b[i]+a[j]
def output(result):
    print('%s' %result)
main()