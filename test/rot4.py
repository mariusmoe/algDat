from sys import stdin

import collections

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
    S=collections.deque()
    S.extend(rot.barn)
    st=collections.deque()
    st.append(len(rot.barn)) 
    if rot.ratatosk:
        return 0
    while len(S) != 0:
        current_node=S[-1]
        if current_node.ratatosk:
                return len(st)
        if len(current_node.barn) > 0:
            S.extend(current_node.barn)
            st.append(len(current_node.barn))
        else:
            S.pop()
            st[-1] = int(st[-1]) - 1
            try:
                if st[-1] == 0:
                    S.pop()
                    st.pop()
                    st[-1] = int(st[-1]) - 1                
            except Exception:
                pass
            
def bfs(rot):
    level = 1
    stak=collections.deque()
    stak.extend(rot.barn)
    st= collections.deque()
    if rot.ratatosk:
        return level-1
    while len(stak) != 0:
        for node in stak:
            if node.ratatosk:
               return level
            elif len(node.barn) > 0:
                st.extend(node.barn)
        stak.clear()    
        stak.extend(st)
        level += 1
   

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