# 4.	Ask the user for a number of seconds. Print the number of minutes and seconds that make of that number of seconds.

total_seconds = int(input("Total seconds: "))
minutes = total_seconds // 60
seconds = total_seconds % 60

print (f"{minutes} minute(s) and {seconds} second(s)")