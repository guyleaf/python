"""
004. 判斷基數偶數

輸入說明：
輸入一個整數

輸出說明：
輸出奇數或偶數

輸入範例:
3
輸出範例:
odd

輸入範例:
6
輸出範例:
even
"""

import math
def identify(num): #判斷奇偶
    if (num % 2 == 0):
       print('even')
    else:
       print('odd')
	
def main(): #main
    num = int(input())
    identify(num)
	
main()