from sys import stdin, stderr
import traceback
from collections import defaultdict
from collections import deque


class Node:
    def __init__(self):
        self.barn = defaultdict(Node)
        self.bar = []
        self.posi = []



def bygg(ordliste):
    
    node = Node()
    pos = deque()
    di=defaultdict(Node)
    for k, v in ordliste:
        di[k].barn =(v) #burde ikke trenge denne
        pos.append(v)
       
    current_node = node
    for word in ord:
        length = len(word)
        for i in xrange(length):    
            current_node = current_node.barn[word[i]]
            #current_node.bar.append(word[i])
            if (i+1)==len(word):
                current_node.posi.append(pos.popleft())            
        current_node = node
            
    return node

def posisjoner(ord, indeks, node):
    
    res = []
    word = sokeord
    bug = True
    bug = False
    se = set()
    ub=[]

    def pas(ord, indeks, node):
        current_node = node
        for i in range(indeks,len(ord)):
            if  bug:
                print " "
                print "i: ", i, " - search: ", ord, " /indeks: ", indeks
            
            if ord[i] == '?':
                temp=i
                if bug:
                    print " ? "
                #en referansenode slik at en kan starte paa denne igjen
                secret_node = current_node
                for k in secret_node.barn:
                    if bug:
                        print secret_node.barn
                        print "k: ", k
                    #gjor om current_node til et av barna til forige node
                    #current_node = current_node.barn[k]
                    
                    current_node = secret_node.barn[k]
                    indeks=temp
                    
                    #trengs kanskje ikke
                    if i==len(ord)-1:
                        res.extend(current_node.posi)
                    
                    pas(ord[:indeks] + '?' + ord[indeks+1:], indeks+1, current_node)
            else:
                if ord[i] in current_node.barn:
                    #print current_node.barn[ord[i]].barn
                    current_node = current_node.barn[ord[i]]
                #hvis denne testen er bedre...
                else:
                    se =set(res)
                    ub=list(se)
                    return ub
                if i==len(ord)-1:
                    res.extend(current_node.posi)
                    if bug:
                        print "appended: " , res
                
        se=set(res)
        
        ub=list(se)
        if bug:
            print "----------------------------------------"    
        return ub
                   
    return pas(ord, indeks, node)
    

try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o,pos) )
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
except:
    traceback.print_exc(file=stderr)
  
    