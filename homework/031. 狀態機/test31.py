"""
031. 有限狀態機
一個有限狀態機(Finite state machine, FSM) 從起始狀態(start)開始運作，
包含一組橢圓形表示的狀態(State)和一組箭頭表示的轉換(Transition)連接兩個狀態，且接受輸入字元資料。
請參考圖片作答，來源網址 : https://imgur.com/a/H0Uya
寫一個function模擬FSM運作流程，識別C語言正確的識別字(Identifier)與非負整數(Number)。
每項資料項目以一或多的空白結束，以句點（.）結束。
需偵測不合法(Invalid)的輸入。

FSM Transition Symbol
Digit(1) 0, 1, .., 9
Period (2) .
Blank(3) 空白
Letter(4) A,.., Z, a, .., z
Letter(5) A,.., Z, a, .., z
Digit(6) 0, 1, .., 9
Underscore(7) _
Blank(8) 空白
Digit(9) 0, 1, .., 9
Blank(10) 空白
Others1(11) 非空白、非Digit、非Letter、非底線
Blank(12) 空白
Others2(13) 非空白、非Digit
Others3(14) 非空白

Input:
rate R2D2 48 2 time 555666 .
Output:
rate - Identifier
R2D2 - Identifier
48 - Number
2 - Number
time - Identifier
555666 - Number
---------------------------------------------------
Input: 4132 6rte r_yg t#ee 6677 .
Output:
4132 - Number
6rte - Invalid
r_yg - Identifier
t#ee - Invalid
6677 - Number
"""

def start(): #起點
    inf = input()
    while inf != '.':
        #判斷是否為號碼 or ID
        if(inf[0].isdigit()): 
            inf = build_num(inf)
        else:
            inf = build_id(inf)

def build_id(inf): #ID
    i = 0
    while True:
        if(inf[i].isspace()): #遇到空格擷取並輸出
            tmp, inf = inf.split(' ', 1)
            identifier(tmp) #輸出ID
            break
        elif(not(inf[i].isspace()) and not(inf[i].isdigit()) and not(inf[i].isalpha()) and inf[i]!= '_'): #檢查ID
            inf = build_invalid(inf, i)
            break
        i += 1
    return inf
        
def build_num(inf): #號碼
    i = 0
    while True:
        if(inf[i].isspace()): #遇到空格擷取並輸出
            tmp, inf = inf.split(' ', 1)
            number(tmp) #輸出number
            break
        elif(not(inf[i].isspace()) and not(inf[i].isdigit())): #檢查號碼
            inf = build_invalid(inf, i)
            break
        i += 1
    return inf
    
        
def build_invalid(inf, i): #違法字串
    i += 1
    while True:
        if(inf[i].isspace()):
            tmp, inf = inf.split(' ', 1)
            invalid(tmp) #輸出違法字串
            break
        i += 1
    return inf
        
def number(tmp):
    print(tmp + ' - Number')
    
def invalid(tmp):
    print(tmp + ' - Invalid')
    
def identifier(tmp):
    print(tmp + ' - Identifier')

start()