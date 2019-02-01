import math
def identify(num):
    if (num % 2 == 0):
       print('even')
    else:
       print('odd')
	
def main():
    num = int(input())
    identify(num)
	
main()