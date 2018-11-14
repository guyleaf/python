def main(): #分數四則運算(含輸入負數判斷)
    n1, d1 = map(int, input().split('/'))
    n2, d2 = map(int, input().split('/'))
    if not(n1 == 0 or n2 == 0 or d1 == 0 or d2==0):
        n1, d1, n2, d2 = check(n1, d1, n2, d2)
        numerator, deniminator = add_function(n1, d1, n2, d2)
        output(numerator, deniminator)
        numerator, deniminator = substract_function(n1, d1, n2, d2)
        output(numerator, deniminator)
        numerator, deniminator = multiply_function(n1, d1, n2, d2)
        output(numerator, deniminator)
        numerator, deniminator = divide_function(n1, d1, n2, d2)
        output(numerator, deniminator)
    else:
        print('ERROR\nERROR\nERROR\nERROR')

def output(numerator, deniminator):
    space = 0                                                                #儲存代分數整數
    numerator, deniminator = simplify(numerator, deniminator)                #分數化簡
    if(abs(numerator) % deniminator ==0):                                    #整數
        print('%d' %(numerator // deniminator))

    elif(numerator < 0 and abs(numerator) > deniminator):                    #負數假分數
        space = abs(numerator) // deniminator
        numerator = abs(numerator) - (deniminator * space)
        print('-%d(%d/%d)' %(space, numerator, deniminator))

    elif(numerator > deniminator):                                           #正數假分數
        space = numerator // deniminator
        numerator -= (deniminator * space)
        print('%d(%d/%d)' %(space, numerator, deniminator))

    else:
        print('%d/%d' %(numerator, deniminator))

def check(n1, d1, n2, d2):                                                   #判斷輸入正負
    if(n1 < 0 and d1 < 0): #
        n1 = abs(n1)
        d1 = abs(d1)
    elif(d1 < 0):
        d1 = abs(d1)
        n1 = n1 - n1*2
    if(n2 < 0 and d2 < 0):
        n2 = abs(n2)
        d2 = abs(d2)
    elif(d2 < 0):
        d2 = abs(d2)
        n2 = n2 - n2*2
    return n1, d1, n2, d2

def add_function(n1, d1, n2, d2):
    numerator = 0
    deniminator = 0
    if(d1==d2):
        numerator = n1 + n2
        deniminator = d1
    else:
        deniminator = d1 * d2
        numerator = n1 * d2 + n2 * d1
    return numerator, deniminator

def substract_function(n1, d1, n2, d2):
    numerator = 0
    deniminator = 0
    if(d1==d2):
        numerator = n1 - n2
        deniminator = d1
    else:
        deniminator = d1 * d2
        numerator = n1 * d2 - n2 * d1
    return numerator, deniminator

def multiply_function(n1, d1, n2, d2):
    numerator = 0
    deniminator = 0
    numerator = n1 * n2
    deniminator = d1 * d2
    return numerator, deniminator

def divide_function(n1, d1, n2, d2):
    numerator = 0
    deniminator = 0
    numerator = n1 * d2
    deniminator = d1 * n2
    if(deniminator<0):
        numerator = numerator - numerator*2
        deniminator = abs(deniminator)
    return numerator, deniminator

def simplify(numerator, deniminator):
    result = 0
    if(numerator % deniminator ==0):
        return numerator, deniminator
    factor = find_factor(numerator, deniminator)
    numerator //= factor
    deniminator //= factor
    return numerator, deniminator

def find_factor(numerator, deniminator):
    factor = 0
    numerator = abs(numerator)
    while(min(numerator, deniminator)!=0):
        if(numerator > deniminator):
            numerator %= deniminator
        elif(numerator < deniminator):
            deniminator %= numerator
    factor = max(numerator, deniminator)
    return factor
main()