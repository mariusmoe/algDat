from sys import *
import traceback

def subgraftetthet(nabomatrise, startnode):
    n = len(nabomatrise)
    visited = []
    bug = False
    
    kanter = 0.0

    can = []
    for o in range(n):
            current = nabomatrise[startnode][o]
            if current == True:
                can.append(o)
                kanter +=1
    #visited.append(current)
    
    #noder = 0
    #sdfsdfs
    #oooooo
    kant2=0
    
    noder = n
    while len(can)!=0:
        row = can.pop()
        #while row in visited and len(can)!=0:
         #   row = can.pop()
            
        for i in range(n):
            current = nabomatrise[row][i]
            if current == True and i not in visited:
                if bug:
                    print "rad: ", row
                can.append(i)
                kanter += 1
                
        visited.append(row)
        if bug:print "kanter ooo: ", kanter
        
        
    count=0
    for u in range(n):
        for w in range(n):
            if nabomatrise[u][w] == True:
                count +=1
    
    #kanter = count-kanter     
    """           
    for i in range(startnode,n):
        for m in range(n):
            print nabomatrise[i][m]
            if nabomatrise[i][m] == True:
                visited.append(nabomatrise[i][m])
        print "---------------------------new row"
    """
    if bug:
            
        #noder=n-len(visited)
        print "count: ", count
        print "kanter: ",kanter
        print "noder: ", noder
        print "visited: ", visited
        
        print "-------------"
        print "noder i subgrafen: ", noder
    S = set(visited)
    noder = n-len(S)-1
        
    if noder == 1:
        noder = 0
   
    
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