"""
017. 計算電費
輸入月份、輸入前年所使用的度數及今年使用的度數，
依據月份是否為夏季電費做計算依據，並計算出電費，
若今年度有較前年成功節電，則每節一度電可省0.6元
每度(元) 夏季電價(7~9月) 非夏季電價
120度以下 2.10 2.10
121-330度 3.02 2.68
331-500度 4.39 3.61
501-700度 4.97 4.01
701度以上 5.63 4.50

輸入說明：
---------------
輸入月份
輸入前年使用度數
輸入今年使用度數
輸出說明：
---------------
輸出電費

測試案例(Test Case)資料：
Input：
7
505
525
Output：
2609.25
Input：
7
550
525
Output
2594.25

(以此題為例，較上年度節電25度，故計算方式為525*4.97-(550-525)*0.6)
"""

def main(): #main
    month = int(input()) #月份
    past = int(input()) #前年使用度數
    now = int(input()) #今天使用度數
    save = compare(past, now) 
    if(month>=7 and month<=9): #7~9月為夏季
        total = compute_summer(past, now, save)
    else:
        total = compute_notsummer(past, now, save)
    output(total)
    
def compare(past, now): #比較使用度數
    if(past>now):
        return 1
        
def compute_summer(past, now, save): #計算夏季電費
    if(save==1):
        if(now<=120):
            return now*2.1-(past-now)*0.6
        elif(now<=330):
            return now*3.02-(past-now)*0.6
        elif(now<=500):
            return now*4.39-(past-now)*0.6
        elif(now<=700):
            return now*4.97-(past-now)*0.6
        else:
            return now*5.63-(past-now)*0.6
    else:
        if(now<=120):
            return now*2.1
        elif(now<=330):
            return now*3.02
        elif(now<=500):
            return now*4.39
        elif(now<=700):
            return now*4.97
        else:
            return now*5.63
            
def compute_notsummer(past, now, save): #計算非夏季電費
    if(save==1):
        if(now<=120):
            return now*2.1-(past-now)*0.6
        elif(now<=330):
            return now*2.68-(past-now)*0.6
        elif(now<=500):
            return now*3.61-(past-now)*0.6
        elif(now<=700):
            return now*4.01-(past-now)*0.6
        else:
            return now*4.5-(past-now)*0.6
    else:
        if(now<=120):
            return now*2.1
        elif(now<=330):
            return now*2.68
        elif(now<=500):
            return now*3.61
        elif(now<=700):
            return now*4.01
        else:
            return now*4.5
            
def output(total): #輸出
    print('%.2f' %total)
main()