#!/usr/bin/env python3
hourly = None
attempts = 0
max_attempts = 3

while hourly is None:
    try:
        hourly = float(input("Enter in hourly wage: $"))
        if hourly < 0:
            hourly = None
            raise ValueError("Hourly wage must be a positive number") 
    except ValueError as e:
        attempts += 1
        print(f"Invalid input: {e}. Please enter a valid number for the hourly wage.")
        if attempts == max_attempts:
            print("Maximum attempts reached. Exiting.")
            exit()

salary = hourly * (80 * 26)
print(f"Before taxes, your salary is ${round(salary, 2):,}")

standard_deduction = 14600

if salary >= 14600:
    taxable_salary = salary - standard_deduction
    print(f"Your taxable income is ${round(taxable_salary, 2):,} after the standard deduction.")
else:
    print("Your income is not taxable as it is below the maximum for the standard deductible.")
    exit()

if salary <= 11600:
   tax = 0
   # tax = salary * .10
elif salary <= 47150:
    tax = .12 * (salary - standard_deduction)
elif salary <= 100525:
    tax = 3906 + .22 * (salary - 47150)
elif salary <= 191950:
    tax = 15648.5 + .24 * (salary - 100525)
elif salary <= 243725:
    tax = 37590 + .32 * (salary - 191950)
elif salary <= 609350:
    tax = 54158 + .35 * (salary - 243725)
else:
    tax = 182126.75 + .37 * (salary - 609350)
print(f"You pay ${round(tax, 2):,} in federal income taxes.")
net = salary - tax
print(f"After taxes, your salary is ${round(net, 2):,}")
