def bmi(weight, height):
    BMI = weight / (height*height)
    return BMI
	
def main():
    height = float(input())
    weight = float(input())
    BMI = bmi(weight, height)
    print('%.1f' %BMI)
	
main()