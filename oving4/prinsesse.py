from sys import *
import traceback

def subgraftetthet(nabomatrise, startnode):
    n = len(nabomatrise)
    visited = []
<<<<<<< HEAD
    can = []
    
    #noder = 0
    #sdfsdfs
    #oooooo
    for o in range(n):
        current = nabomatrise[startnode][o]
        if current == True:
            can.append(current)
            
            
            
            
            
            
            
            
            
            
            
            
            
=======
    #noder = 0
>>>>>>> 6d06eb627f0690ba968dcabe0147fb2f44474b83
    
    for i in range(startnode,n):
        for m in range(n):
            print nabomatrise[i][m]
            if nabomatrise[i][m] == True:
                visited.append(nabomatrise[i][m])
        print "---------------------------new row"
    noder=n-len(visited)
    if noder == 0:
        return 0.0
    else:
        return float(kanter) / float(noder**2)


try:
    n = int(stdin.readline())
    nabomatrise = [None] * n # rader
    for i in range(0, n):
        nabomatrise[i] = [False] * n # kolonner
        linje = stdin.readline()
        for j in range(0, n):
            nabomatrise[i][j] = (linje[j] == '1')
    for linje in stdin:
        start = int(linje)
        print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
except:
    traceback.print_exc(file=stderr)