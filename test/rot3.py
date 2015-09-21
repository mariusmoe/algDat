from sys import stdin



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
    AntAtLevel=[]
    lant=[]
    S=[]
    S.extend(rot.barn)
    if rot.ratatosk:
        return level-1
    while len(S) != 0:

        current_node=S[-1]

        if current_node.ratatosk:
                return level
        if len(current_node.barn) > 0:
            S.extend(current_node.barn)
            level = level+1
            antILevel=len(current_node.barn)
            AntAtLevel.append(antILevel)
        else:
            S.pop()

            try:
                lant.append(lant[-1]+1)
            except Exception:
                lant.append(1)
            try:
                if lant[-1]==li[-1]:
                    level -=1
                    S.pop()
                    AntAtLevel.pop()
                    lant.pop()
    
            except Exception:
                pass

def bfs(rot):
   """ level = 1
    stak=[]
    stak.extend(rot.barn)
    st=[]
    if rot.ratatosk:
        return level-1
    while len(stak) != 0:
        for node in stak:
            if node.ratatosk:
               return level
            elif len(node.barn) > 0:
                st.extend(node.barn)
        stak[:] = []    
        stak.extend(st)
        level += 1
   """
   pass
    # SKRIV DIN KODE HER

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
    print (dfs(start_node))
elif funksjon == 'bfs':
    print (bfs(start_node))
elif funksjon == 'velg':
    print (bfs(start_node))

    


