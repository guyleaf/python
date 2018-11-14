def main():
    question = []
    num = int(input())
    if(1<=num<=20):
        for i in range(num):
            question.append(list(map(int, input().split())))
        for i in range(num):
            question, error = check(question, i)
            output(question, i, error)
    else:
        print('E')
def check(question, i):
    error = 0
    common_ratio = question[i][1] / question[i][0]
    equal_ratio = question[i][1] - question[i][0]
    if(common_ratio==(question[i][2] / question[i][1])==(question[i][3] / question[i][2])):
        last = question[i][3] * common_ratio
        question[i].append(last)
    elif(equal_ratio==(question[i][2] - question[i][1])==(question[i][3] - question[i][2])):
        last = question[i][3] + equal_ratio
        question[i].append(last)
    else:
        error = 1
    return question, error
def output(question, i, error):
        if(error==0):
            for j in range(5):
                print('%d' %question[i][j], end='')
                print(' ',end='')
            print()
        else:
            print('E')
main()