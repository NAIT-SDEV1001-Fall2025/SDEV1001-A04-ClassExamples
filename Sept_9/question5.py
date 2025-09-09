# 5.	Ask the user for a currency amount and display the number of quarters, dimes, nickels and pennies total that amount.

amount = float(input("Enter an amount: "))
cents = int(amount * 100)
quarters = cents // 25
remainder = cents % 25
dimes = remainder // 10
remainder = remainder % 10
nickels = remainder // 5
pennies = remainder % 5

print (f"Quarters: {quarters}")
print (f"Dimes: {dimes}")
print (f"Nickels: {nickels}")
print (f"Pennies: {pennies}")
