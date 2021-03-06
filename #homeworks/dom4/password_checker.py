
# # Napisz program, który jako dane wejściowe przyjmuje hasło od użytkownika i sprawdza
# poprawność hasła względem poniższym kryteriów:
# a. Conajmniej jedna mała litera
# b. Conajmniej jedna cyfra
# c. Conajmniej jedna wielka litera
# d. Conajmniej jeden znak specjalny np. - @ #
# e. Minimalna długość hasła 8 znaków
# f. Maksymalna długość hasła 64 znaki (aby nikt nie wkleił całej treści Pana
# Tadeusza ;) )

import re
import string

print('Program sprawdza poprawność hasła względem poniższym kryteriów')
print('a. Conajmniej jedna mała litera')
print('b. Conajmniej jedna cyfra')
print('c. Conajmniej jedna wielka litera')
print('d. Conajmniej jeden znak specjalny np. - @ #')
print('e. Minimalna długość hasła 8 znaków')
print('f. Maksymalna długość hasła 64 znaki')

while True:
    password = input("Podaj hasło do sprawdzenia: ")
    flag = 0

    if (len(password) < 8):
        flag = -1
        print("hasło za krótkie - Minimalna długość hasła 8 znaków")
    if (len(password) > 64):
        flag = -1
        print("hasło za długie - Maksymalna długość hasła 64 znaki")
    if not re.search("[a-z]", password):
        flag = -1
        print("Hasło nie zawiera conajmniej jednej małej litery")
    if not re.search("[A-Z]", password):
        flag = -1
        print("Hasło nie zawiera conajmniej jednej wielkiej litery")
    if not re.search("[0-9]", password):
        flag = -1
        print("Hasło nie zawiera conajmniej jednej cyfry")
    if not re.search('['+string.punctuation+']', password):
        flag = -1
        print("Hasło nie zawiera znaku specjalnego")
    if flag < 0:
        print("Hasło niepoprawne")
    else:
        flag = 0
        print("Hasło poprawne")
        break