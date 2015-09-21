from sys import stdin


class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt 
        self.neste = None 

def spor(kubbe):

    # SKRIV DIN KODE HER
    biggest_weight = -1
    while kubbe != None:
        if kubbe.vekt > biggest_weight:
            biggest_weight = kubbe.vekt
        kubbe = kubbe.neste
    return biggest_weight

# Oppretter lenket liste
forste = None
siste = None
for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste

# Kaller loesningsfunksjonen og skriver ut resultatet

print (spor(forste))


#moe@moe-ENVY:~/workspace/AlgDat/test$ python3.4 dynamitt_2.py < input.txt

