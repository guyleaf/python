import math
def getx(a, b, c):
    x1 = ((-b) + (math.sqrt(b**2-4*a*c))) / (2*a)
    x2 = ((-b) - (math.sqrt(b**2-4*a*c))) / (2*a)
    return x1, x2


	
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x1, x2 = getx(a, b, c)
    print('%.1f' %x1)
    print('%.1f' %x2)
	
main()