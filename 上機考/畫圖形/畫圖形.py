def f1(n):
    if(n%2!=0 and 1<=n<=15):    #n={1,3,5,7,9,11,13,15}
        for i in range(n//2+1):
            for j in range(i):
                print('.', end='')
            for j in range(n-2*i):
                print('*', end='')
            for j in range(i):
                print('.', end='')
            print()
        for i in range(n//2):
            for j in range((n//2)-i, 1, -1):
                print('.', end='')
            for j in range(2*(i+1)+1):
                print('*', end='')
            for j in range((n//2)-i, 1, -1):
                print('.', end='')
            print()
    else:
        print('Error(n is 1,3,..,15)')

def f2(n):
    if(1<=n<=9 and n%2!=0):    #n={1,3,5,7,9}
        m = 0
        m = 2*n-1
        for i in range(m//2+1):
            for j in range(m-1-2*i):
                print('.', end='')
            for j in range(n, n-i-1, -1):
                print(j, end='')
                if(n-i!=j):
                    print('.', end='')
            for j in range(n-i+1, n+1):
                print('.', end='')
                print(j, end='')
            for j in range(m-1-2*i):
                print('.', end='')
            print()
        for i in range(m//2):
            for j in range(m-2*i-2, m):
                print('.', end='')
            for j in range(n, 1+i, -1):
                print(j, end='')
                if(i+2!=j):
                    print('.', end='')
            for j in range(3+i, n+1):
                print('.', end='')
                print(j, end='')
            for j in range(m-2*i-2, m):
                print('.', end='')
            print()
    else:
        print('Error(n is 1,3,..,9)')

def f3(n):
    if(1<=n<=16):    #n={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
        for i in range(n, 0, -1):
            for j in range(n-i):
                print('.', end='')
            for j in range(i, 0, -1):
                if(j*2-1>=10):
                    print(chr(j*2-1+87), end='')
                else:
                    print(j*2-1, end='')
            for j in range(1, i):
                if(j*2+1>=10):
                    print(chr(j*2+1+87), end='')
                else:
                    print(j*2+1, end='')
            for j in range(n-i):
                print('.', end='')
            print()
    else:
        print('Error(n is 1,2,..,16)')

def main():
    n = 1
    while n!=0:
        n = int(input())
        if(n==0):
            break
        elif(n==1):
            f1(int(input()))
        elif(n==2):
            f2(int(input()))
        elif(n==3):
            f3(int(input()))
        else:
            print('Error(0, 1, 2, 3)')
main()