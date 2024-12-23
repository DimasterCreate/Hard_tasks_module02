import random
from random import randint

first_number = randint(3, 20)
result = []
for j in range(1, 21):
    for k in range(1, 21):
        summa = j + k
        if first_number % summa == 0:
            if j != k and j < k:
                result.append(f'{j}' + f'{k}')

password = ''.join(result)

print("Число из первой вставки: ", first_number)
print("Пароль: ", password)