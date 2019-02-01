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