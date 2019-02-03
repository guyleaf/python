"""
019. 猜數列
小明的家庭作業裏有很多數列填空練習。
填空練習的要求是：已知數列的前四項，填出第五項。
因為已經知道這些數列只可能是等差或等比數列，他決定寫一個程式來完成這些練

輸入說明:
第一行是數列的數目t（1 <= t <= 20）。
以下每行均包含四個整數，表示數列的前四項。
輸出說明:
對輸入的每個數列，輸出它的前五項。
不合法的輸入則輸出E。

input :
2
1 2 3 4
32 16 8 4
output:
1 2 3 4 5
32 16 8 4 2
"""

def main(): #main
    question = [] #儲存數列
    num = int(input()) #輸入num組數列
    if(1<=num<=20): #限定1~20組數列
        for i in range(num):
            question.append(list(map(int, input().split()))) #輸入數列
        for i in range(num):
            question, error = checkandanswer(question, i) 
            output(question, i, error)
    else:
        print('E')

def checkandanswer(question, i): #檢查數列有無規律並算出下一數值
    error = 0
    common_ratio = question[i][1] / question[i][0] #公比
    equal_ratio = question[i][1] - question[i][0] #公差
    if(common_ratio==(question[i][2] / question[i][1])==(question[i][3] / question[i][2])): #等比級數
        last = question[i][3] * common_ratio
        question[i].append(last)
    elif(equal_ratio==(question[i][2] - question[i][1])==(question[i][3] - question[i][2])): #等差數列
        last = question[i][3] + equal_ratio
        question[i].append(last)
    else:
        error = 1
    return question, error
    
def output(question, i, error): #輸出
        if(error==0):
            for j in range(5):
                print('%d' %question[i][j], end='')
                print(' ',end='')
            print()
        else:
            print('E')
            
main()