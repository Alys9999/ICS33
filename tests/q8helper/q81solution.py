from random import randrange
import random
from influence import find_influencers
from goody import irange
from performance import Performance

def random_graph (nodes : int, edges : int) -> {str:{str}}:
    g = {str(n) :set() for n in range(nodes)}
    
    for i in range(int(edges)):
        n1 = str(randrange(nodes))
        n2 = str(randrange(nodes))
        if n1 != n2 and n1 in g and n2 not in g[n1]:
            g[n1].add(n2)
            g[n2].add(n1)
    return g


# Put the code here to generate data for Quiz 8 problem #1
for i in range(8):
    size = 100 * 2**i
    rg=random_graph(size,5*size)
    p = Performance(lambda: find_influencers(rg),title=f'\n\nFinding inflencer for graph with {size} size')
    p.evaluate()
    try:
        p.analyze()
    except ValueError:
        print(f"\n\nFinding inflencer for graph with {size} size\nAnalysis of 5 timings\n0 time-elapsed; cannot show analysis")
