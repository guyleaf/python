def create():
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    A = []
    B = []
    #A = [i for i in range(0, 10000) if Filter(i)]
    for i in range(10000):
        x1 = i%10
        x2 = (i%100 - x1)//10
        x3 = (i%1000 - x1)//100
        x4 = (i%10000 - x1)//1000
        if x4!=x3 and x4!=x2 and x4!=x1 and x3!=x2 and x3!=x1 and x2!=x1:
            B.append([x4, x3, x2, x1])
    return B

def identify(num, guess, result):
    new = []
    count = 0
    for i in range(len(result)):
        A = 0
        B = 0
        copy_num = []
        copy_list = []
        copy_num.extend(num)
        copy_list.extend(result[i])
        for j in range(4):
            if(result[i][j]==num[j]):
                copy_list.pop(j-A)
                copy_num.pop(j-A)
                A +=1
        for x in copy_num:
            if(copy_list.count(x)>0):
                B +=1
        del copy_list, copy_num
        if(guess[0]!=str(A) or guess[2]!=str(B)):
            new.append(i)
    for i in new:
        result.pop(i-count)
        count += 1
    return result

def main():
    group = [] 
    guess = []
    num = []
    result = create()
    #result.extend(list_init)
    for i in range(5):
        num, guess = input().split(',')
        if('4A0B' in guess):
            for j in num:
                print(j, end='')
            print()
            break
        num = list(map(int, num))
        result = identify(num, guess, result)
        if(len(result)==1):
            for j in result[0]:
                print(j, end='')
            print()
            break
main()