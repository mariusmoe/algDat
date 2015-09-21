from sys import stdin
import time


# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner


class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0

def dfs(rot):
    level = 1
    li=[]
    #levelAnt=0
    lant=[]
    S=[]
    S.extend(rot.barn)
    while len(S) != 0:

        current_node=S[-1]

        if current_node.ratatosk:
                return level
        if len(current_node.barn) > 0:
            S.extend(current_node.barn)
            level = level+1
            antILevel=len(current_node.barn)
            li.append(antILevel)
        else:
            S.pop()
            #levelAnt +=1
            try:
                lant.append(lant[-1]+1)
            except Exception:
                lant.append(1)
            try:
                if lant[-1]==li[-1]:
                    level -=1
                    S.pop()
                    li.pop()
                    lant.pop()
    
            except Exception:
                pass

def bfs(rot):
    level = 1
    stak=[] #hovedlisten min - den jeg faktisk soker igjenom
    stak.extend(rot.barn)   #legger til de forste barna
    print(stak)
    st=[]   #buffer liste
    while len(stak) != 0:   #saa lenge jeg har noe aa gjore
        for node in stak:
            if node.ratatosk:   #sjekker om ratatosk er i den noden jeg er i 
               return level
            elif len(node.barn) > 0:    #hvis noden jeg ser paa har barn saa legg disse til i buffer listen min
                st.extend(node.barn)
        stak[:] = []    #tommar stak - listen jeg soker gjennom
        stak.extend(st) #legger til de jeg fant i buffer listen min til hovedlisten min
        level += 1
   
    # SKRIV DIN KODE HER
def main():
    funksjon = stdin.readline().strip()
    antall_noder = int(stdin.readline())
    noder = []
    for i in range(antall_noder):
        noder.append(Node())
    start_node = noder[int(stdin.readline())]
    ratatosk_node = noder[int(stdin.readline())]
    ratatosk_node.ratatosk = True
    for linje in stdin:
        tall = linje.split()
        temp_node = noder[int(tall.pop(0))]
        for barn_nr in tall:
            temp_node.barn.append(noder[int(barn_nr)])

    if funksjon == 'dfs':
        print(noder)
        print(temp_node)
        print (dfs(start_node))
    elif funksjon == 'bfs':
        print (bfs(start_node))
    elif funksjon == 'velg':
        pass
    
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))