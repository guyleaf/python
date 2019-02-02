import math
def main(): #main
    data = input().split()
    avg = average(data)
    var = variance(avg, data)
    st = standard(var)
    output(var, sum, avg)

def output(var, st, avg):
    print('%.2f' %var) #標準差
    print('%.2f' %st) #變異數
    print('%.2f' %avg) #平均數

def average(data): #平均數
    avg = (int(data[0])+int(data[1])+int(data[2])+int(data[3])+int(data[4]))/5
    return avg

def variance(avg, data): #變異數
    var = (int(data[0])-avg)**2+(int(data[1])-avg)**2+(int(data[2])-avg)**2+(int(data[3])-avg)**2+(int(data[4])-avg)**2
    return var/5

def standard(var): #標準差
    st = math.sqrt(var)
    return st
main()