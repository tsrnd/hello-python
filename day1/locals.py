var = "nghia"
print(var)
del var
if 'var' in locals():
    print('can not delete var')
else:
    print('var was deleted')