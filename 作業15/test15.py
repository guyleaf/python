def main():
    switch = int(input())
    num = int(input())
    if(switch==1):
        right(num)
    elif(switch==2):
        left(num)
    else:
        rhombus(num)
def right(num):
    n = num//2
    for i in range(n+1):
        for j in range(i+1):
            print('*',end="")
        print()
    for i in range(n):
        for j in range(n-i):
            print('*',end="")
        print()
def left(num):
    n = num//2
    for i in range(n+1):
        for j in range(n-i):
            print('.',end="")
        for j in range(i+1):
            print('*',end="")
        print()
    for i in range(n):
        for j in range(i+1):
            print('.',end="")
        for j in range(n-i):
            print('*',end="")
        print()
def rhombus(num):
    n = num//2
    for i in range(n+1):
        for j in range(n-i):
            print('.',end="")
        for j in range(i+1):
            print('*',end="")
        for j in range(i):
            print('*',end="")
        print()
    for i in range(n):
        for j in range(i+1):
            print('.',end="")
        for j in range(n-i):
            print('*',end="")
        for j in range(n-i-1):
            print('*',end="")
        print()
main()