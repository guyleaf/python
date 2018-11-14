def main():
    ax1 = int(input())
    ax2 = int(input())
    bx1 = int(input())
    bx2 = int(input())
    cx1 = int(input())
    cx2 = int(input())
    sum = compute(ax1, ax2, bx1, bx2, cx1, cx2)
    space = compare(ax1, ax2, bx1, bx2, cx1, cx2)
    output(sum, space)

def compute(ax1, ax2, bx1, bx2, cx1, cx2):
    sum = (ax2-ax1)+(bx2-bx1)+(cx2-cx1)
    return sum

def compare(ax1, ax2, bx1, bx2, cx1, cx2):
    space1 = 0
    space2 = 0
    space3 = 0
    space4 = 0
    sign1 = 0
    sign2 = 0
    sign3 = 0
    sign4 = 0
    for i in range(ax1, ax2+1):
        if(i==bx1):
            sign1 = 1
        if(i==bx2):
            space1 = bx2 - bx1
            sign1 = 0
        if(i==cx1):
            sign2 = 1
        if(i==cx2):
            space2 = cx2 - cx1
            sign2 = 0
            sign3 = 0
    if(sign1==1):
        space1= ax2 - bx1
    if(sign2==1):
        space2= ax2 - cx1
        sign3 = 1
	
    for j in range(bx1, bx2+1):
        if(sign3==1 and j==cx2):
            space3 = cx2 - ax2
            sign3 = 0
        elif(sign3==1):
            space3 = bx2 - ax2
        if(sign2==0 and j==cx1):
            sign4 = 1
        if(j==cx2):
            space4 = cx2 - cx1
            sign4 = 0
    if(sign4==1):
        space4= bx2 - cx1
    return space1+space2+space3+space4
def output(sum, space):
    print('%d' %(sum-space))
main()