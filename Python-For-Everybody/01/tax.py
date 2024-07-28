tax_rate = 0.2
std_deduction = 10000
dependent_deduction = 3000

gross_income = float(input('Enter gross income = '))
dependents = int(input('Enter no of dependents = '))

taxable_income = gross_income - std_deduction - dependent_deduction*dependents
income_tax = taxable_income*tax_rate

print('Income tax = ',income_tax)
print('income tax = ',str(income_tax))
print('income tax = {}'.format(income_tax))