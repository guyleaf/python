def data(row_num, column_num):
    row = []
    column = []
    for i in range(row_num):
        row.append(list(map(int, input())))
    column = list(map(list, zip(*row)))
    return row, column
    
def check(rank):
    for i in range(1, 3):
        if(rank.count(str(i))//2==4):
            rank.replace(str(i), '', 4)
    rank = rank.replace('3', '', (rank.count('3')//2)*2)
    num = min(rank.count('1'), rank.count('2'))
    rank = rank.replace('1', '', num)
    rank = rank.replace('2', '', num)
    return rank

def main():
    row_num, column_num= map(int, input().split())
    try:
        row, column = data(row_num, column_num)
        if(1<=row_num<=10 and 1<=column_num<=10 and len(column)==column_num):
            rank = input()
            rank = check(rank)
            new = sort_shape(row, column, rank)
            output(new)
        else:
            print('E')
    except:
        print('E')

def sort_shape(row, column, rank):
    new, row, column = rotate_1(row, column, rank)
    new, row, column = rotate_2(new, row, column, rank)
    new = rotate_3(new, row, column, rank)
    return new
    
def rotate_1(row, column, rank):
    new = []
    if(rank.count('1')==3):
        new = column[::-1]
        row, column = reset(new)
    elif(rank.count('1')==2):
        new = list(reversed(row))
        for i in range(len(new)):
            new[i].reverse()
        row, column = reset(new)
    elif(rank.count('1')==1):
        new = list(map(list, zip(*row[::-1])))
        row, column = reset(new)
    return new, row, column

def rotate_2(new, row, column, rank):
    if(rank.count('2')==3):
        new = list(map(list, zip(*row[::-1])))
        row, column = reset(new)
    elif(rank.count('2')==2):
        new = list(reversed(row))
        for i in range(len(new)):
            new[i].reverse()
        row, column = reset(new)
    elif(rank.count('2')==1):
        new = column[::-1]
        row, column = reset(new)
    return new, row, column

def rotate_3(new, row, column, rank):
    if(len(new)==0):
        new.extend(row)
    if(rank.count('3')==1):
        new = row[::-1]
        for i in range(len(new)):
            new[i].reverse()
        row, column = reset(new)
    return new

def reset(new):
    row = []
    row.extend(new)
    column = []
    column = list(map(list, zip(*row)))
    return row, column

def output(new):
    for i in new:
        for j in i:
            print(j, end='')
        print()
main()