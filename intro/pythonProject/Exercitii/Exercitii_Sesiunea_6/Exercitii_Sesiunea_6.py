# SESIUNEA 6

print()
# Exercitiul 1  - While
print('Exercitiul 1  - While')
x = -5
while x < 0 :
    print(f'x = : {x}')
    x += 1
else:
    print(f'Au fost afisate toate numerele negative.')

print()
# Exercitiul 2  - While
print('Exercitiul 2  - While')

b = 0
c = 0
i = 0

while b != -1 :
    b = float(input("Scrie nota (cu -1 se incheie seria de note) : "))

    if b > -1 :
            c += b  # variabilei c se aduna valoarea variabilei b
            i += 1

else :
    print(f'Media notelor este : {c/i}')


print()
# Exercitiul 3  - For,  For else
print('Exercitiul 3  - For,  For else')


for i in range (1, 10+1):
    if i % 2 == 0 and i > 0 :
        print (f'i = {i}')

print()
# Exercitiul 4  - For,  For else
print('Exercitiul 4  - For,  For else')
i = 0
legume = ['spanac', 'castraveti', 'conopida', 'ardei']
for i in range(len(legume)) :
    print(f'Elementul cu indexul {i} : {legume[i]}')

produse = [
    {'nume produs':'rosii','pret':5
     },
    {'nume produs':'paine','pret':8
     },
    {'nume produs':'lapte','pret':6
     },
    {'nume produs':'cafea'
     }
]
print()
# Exercitiul 5  - For,  For else
print('Exercitiul 5  - For,  For else')
j=1
print('Produse cu valoarea mai mare de 5 lei :')
for i in range(len(produse)): # pentru valori ale lui i pana la valoarea lungimii listei produse
    if len(produse[i])==2 : # daca elementul i din lista produse are 2 elemente atunci executa urmatoarele instructiuni
        if produse[i]['pret'] > 5 : # daca elementul i din lista produse are pretul mai mare decat 5 atunci executa urmatoarele
            print(f'{j}. pret {produse[i]['nume produs']} : {produse[i]['pret']} lei')
            j += 1

print()
# Exercitiul 6  - Break
print('Exercitiul 6  - Break')

for i in range (1, 10+1):
    if i % 2 == 0 :
        print(f'Primul numar par din intervalul (1 - 10) este : {i}')
        break

print()
# Exercitiul 7  - Break
print('Exercitiul 7  - Break')
participanti = ['Maria', 'Ionela', 'Marius', 'Paul']
for i in range(len(participanti)):
    if participanti[i] == 'Marius':
        print('Marius este in lista.')
        break

print()
# Exercitiul 8  - Continue
print('Exercitiul 8  - Continue')
numere = [1, 2, 3, 4, 5, 6, 7]
print(numere)
print('Lista fara cifrele 3 si 5 este : ', end="")
for i in range(len(numere)):
    if numere[i]==3 or numere[i]==5:
        continue
    print(numere[i], end=" ")