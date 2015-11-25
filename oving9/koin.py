from sys import stdin
import copy

def minCoinsGreedy(coins, value):
    #print("coins: ", coins)
    #print("value: ", value)
    new_coins = copy.copy(coins)
    antMynt = 0
    amount = 0
    while amount<value:
        if new_coins[0] <= value-amount and new_coins[0]!=1:
            amount += new_coins[0]
            #new_coins.pop(0)
            antMynt += 1
        elif new_coins[0]==1:
            amount += 1
            antMynt +=1
        else:
            new_coins.pop(0)
    #print("antMynt: ", antMynt)
    return antMynt

def minCoinsDynamic(coins, value):
    # SKRIV DIN KODE HER
    return null

def canUseGreedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut 
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER
	return false

Inf = 1000000000
coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
    for line in stdin:
        print(minCoinsGreedy(coins, int(line)))
else:
    for line in stdin:
        print(minCoinsDynamic(coins, int(line)))
        #husk å fjerne ekstra paranteser