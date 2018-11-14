def computescore(csi, pd, chinese):
    average = (csi + pd + chinese) //3
    total = csi + pd + chinese
    return average, total


	
def main():
    name = input()
    id = int(input())
    csi = int(input())
    pd = int(input())
    chinese = int(input())
    average, total = computescore(csi, pd, chinese)
    print('Name:%c' %name)
    print('ID:%d' %id)
    print('Average:%d' %average)
    print('Total:%d' %total)

	
main()