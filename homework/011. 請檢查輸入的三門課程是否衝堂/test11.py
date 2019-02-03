"""
011. 請檢查輸入的三門課程是否衝堂。
依序輸入
課程編號 (4位數字)、
上課小時數 (1-2小時)、
上課時間 (依小時數輸入上課時間, 星期1-5, 第1-8節)。
輸入任何錯誤，輸出-1。

輸入說明：
---------------
1002 (第一門課課程編號)
2 (2 小時)
33 (星期 3 第 3 節課)
59 (星期 5 第 9 節課)
1003 (第二門課課程編號)
2 (2 小時)
11 (星期 1 第 1 節課)
33 (星期 3 第 3 節課)
3003 (第三門課課程編號)
2 (2 小時)
11 (星期 1 第 1 節課)
33 (星期 3 第 3 節課)
(上課時間輸入順序為星期 1~5，第 1 節 ~ 第 8 節)
(課程編號輸入順序為編號大小)

輸出說明：
---------------
1002,1003,33
1002,3003,33
1003,3003,11
1003,3003,33
輸出 課程編號,課程編號,衝突時間
若沒有衝突則輸出 correct
若有錯誤輸入則輸出 -1
(每次列出兩個衝突課程編號，一個衝突時間，所有倆倆課程衝突均要列出)
(衝突輸出順序，課程 1-2, 1-3, 2-3, 第 1 節 ~ 第 2 節)

測試案例(Test Case)資料：
Input：
1001
2
12
13
1002
2
13
21
1003
2
21
25
Output：
1001,1002,13
1002,1003,21
---------------
Input：
1001
1
21
1002
2
32
33
1003
2
45
46
Output：
correct
---------------
Input：
101
3
99
1002
2
32
33
1003
2
45
46
Output：
-1
"""

def main(): #main
    class1=[]
    class2=[]
    class3=[]
    num1 = int(input()) #課程編號
    hr1 = int(input()) #上課時數
    if(hr1==1):
        class1.append(int(input())) #第幾節
    elif(hr1==2):
        class1.append(int(input()))
        class1.append(int(input()))
    else:
        class1.append(int(input()))
        
    num2 = int(input())
    hr2 = int(input())
    if(hr2==1):
        class2.append(int(input()))
    elif(hr2==2):
        class2.append(int(input()))
        class2.append(int(input()))
    else:
        class2.append(int(input()))
        
    num3 = int(input())
    hr3 = int(input())
    if(hr3==1):
        class3.append(int(input()))
    elif(hr3==2):
        class3.append(int(input()))
        class3.append(int(input()))
    else:
        class3.append(int(input()))
        
    if(hr1 > 2 or hr3 > 2 or hr2 > 2 and checknum(num1, num2, num3)): #檢查課程編號及時數
        print('-1')
    else:
        space12, space13, space23 = compare(num1, num2, num3, class1, class2, class3)
        output(space12, space13, space23)

def checknum(num1, num2, num3): #檢查課程編號
     if(num1<=num2 and num1 <=num3 and num2<=num3): #檢查是否由小到大
         return 1
     else:
         return -1
         
def compare(num1, num2, num3, class1, class2, class3): #比較有無衝堂
    space12=[num1, num2] #1-2衝堂列表
    space13=[num1, num3] #1-3衝堂列表
    space23=[num2, num3] #2-3衝堂列表
    for i in class1:
        if(i in class2): #1-2比較
            space12.append(i)
        if(i in class3): #1-3比較
            space13.append(i)
    for j in class2: #2-3比較
        if(j in class3):
            space23.append(j)
    return space12, space13, space23
    
def output(space12, space13, space23): #輸出衝堂
    if(len(space12)==len(space13)==len(space23)==2): #皆無衝堂則輸出correct
        print('correct')
        return
    if(len(space12)==3):
        print('%d,%d,%d' %(space12[0], space12[1], space12[2]))
    elif(len(space12)==4):
        print('%d,%d,%d' %(space12[0], space12[1], space12[2]))
        print('%d,%d,%d' %(space12[0], space12[1], space12[3]))
    if(len(space13)==3):
        print('%d,%d,%d' %(space13[0], space13[1], space13[2]))
    elif(len(space13)==4):
        print('%d,%d,%d' %(space13[0], space13[1], space13[2]))
        print('%d,%d,%d' %(space13[0], space13[1], space13[3]))
    if(len(space23)==3):
        print('%d,%d,%d' %(space23[0], space23[1], space23[2]))
    elif(len(space23)==4):
        print('%d,%d,%d' %(space23[0], space23[1], space23[2]))
        print('%d,%d,%d' %(space23[0], space23[1], space23[3]))
    
main()