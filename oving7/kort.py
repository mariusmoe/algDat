from sys import stdin
from itertools import repeat

def merge(decks):
    # SKRIV DIN KODE HER
    bug = True
    
    def merge1(decks):
        li = []
        try:
            while decks[0]:    
                big, letter, pointer, counter = 0, '', 0, 0
                for lists in decks:
                    try:
                        if lists[-1][0] > big:
                            big = lists[-1][0]
                            letter = lists[-1][1]
                            pointer = counter
                        counter +=1 
                        if bug:
                            print lists[-1][0]
                    except:
                        pass
               
                if not decks[pointer]:
                    decks.pop(pointer)    
                li.append(letter)
                decks[pointer].pop()
               
                
            if bug:
                print li
                print "#######"
            li.reverse()
            if bug:
                print li
            #print decks
            return li
        except:
            return li
                    
                    
        
            
    
    
    return ''.join(merge1(decks))
    
    
    
    
    
    
    
    
    
   
   
decks = []
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    decks.append(deck)
print merge(decks)