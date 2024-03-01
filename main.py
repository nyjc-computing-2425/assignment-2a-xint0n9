num = input('Enter a number (decimal or integer): ')
num = num.strip()
numm = num.replace(".","")
numm = numm.lstrip("0")
sf = len(numm)
# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
