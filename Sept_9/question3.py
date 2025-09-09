# 3.	Ask the user for an integer between 0 and 1000 and add up all the digits and display the sum. For example, if the integer is 423, the sum of the digits is 9
number = int(input("Enter an integer berween 0 and 1000: "))
sum_of_digits = (number // 1000) + ((number % 1000)//100) + ((number % 100)//10) + (number % 10)
print (f"Sum of digits: {sum_of_digits}")
