import string
import secrets
import random
from math import log2


simbols = []
long = int(input('Введите желаемую длину пароля: '))
upper = input('A-Z?  y/n ')
lower = input('a-z?  y/n ')
dig = input('0-9?  y/n ')
punct = input('#$%?  y/n ')


count = 0

while count == 0:
    if upper == 'y':
        simbols.append(string.ascii_uppercase)
    
    if lower == 'y':
        simbols.append(string.ascii_lowercase)
    
    if dig == 'y':
        simbols.append(string.digits)
    
    if punct == 'y':
        simbols.append(string.punctuation)
    
    if upper == 'n' and lower == 'n' and dig == 'n' and punct == 'n':
        exit()

    count += 1

simbols = ''.join(simbols)

entropyText = ''
entropy = round(log2(len(simbols)) * long, 2)
if entropy <= 30:
    entropyText = 'Придумай получше'
elif entropy > 30 and entropy <= 60:
    entropyText = 'Сойдет'
elif entropy > 60 and entropy <= 90:
    entropyText = 'Хороший'
elif entropy > 90:
    entropyText = 'Замечательный'


password = ''.join(secrets.choice(random.choices(simbols)) for i in range(long))
print(password)
print( str(entropy) + ' ' + entropyText ) 