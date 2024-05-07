# SESIUNEA 2

print()
# Exercitiul 1 - String slicing
print('Exercitiul 1 - String slicing')
prop3="Concertul va avea loc maine." # se defineste si atribuie stringul prop3.
var1 = prop3[0:9] # se salveaza primul cuvant in variabila var1 folosind slicing.
print(var1)
var2 = prop3[0:3] # se extrag primele trei caractere din prop3.
print(var2)
print(prop3[::-1]) # Se afiseaza prop3 cu caracterele inversate.


print()
# Exercitiul 2 - Metode ajutatoare string
print('Exercitiul 2 - Metode ajutatoare string')
my_str = 'vacanta'
print(my_str.find('a')) # se printeaza primul index la care se gaseste litera a.
print(my_str.count('a')) # se printeaza de cate ori se gaseste litera a in cuvantul 'vacanta'.
print(my_str.capitalize()) # se printeaza cuvantul 'vacanta' cu prima litera mare.
print(my_str.upper()) # se printeaza cuvantul 'vacanta' cu litere mari.

print()
# Exercitiul 3 - Metode ajutatoare string
print('Exercitiul 3 - Metode ajutatoare string')
print(my_str.endswith('a')) # daca cuvantul vacanta din variabila my_str se termina cu litera 'a', se afiseaza valoarea True
var3 = my_str.endswith('a') # se atribuie valoarea True variabilei var3.
print(var3)
print(my_str.index('t')) # se afiseaza indexul 5 al literei 't' din cuvantul 'vacanta'
var4 = 'VACANTA'
print(var4.lower()) # se afiseaza continutul variabilei var4, cu litere mici
var4 = var4.replace('VACANTA', 'concediu') # se inlocuieste continutul variabilei var4
print(var4)
print(my_str.strip('va')) # se elimina prima si ultima litera din cuvantul 'vacanta'.


print()
# Exercitiul 4 - Operatori aritmetici
print('Exercitiul 4 - Operatori aritmetici')
a = 10
b = 2

print (f'a + b = {a+b}')
print (f'a - b = {a-b}')
print (f'a * b = {a*b}')
print (f'a / b = {a/b}')
print (f'a / b, rest = {a%b}')
print (f'a la puterea b = {a**b}')
print (f'a floor division b = {a//b}')

var5 = ' si '
print(my_str + var5 + var4) # rezultatul este 'vacanta si concediu'
print(var5*3) #  si  si  si


print()
# Exercitiul 5 - Operatori logici
print('Exercitiul 5 - Operatori logici')
  # Exemplul 1:
a = True
b = False
print(f'a este {a}')
print(f'b este {b}')
print(f'not(a) este {not(a)}') # not(a) returneaza opusul valorii initiale a lui a, adica False
print(f'not(b) este {not(b)}') # not(b) returneaza opusul valorii initiale a lui b, adica True


print()
  # Exemplul 2:
a = True
b = False
print(f'a este {a}')
print(f'b este {b}')
x = not(a)
y = not(b)
print(f'x = not(a) = {x}')
print(f'y = not(b) = {y}')
print(f'a or b este {a or b}') # True, daca a sau b este adevarat
print(f'x or y este  {x or y}')# True , daca x sau y este adevarat
print(f'a or x este {a or x}') # True, daca a sau x este adevarat
print(f'x or b este {x or b}') # False, daca nici x si nici b nu sunt adevarate

print()
  # Exemplul 3:
a = False
b = False
print(f'a este {a}')
print(f'b este {b}')
x = not(a) # x este True
y = not(b) # y este True
print(f'x = not(a) = {x}')
print(f'y = not(b) = {y}')
print(f'a and b {a and b}') # False, daca a si b nu sunt adevarate
print(f'a and x {a and x}') # False, daca a si x nu sunt adevarate
print(f'y and b {y and b}') # False, daca y si b nu sunt adevarate
print(f'x and y {x and y}') # True, daca x si y sunt adevarate


