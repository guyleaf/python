"""
001. 計算總成績、平均
某一學生修國文、計算機概論、計算機程式設計三科，使用者輸入名字（一個char）、學號（int）、三科成績(int)。
(1) 計算學生總成績、平均。
(2) 印出名字、學號、總成績、平均。

Input
K
905067
100
100
100

Output
Name:K
ID:905067
Average:100
Total:300
"""

def computescore(csi, pd, chinese): #計算成績 總平均, 總分
    average = (csi + pd + chinese) //3
    total = csi + pd + chinese
    return average, total
	
def main(): #main
    name = input()
    id = int(input())
    csi = int(input())
    pd = int(input())
    chinese = int(input())
    average, total = computescore(csi, pd, chinese)
    output(name, id, average, total)

def output(name, id, average, total): #輸出
    print('Name:%c' %name)
    print('ID:%d' %id)
    print('Average:%d' %average)
    print('Total:%d' %total)

main()