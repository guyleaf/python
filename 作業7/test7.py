import math
def main():
    b = input().split()
    avg = average(b)
    var = variance(avg, b)
    sum = standard(var)
    print('%.2f' %var)
    print('%.2f' %sum)
    print('%.2f' %avg)

def average(st):
    avg = (int(st[0])+int(st[1])+int(st[2])+int(st[3])+int(st[4]))/5
    return avg
def variance(avg, st):
    var = (int(st[0])-avg)**2+(int(st[1])-avg)**2+(int(st[2])-avg)**2+(int(st[3])-avg)**2+(int(st[4])-avg)**2
    return var/5
def standard(var):
    sum = math.sqrt(var)
    return sum
main()