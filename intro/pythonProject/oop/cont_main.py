from oop.cont_bancar import ContBancar
cont1 =ContBancar('Ana ',' Ro001')
cont2 =ContBancar('Dan ',' Ro002')

cont1.activareCont(7777)
cont1.alimentareCont(300)
cont1.interogareSold()

cont2.activareCont(3333)
cont2.activareCont(7777)
cont2.alimentareCont(700)
cont2.alimentareCont(300)
cont2.interogareSold()