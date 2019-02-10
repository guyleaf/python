"""
023. 密碼鎖1A2B
四位數字密碼鎖，忘記密碼最多嘗試10^4=10000次解鎖。
若知道嘗試的密碼的錯務資訊，解鎖速度就可增快。
請寫程式判斷猜測數字跟正確答案的正確位置與個數資訊。

輸入說明:
------------------------------------------------
第一行有四個介於0-9之間的數字，代表正確密碼。
第二行後，每行有四個介於0-9之間的數字，代表一組猜測密碼。
最後輸入-1 結束。
輸出說明
------------------------------------------------
每組猜測密碼，跟正確密碼比對規則
(1) 計算數字值正確，且在正確位子的個數 m，記為 mA。
(2) 計算數字值正確，但不在正確位子的個數 n，記為 nB。
(3) 若出現重複數字，每個數字比對一次，先比對規則(1)，若否再比對規則(2)。
如 5543、5255，第一個 5 數字正確，記為1A、第二個 5 數字正確記為1B。
輸出 mAnB。

Sample Input:
---------------
1 2 3 4
1 1 4 5
1 2 4 3
1 1 4 4
4 3 2 1
-1
Sample Output:
--------------
1A1B
2A2B
2A0B
0A4B

Sample Input:
---------------
1 1 1 5
1 1 1 1
0 9 2 8
1 5 2 3
1 1 5 1
-1
Sample Output:
--------------
3A0B
0A0B
1A1B
2A2B
"""

def main():
    correct = [] #正確組合
    guess = [] #猜組合
    correct = list(map(int, input().split()))
    while True:
        guess.append(list(map(int, input().split())))
        if(-1 in guess[len(guess)-1]): #檢查是否輸入結束
            del guess[len(guess)-1]
            break
            
    for i in guess:
        A, B = compare(i, correct) #正確組合與猜組合個別比對
        print("%dA%dB" %(A, B)) #?A?B
        
def compare(guess, correct):
    A = 0
    B = 0
    copy_guess = guess.copy()
    copy_correct = correct.copy()
    for i, num in enumerate(guess): #index, num
        if(findposition(num, correct, i)): #判斷?A
            copy_correct.pop(i-A) #刪除判斷成A的數字
            copy_guess.pop(i-A) #刪除判斷成A的數字
            A +=1

    B = findnum(copy_correct, copy_guess) #扣掉B有重複數字
    return A, B
    
def findposition(num, correct, j): #判斷?A
    if(correct[j]==num): #index相等&數字相等 回傳1
        return 1
    return 0
    
def findnum(copy_correct, copy_guess): #判斷?A
    B = 0
    for i in list(set(copy_guess)):
        if(copy_guess.count(i)>copy_correct.count(i)): #猜組合>正確組合
            B += copy_correct.count(i)
        else:
            B += copy_guess.count(i)
    return B
main()