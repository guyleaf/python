def main():
    month = int(input())
    past = int(input())
    now = int(input())
    save = compare(past, now)
    if(month>=7 and month<=9):
        total = compute_summer(past, now, save)
    else:
        total = compute_notsummer(past, now, save)
    output(total)
def compare(past, now):
    if(past>now):
        return 1
def compute_summer(past, now, save):
    if(save==1):
        if(now<=120):
            return now*2.1-(past-now)*0.6
        elif(now<=330):
            return now*3.02-(past-now)*0.6
        elif(now<=500):
            return now*4.39-(past-now)*0.6
        elif(now<=700):
            return now*4.97-(past-now)*0.6
        else:
            return now*5.63-(past-now)*0.6
    else:
        if(now<=120):
            return now*2.1
        elif(now<=330):
            return now*3.02
        elif(now<=500):
            return now*4.39
        elif(now<=700):
            return now*4.97
        else:
            return now*5.63
def compute_notsummer(past, now, save):
    if(save==1):
        if(now<=120):
            return now*2.1-(past-now)*0.6
        elif(now<=330):
            return now*2.68-(past-now)*0.6
        elif(now<=500):
            return now*3.61-(past-now)*0.6
        elif(now<=700):
            return now*4.01-(past-now)*0.6
        else:
            return now*4.5-(past-now)*0.6
    else:
        if(now<=120):
            return now*2.1
        elif(now<=330):
            return now*2.68
        elif(now<=500):
            return now*3.61
        elif(now<=700):
            return now*4.01
        else:
            return now*4.5
def output(total):
    print('%.2f' %total)
main()