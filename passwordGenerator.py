import random
import string

minCount = 2
maxCount = 6

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetCaps = alphabet.upper()
numbers = '1234567890'
symbols = '!@#$%^&*()' 

password = ''

alphaCount = random.randint(minCount, maxCount)
alphaCapsCount = random.randint(minCount, maxCount)
numCount = random.randint(minCount, maxCount)
symCount = random.randint(minCount, maxCount)

for x in range(alphaCount):
	password += random.sample(alphabet, 1).pop()

for x in range(alphaCapsCount):
	password += random.sample(alphabetCaps, 1).pop()

for x in range(numCount):
	password += random.sample(numbers, 1).pop()
	
for x in range(symCount):
	password += random.sample(symbols, 1).pop()	

shuffled = ''.join(random.sample(password, len(password)))
print('Your new password is:')
print(shuffled)

try:
	import pyperclip
	pyperclip.copy(shuffled)
	print('Password copied to clipboard')
except ImportError:
	print ('Pyperclip not installed - password not copied to clipboard')