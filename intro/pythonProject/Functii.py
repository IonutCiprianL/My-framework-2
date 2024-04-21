def printGreeting():
    print('Buna ziua!')

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume} !')

def mediaNr(a, b, c):
    return (a + b+ c)/3

def piValue():
    return 3.14

# exercitiu
# daca numarul e pozitiv returnati true, altfel false
def verificareMajor(varsta):
    if varsta>=18:
        return True
    else:
        return False

# zona de apelare (desktop)
printGreeting()
printGreeting()
printGreetingByName('Petre', 'Dan')
printGreetingByName('Onu', 'Ana')
printGreetingByName('Ion', 'Ion')

# zona de apelre (desktop)
printGreeting()
printGreeting()

print(mediaNr(3,3,4))
print(piValue())
print(verificareMajor(18))


# se ia varsta utilizatorului
age = int(input('introduceti varsta dvs'))
if verificareMajor(age):
    print('Cont creat. Bina ai venit in aplicatie')
else:
    print('Nu ai varsta minima necesara (18 ani) pentru a paria')

    