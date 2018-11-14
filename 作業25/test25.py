def main():
    ninth = list(map(int, input().split()))
    tenth = list(map(int, input().split()))
    result = compute(ninth, tenth)
    print('%d' %result)

def compute(ninth, tenth):
    result = 0
    n = 0
    i = 0
    if(ninth[0]==10):
        result = 10
        while n!=2 and i<len(tenth):
            if(tenth[i]!=0 and sum(tenth[:2])==10):
                result += tenth[i]
                n += 1
            else:
                result += sum(tenth[:2])
                n = 2
            i += 1
    elif(sum(ninth)==10):
        result = sum(ninth) + tenth[0] if tenth[0]>0 else tenth[1]
    else:
        result = sum(ninth)
    result += sum(tenth)
    return result
main()