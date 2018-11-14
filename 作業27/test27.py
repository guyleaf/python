def main():
    input_1, input_2 = map(int, input().split())
    check(input_1, input_2)
    
def check(input_1, input_2):
    if(input_1>=10):
        for i in range(input_1, input_2+1):
            display(i)
    else:
        print(0, end=' ')
    print()

def display(i):
    if(str(i)==str(i)[::-1]):
        print(i, end=' ')
main()