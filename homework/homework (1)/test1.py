def computescore(csi, pd, chinese): #計算成績 總平均, 總分
    average = (csi + pd + chinese) //3
    total = csi + pd + chinese
    return average, total
	
def main(): #main
    name = input()
    id = int(input())
    csi = int(input())
    pd = int(input())
    chinese = int(input())
    average, total = computescore(csi, pd, chinese)
    output(name, id, average, total)

def output(name, id, average, total): #輸出
    print('Name:%c' %name)
    print('ID:%d' %id)
    print('Average:%d' %average)
    print('Total:%d' %total)

	
main()