from sys import stdin, stderr
import copy
from heapq import heappush, heappop
from itertools import cycle

def beste_sti(nm, sans):
    # SKRIV DIN KODE HER
	debug = False
	
	
	#Denne implementasjonen av bellman'ford algoritme er innspirert av
    #Apress Magnus Lie Hetland Python Algorithms
	def bellman(Graf, s):
		D, Path = {s:0}, {}
		for rnd in Graf:
			changed = False
			for u in Graf:
				for v in Graf[u]:
					if relax(Graf, u, v, D, Path):
						changed = True
			if not changed: break
		else:
			return 0
		return D, Path

	inf = float('inf')
	def relax(W,u,v,D,Path):
		d = D.get(u,inf) + W[u][v]
		if d<D.get(v,inf):
			D[v], Path[v] = d, u 
			return True
			
			
	#----------------------------------------
	def idijkstra(G, s):
		Q, S = [(0,s)], set()
		while Q:
			d, u = heappop(Q)
			if u in S: continue
		S.add(u)
		yield u, d
		for v in G[u]:
			heappush(Q, (d+G[u][v], v))
	
	def bidir_dijkstra(G, s, t):
		Ds, Dt = {}, {}								# D from s and t, respectively
		forw, back = idijkstra(G,s), idijkstra(G,t) # The "two Dijkstras"
		dirs = (Ds, Dt, forw), (Dt, Ds, back)		# Alternating situations
		try:										# Until one of forw/back ends
			for D, other, step in cycle(dirs):		# Switch between the two
				v, d = next(step)					# Next node/distance for one
				D[v] = d							# Remember the distance
				if v in other: break				# Also visited by the other?
		except StopIteration: return inf			# One ran out before they met
		m = inf										# They met; now find the path
		for u in Ds:								# For every visited forw-node
			for v in G[u]:							# ... go through its neighbors
				if not v in Dt: continue			# Is it also back-visited?
				m = min(m, Ds[u] + G[u][v] + Dt[v]) # Is this path better?
		return m
	
	
	
	
	
	#----------------------------------------
	
	
	
	# convert input -> lag Graf og snu sans
	if debug:
		print nm 
		for row in nm:
			print row
		print " null: ", nm[0][0] 
		print sans
	
	for k in range(len(sans)):
		sans[k] = 1-sans[k]
	if debug:
		print "New sans: ", sans
	
	Graf = {}
	di = {}
	for i in range(len(nm[0])):
		for j in range(len(nm[0])):
			if (i!=j and nm[i][j]!=0):
				#print i,j, sans[j], sans[j]*sans[i]
				san = sans[j] #* sans[i]
				#di[j] = sans[j]
				di[j] = san 
		Graf[i] = copy.deepcopy(di)
		di.clear()
	
	debug = True
	if debug:
		print Graf #Graf er klar
		print "G: "
		for key in Graf:
			print key , " : " ,	 Graf[key]
	#Graf,Path = bellman(Graf, 0)
	print "bidir: ", bidir_dijkstra(Graf, 0, 5)
	print "-------------"
	Graf,Path = bellman(Graf, 0)
	#print Graf,Path
	
	s = n-1		#sisste node i grafen
	li = [s]		#liste med svar
	while s != 0:
		s = Path[s]
		li.append(s)
	li.reverse()
	if debug:
		print li
	sum_av_vei = 1
	for tall in li:
		if sans[tall]!=0:
			sum_av_vei = sum_av_vei* sans[tall]
	
	if sum_av_vei >= 0.9999:
		return '0' 
	if debug:
		print "sum_av_vei: ",sum_av_vei
	li = map(str, li)
	return '-'.join(li)
	
	
	#call and return bellman_ford(Graf, s)
	
	
	
		
	

n = int(stdin.readline())
sannsynligheter = [float(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [0] * n
    naboer = [int(nabo) for nabo in linje.split()]
    for nabo in naboer:
        naborad[nabo] = 1
    nabomatrise.append(naborad)
print beste_sti(nabomatrise, sannsynligheter)