"""
026. 找出正整數之加法表達方式
所有的正整數都可以以連續的正整數相加的和來表達。
例如: 9有3種表達方式
2+3+4
4+5
9
給一個正整數N(N>0)，請計算出N有多少種以連續的正整數相加的和來表達的方式。

輸入說明:
輸入一個正整數N (N>0)
輸出說明:
輸出有哪幾種相加方式。
輸出順序由小到大。
不合法的輸入則輸出E。
"""

def main():
    num = input()
    if(num.isnumeric() and int(num)>0): #判斷是否合法 需為數字
        complete = compute(int(num)) #找出表達方式
        for i in complete:
            print('%s' %i)
    else:
        print('E')

def compute(num): #找出表達方式
    complete = [] #表達方式
    n = 1 #用來由i開始順序之數字
    total = 0 #當前組合總和
    i = 1 #i為起始值
    while i<=num//2: 
        total += n
        if(total==num): #判斷當前連續整數總和是否等於輸入之數值
            string = stringadd(n, i) #製作輸出字串
            complete.append(string) #加入至表達方式
        elif(total>num): #判斷當前連續整數總和大於等於輸入之數值
            total = 0 #歸零
            i +=1 #起始值+1
            n = i #n從i開始
            continue
        n += 1 #順序之數字+1
    complete.append(num) #輸入之數值本身也是一種表達方式
    return complete
    
def stringadd(n, i): #製作輸出字串 i為起始值 n為當前順序之數字
    string = ''
    for i in range(i, n+1):
        string += str(i)
        if(i!=n):
            string += '+'
    return string
main()