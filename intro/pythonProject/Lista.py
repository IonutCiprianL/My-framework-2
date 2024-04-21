

# listele in Py pot sa cuprinda elemente de tipuri diferite
# au diensiune dinamica

fructe = ['mar', 'banana','portocala', 3, True, 3]
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adaugam un nou element
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'para'

# afisam lista
print(fructe)

# aflam dimensiunea
print(len(fructe))

# scoate si ne returneaza ultimul element
last = fructe.pop()
print('ultimul element : ', last)
print('lista : ', fructe)

# de cate ori apare un element
print(fructe.count(3))

# adaugam o lista la alta lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)

