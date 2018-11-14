import math
def add(num1, num2):
    sum = num1 + num2
    return sum
	
def subtract(num1, num2):
    if num1 >= num2:
        difference = num1 - num2
    else:
        difference = num2 - num1

    return difference
	
def multiply(num1, num2):
    product = num1 * num2
    return product
	
def divide(num1, num2):
    quotient = num1 / num2
    return quotient
	
def main():
    num1 = int(input())
    num2 = int(input())
    sum = add(num1, num2)
    difference = subtract(num1, num2)
    product = multiply(num1, num2)
    quotient = divide(num1, num2)
    print('Difference:%.2f' %difference)
    print('Sum:%.2f' %sum)
    print('Quotient:%.2f' %quotient)
    print('Product:%.2f' %product)
	
main()