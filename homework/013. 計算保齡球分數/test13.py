"""
013. 計算保齡球分數(無視規則-除了第十局)
小明到保齡球館打保齡球，一輪有十局，假設小明一到八局都拿零分，剩下最後兩局
每局有十瓶保齡球瓶，倒一瓶保齡瓶得一分，每一局最多為十分，
每一局可以打兩次，若在第十局打出strike，可以再多打一局，但當局只能打一次，試算出總得分
測試案例(Test Case)資料：
Input：
2
5
7
1
Output：
15
---------------
Input：
5
5
10
0
8
Output：
28
"""

def main(): #main
    p1 = int(input())
    p2 = int(input())
    p3 = int(input())
    p4 = int(input())
    p5 = compare(p3, p4)
    compute(p1, p2, p3, p4, p5)

def compare(p3, p4): #判斷第十局是否strike或spare
    if(p3+p4>=10):
        p5 = int(input())
        return p5
    else:
        return 0

def compute(p1, p2, p3, p4, p5): #計算總分並輸出
    sum = p1 + p2 + p3 + p4 + p5
    print('%d' %sum)
    
main()