from sys import stdin, stderr
import copy


def beste_sti(nm, sans):
	til_sans = [0.0] * n
	til_sans[0], sjekket = sans[0],  [False] * n
	beste_forige_node = [a for a in range(n)]
	beste_node, bug = 0 , False
	if bug:	
		print "to_prob" , til_sans
		print "processed", sjekket
		print beste_node
	for i in xrange(n):
		node = beste_node
		sjekket[node], storst_til_sans = True, 0.0
		for nabo in xrange(n):
			if not (sjekket[nabo]):
				if nm[node][nabo]:
					ny_sans = (til_sans[node] * sans[nabo])
					if ny_sans > til_sans[nabo]:
						beste_forige_node[nabo] = node
						til_sans[nabo] = ny_sans
				if til_sans[nabo] > storst_til_sans:
					beste_node = nabo
					storst_til_sans = til_sans[nabo]
					
	if til_sans[-1] == 0.0:
		return 0
	index = n-1
	P=[index]
	#---------------------------------------------------
	di={}
	Graf = {}
	for i in range(len(nm[0])):
		for j in range(len(nm[0])):
			if (i!=j and nm[i][j]!=0):
				#print i,j, sans[j], sans[j]*sans[i]
				san = sans[j] #* sans[i]
				#di[j] = sans[j]
				di[j] = san 
		Graf[i] = copy.deepcopy(di)
		di.clear()
		
	while index!=0:
		index = beste_forige_node[index]
		P.append(index)
	
	return '-'.join(map(str, reversed(P)))












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