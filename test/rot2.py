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
    level = 0
    S=[rot]
   
    while S:
     
        current_node=S[-1]
        
        if current_node.ratatosk == True:
                return len(S) - 1
        
        if current_node.nesteBarn == len(current_node.barn):
            S.pop()
            level = level+1
        else:
            S.append(current_node.barn[current_node.nesteBarn])
            current_node.nesteBarn +=1


        

def bfs(rot):

    
    pass

    
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