def main():
    p1 = int(input())
    p2 = int(input())
    p3 = int(input())
    p4 = int(input())
    p5 = 0
    p5 = compare(p3)
    compute(p1, p2, p3, p4, p5)
def compare(p3):
    if(p3==10):
        p5 = int(input())
        return p5
    else:
        return 0
def compute(p1, p2, p3, p4, p5):
    sum = p1 + p2 + p3 + p4 + p5
    print('%d' %sum)
main()