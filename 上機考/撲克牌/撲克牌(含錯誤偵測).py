def input_f():
    num = list(map(int, input().split()))
    num.sort()
    sign = []
    for i in range(5):
        sign.append(num[i]//100)
        num[i] = num[i] - ((num[i]//100)*100)
    return num, sign
def main():
    num, sign = input_f()
    if(check(num, sign)):
        print(identify(num, sign))
    else:
        print('Error')
###########檢測###########
def check(num, sign):
    quantity = []
    start = 0
    for i in range(5):
        if(num[i]<=0 or num[i]>=14 or sign[i]<=0 or sign[i]>=5):
            return 0
        quantity.append(sign.count(i)) #儲存各花色有幾張
    for i in quantity[1:]:
        start = repeat(start+i, num[start:start+i]) #牌數範圍 start ~ i, start(2nd) ~ i(2nd), start(3nd) ~ i(3th) 
        if(start==0):
            return 0
    return 1

def repeat(scope, x):
    for j in range(1, 14):
        if(x.count(j)>1): #牌數範圍內檢查有無重複
            return 0
    return scope
###########檢測結束###########
def identify(num, sign):
    for i in range(1, 5):
        if(sign.count(i)==5 and Straight(num)):
            return '同花順'
        elif(sign.count(i)==5):
            return '同花'
    num.sort()
    for i in range(1, 14):
        if(num.count(i)==4):
            return '鐵支'
        elif(num.count(i)==3 and (num[0]!=num[1] or num[3]!=num[4])):
            return '三條'
        elif(num.count(i)==3):
            return '葫蘆'

    if(Straight(num)):
        return '順子'
    j = 0
    for i in range(1, 14):
        if(num.count(i)==2):
            j += 1
    if(j==2):
        return '兩對'
    elif(j==1):
        return '一對'
    else:
        return '散套'

def Straight(num):
    space = num[0]
    if(num==[1, 10, 11, 12, 13]):
        return 1
    for i in range(1, 5):
        if(num[i]!=space+i):
            return 0
    return 1
main()