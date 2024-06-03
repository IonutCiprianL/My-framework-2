from winsound import Beep  # se importa modulul pentru generare sunete
import random  # se importa modulul pentru generare numere pseudoaleatoare
from time import sleep  # se importa modulul pentru functia pauza

print()

# se definesc si atribuie variabilele de viteza in semne/min, numarul de semne transmise si frecventa sunetelor in Hz
viteza = 40


ton = 700
cheie_memorata = []
cm_memorat = []
spatiu = 0
d = 'd'
dd = 'd'
semne_aleatoare = False
lungime_text_aleator = 0



# la valoarea True se genereaza numere aleatoare, iar la valoare False transmite text predefinit
viteza2 = int(5350 / viteza)  # este definita valoarea variabilei viteza2 prin raportul cu variabila viteza
slp1 = viteza2 / 2000  # este definita valoarea variabilei slp1 prin raportul variabilei viteza2
slp2 = viteza2 / 250  # este definita valoarea variabilei slp2 prin raportul variabilei viteza2
text_memorat = 0

# se atribuie dictului cheile cu valorile aferente codului Morse
semne = {'a': '13',
         'b': '3111',
         'c': '3131',
         'd': '311',
         'e': '1',
         'f': '1131',
         'g': '331',
         'h': '1111',
         'i': '11',
         'j': '1333',
         'k': '313',
         'l': '1311',
         'm': '33',
         'n': '31',
         'o': '333',
         'p': '1331',
         'q': '3313',
         'r': '131',
         's': '111',
         't': '3',
         'u': '113',
         'v': '1113',
         'w': '133',
         'x': '3113',
         'y': '3133',
         'z': '3311',
         '1': '13333',
         '2': '11333',
         '3': '11133',
         '4': '11113',
         '5': '11111',
         '6': '31111',
         '7': '33111',
         '8': '33311',
         '9': '33331',
         '0': '33333',
         '?': '113311',
         '=': '31113',
         '/': '31131'}

print()  # se printeaza un rand liber
print(f'viteza = {viteza} semne / min')  # se printeaza valoarea vitezei


def transmisie():  # este definita functia transmisie

    print(cheie.upper(), end=" ")  # se tiparesc majuscule

    j = len(cm)  # variabilei j i se atribuie valoarea lungimii continutului din variabila cm

    for i in range(j):
        sleep(slp1)  # pauza in functie de valoarea slp1
        Beep(ton,int(cm[i]) * viteza2)  # fiecare element al valorii din variabila tip string cm este transformat in sunet


def memorare():
    cheie_memorata.append(cheie)
    cm_memorat.append(cm)


def serieV():
    print(f'Atentie ! Dupa seria de V-uri urmeaza textul. ', end=" ")

    sleep(3)





semne_aleatoare_in = input('Transmisie de text cu semne aleatoare ? (NU = n+Enter / DA = ENTER): ')
semne_aleatoare_in = semne_aleatoare_in.lower()  # raspunsul este transformat in litere mici pentru comparatie

if semne_aleatoare_in != 'n':
    semne_aleatoare = True

    lungime_text_aleator = int(input('Numarul de semne ale textului aleator (1 - 50) : '))
    while lungime_text_aleator > 50:
        print('Textul depaseste 50 de semne.')
        lungime_text_aleator = int(input('Numarul de semne ale textului aleator (1 - 50) : '))

if semne_aleatoare_in == 'n':
    semne_aleatoare_in = input('Transmisie cu text predefinit ? (NU = n+Enter / DA = ENTER): ')
    if semne_aleatoare_in != 'n':
        semne_aleatoare = False
    else :
        semne_aleatoare = True
        d = 'n'


while d != 'n':

    if d != 'n':

        if semne_aleatoare == False:
            text = input('Scrie textul de transmis : ')
            text = text.lower()  # textul de transmis este transfoarmat in litere mici pentru comparatie
            jj = len(text)
            if jj > 250:
                print('Textul este mai lung de 250')
            else:
                print(f'Textul are ', jj, " semne")

        if semne_aleatoare == False:
            serieV()
            for iii in range(3):
                cheie = 'v'
                cm = '1113'
                transmisie()

            print()

            for ii in range(jj):
                cheie = text[ii]
                sleep(slp2)

                for key, semnal in semne.items():

                    if cheie == key:
                        cm = semnal


                        memorare()
                        transmisie()


        if semne_aleatoare == True:
            serieV()
            for iii in range(3):
                cheie = 'v'
                cm = '1113'
                transmisie()
            print()

            for iiii in range(lungime_text_aleator):

                aleator = random.randint(0, len(semne) - 1)  # se genereaza o valoare pseudoaleatoare
                cheie = list(semne.keys())[aleator]  # se identifica cheia din dict cu numarul echivalent celui aleator si se atribuie valoarea variabilei cheie.
                sleep(slp2)
                for key, semnal in semne.items():  # se identifica valoarea semnal a cheii key din dictul semne
                    if cheie == key:  # se compara variabila cheie cu key
                        cm = semnal  # se atribuie valoarea semnal variabilei cm
                        memorare()  # se apeleaza functia memorare

                        transmisie()  # se apeleaza functia transmisie


        while dd != 'n':
            print()
            dd = input('Doresti retransmisia textului ? (NU = n+Enter / DA = ENTER): ')
            dd = dd.lower()  # raspunsul este transformat in litere mici pentru comparatie
            if dd != 'n':
                spatiu = 0
                serieV()
                for iii in range(3):
                    cheie = 'v'
                    cm = '1113'
                    transmisie()
                print()
                for l in range(len(cheie_memorata)):
                    sleep(slp2)
                    cheie = cheie_memorata[l]
                    cm = cm_memorat[l]

                    transmisie()
        cheie_memorata=[]
        cm_memorat = []
        dd = 'd'

    d = input('Doresti transmisia unui alt text ? (NU = n+Enter / DA = ENTER): ')
    d = d.lower()  # raspunsul este transformat in litere mici pentru comparatie


    if d == 'n' and semne_aleatoare==True:
        d = input('Doresti transmisie de text predefinit ? : ')
        if d !='n' :
            d = 'd'
            semne_aleatoare = not semne_aleatoare


    if d == 'n' and semne_aleatoare==False:
        d = input('Doresti transmisie de text aleator ? : ')
        if d !='n' :
            d = 'd'
            semne_aleatoare = not semne_aleatoare


    if d != 'n' and semne_aleatoare == True :
        lungime_text_aleator = int(input('Numarul de semne ale textului aleator (1 - 50) : '))
        while lungime_text_aleator > 50:
            print('Textul depaseste 50 de semne.')
            lungime_text_aleator = int(input('Numarul de semne ale textului aleator (1 - 50) : '))