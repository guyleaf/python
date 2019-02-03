"""
014. 停車費計算
假設某個停車場的費率是停車2小時以內，每半小時30元，未滿半小時部分不計費。
超過2小時，但未滿4小時，每半小時40元，未滿半小時以半小時計費。
超過4小時以上的部份，每半小時60元，未滿半小時以半小時計費。
請撰寫程式計算輸入數筆資料，共需繳交的停車費。
本程式不考慮隔夜情況。

輸入說明：
---------------
輸入3組時間，每組分別為開始與離開時間，24小時制。
若輸入格式錯誤，則輸出error

輸出說明：
---------------
輸出總停車費。

測試案例(Test Case)資料：
Input：
8:00
9:15
13:45
16:50
6:20
10:50
Output：
60
240
340

Input：
00:01
25:00
00:11
23:66
-01:00
12:34
Output：
error
error
error
"""

import math
def main(): #main
    hr = [] #小時
    min = [] #分鐘
    for i in range(6): #輸入
        a, b = map(int, input().split(":"))
        hr.append(a)
        min.append(b)
    check(hr, min) #檢查

def check(hr, min):
    for i in range(0,6,2):
        if(hr[i]>=24 or hr[i]<0 or min[i]>=60 or min[i]<0):
            print('error')
        elif(hr[i+1]>=24 or hr[i+1]<0 or min[i+1]>=60 or min[i+1]<0):
            print('error')
        else:
            space = compute(hr, min, i)
            total = fee(space)
            output(total)
        
def compute(hr, min, i): #換算成分鐘數
    sum = (hr[i+1]*60+min[i+1])-(hr[i]*60+min[i])
    return sum

def fee(space): #計算費用
    quotient = space // 30 #取半分鐘
    remainder = space % 30 #取分鐘
    if(quotient<4 or (quotient==4 and remainder==0)):
        sum = quotient*30
    elif(quotient<8 or (quotient==8 and remainder==0)):
        sum = (quotient-4)*40 + math.ceil(remainder / 30)*40 + 4*30
    else:
        sum = (quotient-8)*60 + math.ceil(remainder / 30)*60 + 280
    return sum
    
def output(total): #輸出
        print('%d' %total)	
        
main()