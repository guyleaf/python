def main():
    try:
        num = input()
        if(int(num)>0):
            complete = compute(int(num))
            for i in complete:
                print('%s' %i)
        else:
            print('E')
    except:
        print('E')

def compute(num):
    complete = []
    n = 1
    result = 0
    i = 1
    while i<=num//2:
        result += n
        if(result==num):
            string = stringadd(n, i)
            complete.append(string)
        elif(result>num):
            result = 0
            i +=1
            n = i
            continue
        n += 1
    complete.append(num)
    return complete
def stringadd(n, i):
    string = ''
    for i in range(i, n+1):
        string += str(i)
        if(i!=n):
            string += '+'
    return string
main()