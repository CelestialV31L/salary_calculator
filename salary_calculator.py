#!/usr/bin/env python3
try:
    hourly = float(input("Enter in hourly wage: $"))
    if hourly < 0:
        raise ValueError("Hourly wage must be a positive number.")
except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number for the hourly wage.")

biweekly = hourly * 80
salary = biweekly * 26
print(f"Before taxes, your salary is ${round(salary, 2):,}")

standard_deduction = 14600
taxable_salary = salary - standard_deduction

if salary <= 11600:
   tax = "You owe nothing in federal taxes."
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
