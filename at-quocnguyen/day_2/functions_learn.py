def add_number():
    first_number = 2
    second_number = 4
    total = first_number + second_number
    return (total)
print (add_number())


#  assigning a default value to parameter

def calc_tax(sale_total = 1001.2, tax_rate = 0.55):
    return sale_total * tax_rate

print (calc_tax())