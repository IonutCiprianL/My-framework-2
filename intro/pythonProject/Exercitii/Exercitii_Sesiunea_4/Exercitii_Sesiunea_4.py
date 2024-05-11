# SESIUNEA 4
print()
# Exercitiul 1  - Lista
print('Exercitiul 1  - Lista')

lista1 = [4, 5, 6]
# Lista este o structura ordonata deoarece pastreaza elementele in ordinea in care au fost adaugate.
print(f'Lista contine elementele {lista1}.')
print(f'Al doilea element din lista este {lista1[1]}.')
print(f'Lungimea listei este de {len(lista1)} elemente.')

print()
# Exercitiul 2  - Lista
print('Exercitiul 2  - Lista')
filme_preferate = ['Yes man','Gran Torino','K-PAX']
print(f'Lista contine elementele {filme_preferate}.')
print(f'Lista inversata este     {filme_preferate[::-1]}.')
if len(filme_preferate) == 0 :
    print(f'Lista este goala.')
else:
    print(f'Lista are {len(filme_preferate)} elemente.')

print()
# Exercitiul 3  - Lista
print('Exercitiul 3  - Lista')
cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
print(f'Structura este de tipul {type(filme_preferate)}.')
print(f'Lista are structura : {cifre}')
cifre.sort()
print(f'Lista sortata are structura : {cifre}')
if cifre.count(9) == 1 :
    print(f'Cifra 9 se afla in lista.')
else:
    print(f'Cifra 9 nu se afla in lista.')

print()
# Exercitiul 4  - Lista
print('Exercitiul 4  - Lista')

cifre.append(9)
print(f'Listei i s-a adaugat cifra 9 la sfarsit {cifre}')
cifre.clear()
print(f'Listei i s-au sters elementele {cifre}')
print()
cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
print(f'Lista are structura : {cifre}')
cifre.insert(0,9)
print(f'Listei i s-a adaugat cifra 9, la index 0 {cifre}')
print(f'Cifra 5 se afla in lista la indexul {cifre.index(5)}.')
cifre.pop(0)
print(f'Listei i s-a sters cifra 9, de la index 0 {cifre}')
cifre.reverse()
print(f'A fost inversata ordinea listei {cifre}')
cifre.extend(filme_preferate)
print(f'Listei cifre i s-au adaugat elementele listei filme_preferate {cifre}')

print()
# Exercitiul 5  - Dictionar
print('Exercitiul 5  - Dictionar')
student1 ={'nume':'Marin',
           'prenume':'Angela',
           'varsta':35,
           'an_studiu':3,
           'facultate':'arheologie',
           'medie':9.90
           }
print(f'Dictionarul are continutul {student1}')
print(f'Lungimea dictionarului este {len(student1)}')
print(f'Numele studentului este {student1['nume']}')
print(f'Prenumele studentului este {student1['prenume']}')
student1["tara_studiu"]="Egipt"
print(f'Dictionarului i s-a adaugat țara în care studiază studentul {student1}')
student1.update({"oras_studiu":"Cairo"})
print(f'Dictionarului i s-a adaugat orasul în care studiază studentul {student1}')
if "oras_studiu" in student1 :
    print(f'Orasul exista in dictionar si are continutul {student1['oras_studiu']}')

print()
# Exercitiul 6  - Dictionar
print('Exercitiul 6  - Dictionar')
reteta = {'nume_reteta':'nume',
          'ingrediente_reteta':'ingrediente',
          'timp_preparare':'timp'}

reteta['nume_reteta'] = input('Numele retetei : ')
reteta['ingrediente_reteta'] = input('Ingredientele retetei : ')
reteta['timp_preparare'] = input('Timp de preparare (min) : ')
print(f'Dictionarul are continutul {reteta}')
reteta['nume_reteta'] = reteta['nume_reteta'].upper()
print(f'Numele retetei cu majuscule este : {reteta['nume_reteta']}')

print()
# Exercitiul 7  - Dictionar
print('Exercitiul 7  - Dictionar')
contacte = {'Maria':'0722898956',
            'Aurel': '0755342298'}
print(f' Lista contine urmatoarele contacte : {contacte}')
contacte['Aurel'] = '0722222222'
print(f' Aurel si-a schimbat numarul de telefon : {contacte}')
del contacte['Maria']
print(f'Numarul de telefon al Mariei a fost stears din lista : {contacte}')
if 'Mihaela' in contacte :
    print (f'Mihaela este in lista de contacte.')
else:
    print(f'Mihaela nu este in lista de contacte.')

print()
# Exercitiul 8  - Set
print('Exercitiul 8  - Set')
my_set = {1, 2, 3, 4}
print(f'Setul contine : {my_set}')
my_set.add(5)
print(f'A fost adaugat 5 : {my_set}')
my_set.add(6)
print(f'A fost adaugat 6 : {my_set}')
my_set.add(1)
print(f'A fost adaugat 1 : {my_set}') # valoarea listei se pastreaza
my_set.remove(6)
print(f'A fost sters 6 : {my_set}')
my_set.pop()
print(f'A fost sters primul element : {my_set}')


print()
# Exercitiul 9  - Tuplu
print('Exercitiul 9  - Tuplu')
locatie = (44.34, 12.456)
print(f'Tipul structurii este : {type(locatie)}')
# Structura pastreaza ordinea elementelor in care au fost adaugate.
# Structura este imutabila
print(f'Setul are lungimea : {len(locatie)}')
b = locatie[1]
if b > 13 :
    print (f'A doua valoare din tuplu este mai mare decat 13, are valoarea  : {locatie[1]}')
else:
    print(f'A doua valoare din tuplu este mai mic decat 13, are valoarea : {locatie[1]}')