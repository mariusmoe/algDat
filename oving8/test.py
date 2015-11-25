from sys import stdin, stderr

def beste_path(nm, prob):
    to_prob = [0.0] * n
    to_prob[0] = prob[0]
    processed = [False] * n
    best_prev_node = [a for a in range(n)]
    best_node = 0

    for i in range(n):
        node = best_node
        processed[node] = True
        highest_to_prob = 0.0

        for nabo in range(n):
            if not processed[nabo]:
                if nm[node][nabo]:
                    new_prob = to_prob[node] * prob[nabo]

                    if new_prob > to_prob[nabo]:
                        best_prev_node[nabo] = node
                        to_prob[nabo] = new_prob

                if to_prob[nabo] > highest_to_prob:
                    best_node = nabo
                    highest_to_prob = to_prob[nabo]

    if to_prob[-1] == 0.0:
        return 0

    index = n - 1
    path = [index]

    while index != 0:
        index = best_prev_node[index]
        path.append(index)
    return '-'.join(map(str, reversed(path)))

n = int(stdin.readline())
sannsynligheter = [float(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [0] * n
    naboer = [int(nabo) for nabo in linje.split()]
    for nabo in naboer:
        naborad[nabo] = 1
    nabomatrise.append(naborad)
print(beste_path(nabomatrise, sannsynligheter))