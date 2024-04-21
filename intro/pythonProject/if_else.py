

muzica_faina= False

print('Pornesc radioul')

if muzica_faina== True :
    print('Dau radioul mai tare')
    print('Fredonez')
print('Opresc radioul')



a = 4
if a % 2 == 0: # daca restul impartirii la 2 este 0, atunci
    print('numar par') # scrie "numar par"
if a % 2 != 0: # daca restul impartirii la 2 este diferit de 0, atunci
    print('numar impar') # scrie "numar impar"


a = 5
if a % 2 == 0: # daca restul impartirii la 2 este 0, atunci
    print('numar par') # scrie "numar par"
else :
    print('numar impar') # altfel scrie "numar impar"

a = 8

if a > 0 :
    print('numar pozitiv')
else:
    print('numarul nu este pozitiv')


ora=input('Scrie ora : ') # se introduc date tip string de la tastatura
print(ora)

# if, else if, else/

ora=int(input('Scrie ora : ')) # se introduc date integer de la tastatura

if ora <0:
    print('Ora negativa')
elif ora <=11 :
    print('Buna dimineata !')
elif ora <= 18 :
    print ('Buna ziua')
elif ora <=21 :
    print('Buna seara')
elif ora <=24 :
    print('Noapte buna')
else :
    print('Ora este prea mare')


#  CTRL + /  decomenteaza / recomenteaza


optiune= int(input('Alege o optiune'))
if optiune==0 :
    print('Meniu anterior')
elif optiune== 1:
    print('Ati ales limba romana')
elif optiune==2:
    print('Ati ales limba engleza')
else:
    print('Nu am identificat optiunea. Mai incercati')

