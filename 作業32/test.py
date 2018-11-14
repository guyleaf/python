row = [[1,2,3],[4,5,6],[7,8,9]]
st = list(map(list, zip(*row)))
print(st)