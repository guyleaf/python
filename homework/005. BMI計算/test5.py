def bmi(weight, height): #BMI計算
    BMI = weight / (height*height)
    return BMI
	
def main(): #main
    height = float(input())
    weight = float(input())
    BMI = bmi(weight, height)
    print('%.1f' %BMI)
	
main()