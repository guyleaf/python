"""
032. 旋轉抽抽樂
小明有個N*M(１≦N≦10,1≦M≦10) 的抽抽樂矩陣, 裡面放著1~9號等獎項,
小明在走樓梯的時候不小心手滑讓抽抽樂滾走，
抽抽樂有三種滾動方式:向右轉90度,向左轉90度,向右轉180度,
請幫助小明找出目前的獎項排列。

輸入說明:
3 3 (矩陣大小為3*3)(數字間有空格)
123 (輸入矩陣內的獎項)(數字之間沒有空格)(數字可重複)
321
456
12321322 (滾動方式 1=:向右轉90度 ,2=向左轉90度, 3=向右轉180度)
輸出說明:
輸出旋轉後的矩陣。(數字間沒有空格)
不合法的輸入則輸出E。
------------測資--------------
input:
3 4
1234
3216
1397
12321233
output:
131
322
913
764
--------------------------------
input
1 10
123456789
3321
output:
E
--------------------------------
input
1 10
1234567893
123321313
output:
1
2
3
4
5
6
7
8
9
3
"""

def input_f(): #輸入
    n, m = map(int, input().split()) #行and列
    data = [] #圖形
    for i in range(n):#n行
        data.append(list(map(int, input())))
        if(len(data[i])!=m): return 0 #檢查每行數字個數是否違反
    return data
 
def main(): #main
    data = input_f() #輸入
    if(data==0): #違反
        print("E")
    else:
        order = list(map(int, input())) #旋轉順序
        for i in order: #依序旋轉
            if(i==1): #向右旋轉90度
                data = rotate_right(data)
            elif(i==2): #向左旋轉90度
                data = rotate_left(data)
            elif(i==3): #旋轉180度
                data = rotate_180(data)
            else: #旋轉代碼違反規則
                print("E")
                return
        for i in data: #輸出旋轉後的矩陣
            print("".join(map(str, i)))

def rotate_right(data): #向右旋轉90度
    data = list(zip(*data[::-1]))
    return data

def rotate_left(data): #向左旋轉90度
    data = list(zip(*data))[::-1]
    return data

def rotate_180(data): #旋轉180度
    for i in range(len(data)):
        data[i] = data[i][::-1]
    data = data[::-1]
    return data
main()