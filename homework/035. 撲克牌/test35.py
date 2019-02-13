"""
035. 撲克牌
撲克牌四種花色分別是黑桃、紅心、磚塊、梅花，定義 S, H, D, C。
牌面數字2~13，A為 14，共有52張牌。
花色大小：黑桃>紅心>方塊>梅花。
編碼規則為數字+花色，例如 10S 表黑桃 10、7D 表磚塊 7，12C 表梅花 Q。

撲克牌遊戲把單一張牌命名為單張，沒有任何花色牌型，編號 0。
兩張數字一樣的命名為 Pair，編號 1。
2 組 pair 的牌稱為 Two pair，編號 2。
三張一樣的稱為 Three of a Kind，編號 3。
數字連續的5張牌稱為 Straight，包括 13 ,14, 2, 3, 4，編號 4。
Three of a Kind 加一個 Pair 稱為 Full House，編號 5。
四張一樣稱為 Four Of A Kind，編號 6。
數字連續的5張且花色一樣稱為 Straight Flush，編號 7。
輸入5張撲克牌，判斷哪一類型的牌形編號(0~7)。

輸入說明 ：
第一列輸入為5個編碼分別由空格分開，表示5張撲克牌。
輸出說明 ：
輸出為一個0~7的整數，代表牌型編號。
Input:
-------------------------
9D 8C 8S 8H 9S
Output:
------------------------
5
"""

def input_f(): #輸入poker
    poker = list(input().split())
    return poker

def game(): #遊戲本體
    poker = input_f()
    N = [int(i.replace(i[-1], '')) for i in poker] #取數字
    S = [i[-1] for i in poker] #取花色
    if(flush(S) and Straight(sorted(N))): return 7 #同花順
    elif(Straight(sorted(N))): return 4 #順子
    return pair(N) #pair

def pair(N): #pair
    F = [N.count(i) for i in N]
    if(4 in F): return 6 #鐵支
    elif(3 in F and 2 in F): return 5 #葫蘆
    elif(3 in F): return 3 #三條
    elif(F.count(2)==4): return 2 #two pair
    elif(F.count(2)==2): return 1 #one pair
    else: return 0 #散牌

def flush(S): #同花
    if(S.count(S[0])!=5): return 0
    return 1

def Straight(N): #順子
    if(14 in N and 2 in N): #12 13 14 2 3  也可為順子
        for i in range(5): 
            if(N[i]<=5):
                N[i] += 13 #12 13 14 2+13 3+13
        for i in range(min(N), min(N)+5): 
            if(N.count(i)!=1): #從最小開始 依序檢查
                return 0
    else:
        for i in range(min(N), min(N)+5):
            if(N.count(i)!=1): #從最小開始 依序檢查
                return 0
    return 1

def main(): #main
    result = game()
    print(result)
main()