def main():
    class1=[]
    class2=[]
    class3=[]
    num1 = int(input())
    hr1 = int(input())
    if(hr1==1):
        class1.append(int(input()))
    elif(hr1==2):
        class1.append(int(input()))
        class1.append(int(input()))
    else:
        class1.append(int(input()))
    num2 = int(input())
    hr2 = int(input())
    if(hr2==1):
        class2.append(int(input()))
    elif(hr2==2):
        class2.append(int(input()))
        class2.append(int(input()))
    else:
        class2.append(int(input()))
    num3 = int(input())
    hr3 = int(input())
	
    if(hr3==1):
        class3.append(int(input()))
    elif(hr3==2):
        class3.append(int(input()))
        class3.append(int(input()))
    else:
        class3.append(int(input()))
    check = checknum(num1, num2, num3)
    if(hr1 > 2 or hr3 > 2 or hr2 > 2):
        check = -1
    if(check==-1):
        print('-1')
    else:
        space12, space13, space23 = compare(num1, num2, num3, class1, class2, class3)
        output(space12, space13, space23)
def checknum(num1, num2, num3):
     if(num1<=num2 and num1 <=num3 and num2<=num3):
         return 1
     else:
         return -1
def compare(num1, num2, num3, class1, class2, class3):
    space12=[num1, num2]
    space13=[num1, num3]
    space23=[num2, num3]
    for i in class1:
        if(i in class2):
            space12.append(i)
        if(i in class3):
            space13.append(i)
    for j in class2:
        if(j in class3):
            space23.append(j)
    return space12, space13, space23
def output(space12, space13, space23):
    if(len(space12)==3):
        print('%d,%d,%d' %(space12[0], space12[1], space12[2]))
    elif(len(space12)==4):
        print('%d,%d,%d' %(space12[0], space12[1], space12[2]))
        print('%d,%d,%d' %(space12[0], space12[1], space12[3]))
    if(len(space13)==3):
        print('%d,%d,%d' %(space13[0], space13[1], space13[2]))
    elif(len(space13)==4):
        print('%d,%d,%d' %(space13[0], space13[1], space13[2]))
        print('%d,%d,%d' %(space13[0], space13[1], space13[3]))
    if(len(space23)==3):
        print('%d,%d,%d' %(space23[0], space23[1], space23[2]))
    elif(len(space23)==4):
        print('%d,%d,%d' %(space23[0], space23[1], space23[2]))
        print('%d,%d,%d' %(space23[0], space23[1], space23[3]))
    if(len(space12)==len(space13)==len(space23)==2):
        print('correct')
main()