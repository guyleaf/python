import math
def main():
    num = input()
    if(num.isdecimal() and num!='1'):
        prime_factor = findprime_factor(int(num))
        level_output(prime_factor)
    else:
        print('E')
def findprime_factor(num):
    prime_factor = []
    if(num%2==0):
        prime_factor.append(2)
    for i in range(3,num+1):
        for j in range(2,i):
            if(i % j==0):
                sign = 1
                break
            else:
                sign = 0
        if(sign==0 and num%i==0):
            prime_factor.append(i)
    return prime_factor
def level_output(prime_factor):
    total = 0
    for i in prime_factor:
        total += math.factorial(i)
        print('%d,%d' %(i, math.factorial(i)))
    print(total)
main()