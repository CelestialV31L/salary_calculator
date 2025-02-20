#!/usr/bin/env python3
hourly = float(input("Enter in hourly wage: $"))
biweekly = hourly * 80
salary = biweekly * 26
print(f"Before taxes, your salary is ${round(salary, 2):,}")
if salary <= 11600:
    tax = salary * .10
elif salary <= 47150:
    tax = 1160 + .12 * (salary - 11600)
elif salary <= 100525:
    tax = 5426 + .22 * (salary - 47150)
elif salary <= 191950:
    tax = 17168.5 + .24 * (salary - 100525)
elif salary <= 243725:
    tax = 39110.5 + .32 * (salary - 191950)
elif salary <= 609350:
    tax = 55678.5 + .35 * (salary - 243725)
else:
    tax = 183647.25 + .37 * (salary - 609350)
print(f"You pay ${round(tax, 2):,} in federal income taxes.")
net = salary - tax
print(f"After taxes, your salary is ${round(net, 2):,}")