print()
# Exercitiul 6  Operatori de comparare
print('Exercitiul 6 - Operatori de comparare')
num = 12
print(f'12 este numar pozitiv ? : {num >= 0}') # returneaza True, 12 este un numar pozitiv
print(f'12 este mai mare decat 5 ? : {num > 5}') # returneaza True, 12 este mai mare decat 5
print(f'12 este mai mic decat 25 ? : {num < 25}') # returneaza True, 12 este mai mic decat 25
print(f'12 este intre 0 si 20 ? : {num > 0 and num <20 }') # returneaza True, 12 este intre 0 si 20


print()
# Exercitiul 7 - If
print('Exercitiul 7 - If')
varsta = 18

if varsta >= 18 :
    print('Persoana are ',varsta,' ani, este majora.')
if varsta < 18 :
    print('Persoana are ',varsta,' ani, nu este majora.')


print()
# Exercitiul 8 - If
print('Exercitiul 8 - If')
pret = 80
if pret <= 100 :
    print(f'',pret,' : Pretul pe care l-ati introdus este mai mic sau egal cu 100 dolari.')


print()
# Exercitiul 9 - If - else
print('Exercitiul 9 - If - else')
var6 = float(input('Introduceti un numar : '))
if var6 % 2 == 0 :
    print('Numarul este par.')
else:
    print('Numarul este impar.')


print()
# Exercitiul 10 - If - else
print('Exercitiul 10 - If - else')
viteza = float(input('Introdu viteza medie a autovehiculului : '))
if viteza <= 50 :
    print('Viteza normala')
else:
    print('Viteza depasita')


print()
# Exercitiul 11 - If, elif, else
print('Exercitiul 11 - If, elif, else')
varsta = float(input('Introduceti varsta dvs : '))
if varsta < 18 :
    print('Varsta 0 - 18 ani : minor')
elif varsta <= 65 :
        print ('Varsta intre 18 - 65 ani : adult')
else:
        print('Peste 65 de ani : senior')


print()
# Exercitiul 12 - If, elif, else
print('Exercitiul 12 - If, elif, else')

valoare_cumparaturi = float(input('Introduceti valoarea totala a cumparaturilor : '))
def total_plata():
    print (f'Ati efectuat cumparaturi in valoare de : {valoare_cumparaturi} lei.')
    print(f'Reducere : {procente} %, adica {valoare_cumparaturi*procente/100} lei.')
    print(f'Rest de plata : {(valoare_cumparaturi-(valoare_cumparaturi*procente/100))} lei.')

if valoare_cumparaturi > 400 :
    procente =30
    total_plata()

elif valoare_cumparaturi > 300 :
    procente = 20
    total_plata()

elif valoare_cumparaturi > 200:
    procente = 15
    total_plata()

elif valoare_cumparaturi > 100:
    procente = 10
    total_plata()

else :
    procente = 0
    total_plata()


print()
# Exercitiul 13 - Nested ifs
print('Exercitiul 13 - Nested ifs')
ore_lucrate = float(input('Introduceti numarul de ore lucrate : '))

def plata_ore():
    print (f'Angajatul a efectuat {ore_lucrate} ore de lucru.')
    print(f'Bonus pentru ore suplimentare : {bonus} lei.')

if ore_lucrate > 50 :
    bonus = 100
    plata_ore()
else:
      if ore_lucrate > 40:
         bonus = 50
         plata_ore()
      else:
          bonus = 0
          plata_ore()


print()
# Exercitiul 14 - Nested ifs
print('Exercitiul 14 - Nested ifs')
varsta = float(input('Introduceti varsta : '))
cetatenie = input('Aveti cetatenie romana ? ( DA / NU) : ')

if varsta >= 18 :
                if cetatenie == 'da' or cetatenie =='DA' or cetatenie=='Da' or cetatenie=='dA':
                             print('Aveti drept de vot.')
                else:
                    print('Nu aveti drept de vot.')
else:
    print('Nu aveti drept de vot.')



