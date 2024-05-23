# Q1 Task 1

number = float(input("Enter a number: "))  # Ensure numerical input

if number > 0:
    print("The number is positive.")
elif number == 0:  # Use == for equality check
    print("The number is zero.")
else:
    print("The number is negative.")

2. The Greatest Showdown

#Task 1

# Get user input for the three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number using conditional statements
if num1 >= num2 and num1 >= num3:
    largest_number = num1
elif num2 >= num1 and num2 >= num3:
    largest_number = num2
else:
    largest_number = num3

# Print the largest number
print("The largest number is:", largest_number)

#Task 2

# Get user input for the three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest and smallest numbers
largest_number = max(num1, num2, num3)
smallest_number = min(num1, num2, num3)

# Print the results
print("The smallest number is:", smallest_number)
print("The largest number is:", largest_number)


#Task 3 Equality Check

Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".

Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. There are two numbers equal to each other." Printing out which numbers are equal would be a great added bonus.

# Q3 Task 1

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Get user input for the year
try:
    user_year = int(input("Enter a year: "))
    if is_leap_year(user_year):
        print(f"{user_year} is a leap year.")
    else:
        print(f"{user_year} is not a leap year.")
except ValueError:
    print("Invalid input. Please enter a valid year (e.g., 2000).")
