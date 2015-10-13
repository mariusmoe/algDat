from sys import stdin
#from collections import deque
from heapq import heappop, heappush
#from collections import defaultdict
import copy

Inf = float(1e3000)
False = 0
True = 1

def mst(nm):
    # SKRIV DIN KODE HER
    #take the shortest road, take the shortest road
    # if it maks a sycle dropit and take the shortest road

    #Denne implementasjonen av prim's algoritme er hentet fra
    #Apress Magnus Lie Hetland Python Algorithms
    #-----------------------------------------------------
    def prim(G, s):
        P, Q = {}, [(0, None, s)]
        while Q:
            _, p, u = heappop(Q)
            if u in P: continue
            P[u] = p
            for v, w in G[u].items():
                heappush(Q, (w, u, v))
        return P
    #-----------------------------------------------------
    
    
    #++++++++++++++++++++++++++++++++++++++++++++++++++++
    """
    def prim2(G,s):
        P = {}
        Q = []
        
        for u in G.items():
            u.key = 9999
            u.pi = None
        s.key = 0
        Q = G.items()
        while Q:
            u = #extract-min(Q)
            for v in G[u].items():
                if v in Q and w(u,v) < v.key:
                    v.pi = u
                    v.key = w(u,v)
    
    """
    #++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    
        
    si = prim(nm,0)
    so =[]
    
    #gaar veien som er funnet og legger til vekten i en liste
    for k, v in si.items():
        if v != None:
            so.append(nabomatrise[v][k])
    
    #so.max()       # finnes det en raskere metode?
    
    return max(so)

no=[]
di = dict()
linjer = []
for str in stdin:
    linjer.append(str)
n = len(linjer)
nabomatrise = [None] * n
node = 0
for linje in linjer:
    nabomatrise[node] = [Inf] * n

    for k in linje.split():
        data = k.split(':')
        nabo = int(data[0])
        vekt = int(data[1])
        nabomatrise[node][nabo] = vekt
        di[nabo] = vekt

    no.append(copy.deepcopy(di))
    di.clear()
    node += 1
print mst(no)
