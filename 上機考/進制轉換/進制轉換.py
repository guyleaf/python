def main(): #進制轉換
    try:
        num = input().upper()
        base1 = int(input())
        base2 = int(input())
        if(check(num, base1, base2)):
            num = convert(num, base1, base2)
            output(num)
        else:
            print('E')
    except ValueError:
        print('E')

def check(num, base1, base2):
    if(base1<=1 or base2<=1 or not(num.isalnum())):
        return 0
    if(base1<=10 and '0'<=max(num)<str(base1)):
        return 1
    elif('0'<=max(num)<='9' or 'A'<=max(num)<chr(55+base1)):
        return 1
    return 0

def convert(num, base1, base2):
    result = []
    power = base2
    remainder = 0
    num = int(num, base1)
    while num!=0:
        remainder = num % base2
        if(remainder>=10):
            remainder = chr(55+remainder)
        num = num // base2
        result.append(remainder)
    result.reverse()
    return result

def output(num):
    for i in num:
        print(i, end='')
    print()
main()