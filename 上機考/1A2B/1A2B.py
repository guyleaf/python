def create(): #1A2B
    A = ['{0:0>4}'.format(i) for i in range(0, 10000) if Filter(i)]
    return A

def Filter(i):
    i = '{0:0>4}'.format(i)
    for x in range(10):
        if(i.count(str(x))>1):
            return 0
    return 1

def identify(num, guess, result):
    new = []
    count = 0
    for i in range(len(result)):
        A = 0
        B = 0
        for j in range(4):
            if(result[i][j]==num[j]):
                A +=1
        B = len(set(num) & set(result[i]))- A
        if(guess[0]!=str(A) or guess[2]!=str(B)):
            new.append(i)
    for i in new:
        result.pop(i-count)
        count += 1
    return result

def main():
    guess = []
    num = []
    result = create()
    #result.extend(list_init)
    for i in range(5):
        num, guess = input().split(',')
        num = list(map(int, num))
        result = identify(num, guess, result)
        if(len(result)==1):
            for j in result[0]:
                print(j, end='')
            print()
            break
main()