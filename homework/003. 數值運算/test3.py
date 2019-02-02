"""
003. 數值運算
分別輸入 num1 num2 求出兩數的 Sum,Difference,Product,Quotient。
結果須輸出到小數點第二位
print("%.2f" %x1);

輸入:
25
2

輸出:
Difference:23.00
Sum:27.00
Quotient:12.50
Product:50.00
"""

import math
def add(num1, num2): #加法
    sum = num1 + num2
    return sum
	
def subtract(num1, num2): #減法
    if num1 >= num2:
        difference = num1 - num2
    else:
        difference = num2 - num1
    return difference
	
def multiply(num1, num2): #乘法   
    product = num1 * num2
    return product
	
def divide(num1, num2): #除法
    quotient = num1 / num2
    return quotient
	
def main(): #main
    num1 = int(input())
    num2 = int(input())
    sum = add(num1, num2)
    difference = subtract(num1, num2)
    product = multiply(num1, num2)
    quotient = divide(num1, num2)
    output(sum, difference, product, quotient)

def output(sum, difference, product, quotient): #輸出
    print('Difference:%.2f' %difference)
    print('Sum:%.2f' %sum)
    print('Quotient:%.2f' %quotient)
    print('Product:%.2f' %product)
	
main()