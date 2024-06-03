from winsound import Beep  # se importa modulul pentru generare sunete
import random # se importa modulul pentru generare numere pseudoaleatoare
from time import sleep # se importa modulul pentru functia pauza
print()

# se definesc si atribuie variabilele de viteza in semne/min, numarul de semne transmise si frecventa sunetelor in Hz
viteza = 45
grupa = 5
ton = 700
semne_aleatoare=True # la valoarea True se genereaza numere aleatoare, iar la valoare False transmite text predefinit
viteza2= int(5350/viteza) # este definita valoarea variabilei viteza2 prin raportul cu variabila viteza
slp1= viteza2/2000 # este definita valoarea variabilei slp1 prin raportul variabilei viteza2
slp2=viteza2/250 # este definita valoarea variabilei slp2 prin raportul variabilei viteza2

# se atribuie dictului cheile cu valorile aferente codului Morse
semne= {'a' :'13',
        'b':'3111',
        'c':'3131',
        'd':'311',
        'e':'1',
        'f':'1131',
        'g':'331',
        'h':'1111',
        'i':'11',
        'j':'1333',
        'k':'313',
        'l':'1311',
        'm':'33',
        'n':'31',
        'o':'333',
        'p':'1331',
        'q':'3313',
        'r':'131',
        's':'111',
        't':'3',
        'u':'113',
        'v':'1113',
        'w':'133',
        'x':'3113',
        'y':'3133',
        'z':'3311',
        '1':'13333',
        '2':'11333',
        '3':'11133',
        '4':'11113',
        '5':'11111',
        '6':'31111',
        '7':'33111',
        '8':'33311',
        '9':'33331',
        '0':'33333',
        '?':'113311',
        '=':'31113',
        '/':'31131'}

print() # se printeaza un rand liber
print(f'viteza = {viteza} semne / min') # se printeaza valoarea vitezei
print(f'grupa de {grupa} semne') # se printeaza valoarea variabilei grupa
if semne_aleatoare==True:
    print('Se transmite text cu semne aleatoare. Pentru text predefinit seteaza variabila semne_aleatoare = False')
    print()
if semne_aleatoare==False:
    print('Se transmite text predefinit. Pentru text cu semne aleatoare seteaza variabila semne_aleatoare = True')
    print()




def transmisie():  # este definita functia transmisie

    print(cheie, end=" ")
    j = len(cm)  # variabilei j i se atribuie valoarea lungimii continutului din variabila cm

    for i in range(j):
            sleep(slp1)  # pauza in functie de valoarea slp1
            Beep(ton, int(cm[i])*viteza2) # fiecare element al valorii din variabila tip string cm este transformat in sunet


if semne_aleatoare==False:
    text=input('Scrie textul de transmis : ')
    jj = len(text)
    if jj > 250 :
        print('Textul este mai lung de 250')
    else:
        print(f'Textul are ',jj," semne")
print()


input('Pentru START apasa tasta ENTER.') # calculatorul asteapta comanda de START prin actionarea tastei ENTER
print()


print(f'Atentie ! Dupa seria de V-uri urmeaza textul. ', end="")
sleep(3)
for iii in range(3):
        cheie = 'v'
        cm = '1113'
        transmisie()
print()
sleep(1)


if semne_aleatoare==False:
    for ii in range(jj):
        cheie = text[ii]
        sleep(slp2)
        for key, semnal in semne.items():
             if cheie == key:
                cm = semnal
                transmisie()



if semne_aleatoare==True:
    for iiii in range (grupa):

        aleator = random.randint(0, len(semne) - 1)  # se genereaza o valoare pseudoaleatoare
        cheie = list(semne.keys())[aleator]  # se identifica cheia din dict cu numarul echivalent celui aleator si se atribuie valoarea variabilei cheie.
        sleep(slp2)
        for key, semnal in semne.items():
             if cheie == key:
                 cm = semnal
                 transmisie()