import re

a = re.split('[a-f]+', '0a3B9', flags=re.I)
print(''.join(a))
