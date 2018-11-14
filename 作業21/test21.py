def main():
    group = []
    result = []
    addnum = []
    checknum = num = i = j = 0
    n = int(input())
    while(i<n):
        num = input()
        group.append(list(map(int, num)))
        num = int(num)
        group[i].extend(ip(num))
        addnum.append(num)
        total = compute(group[i])
        result.append(total)
        i += 1
    if(n<0):
        print('E')
    for i in range(n):
        checknum = check(group[i], addnum[i])
        if(checknum==-1):
            print('E')
        elif(checknum==1):
            print('%d' %result[i])

def ip(num): #input number
    register = []
    sign = 0
    for i in range(num):
        register.append(list(map(int, input().split())))
    register.sort()
    for i in range(num): #extend list of list && remove list of list
        register.extend(register[i-sign])
        register.pop(i-sign)
        sign +=1
    return register

def check(group, num):
    if not(len(group)== num*2+1):
        return -1
    elif(group[0]<0 or group[0]>5000):
        return -1
    for i in range(1, len(group)-1, 2):
        if((group[i]>group[i+1]) or group[i]<0 or group[i+1]<0 or group[i]>60000 or group[i+1]>60000):
            return -1
    return 1

def compute(group):
    total = 0
    total = group[2] - group[1]
    for i in range(3, len(group)-1, 2):
        total += othercompute(group, i)
    return total

def othercompute(group, i):
    totalright = totalleft = 0
    for j in range(1, i, 2):
        if((group[i]>=group[j]) and (group[i]<=group[j+1]) and (group[i+1]<=group[j+1])):
            return 0
    for j in range(1, i, 2):
        cc = group[i]
        if((cc<group[j]) and (group[i+1]>group[j])):
            totalleft = group[j] - cc
        if((cc<group[j+1]) and (group[i+1]>group[j+1])):
            cc = group[j+1]
            totalright = group[i+1] - cc
    if((totalright + totalleft)==0):
        total = group[i+1] - group[i]
        return total
    return totalright + totalleft
main()