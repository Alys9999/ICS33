import prompt
from goody       import safe_open
from math        import ceil 
from collections import defaultdict


def read_graph(open_file : open) -> {str:{str}}:
    graph = defaultdict(set)
    for line in open_file:
        if ';' not in line:
            if line not in graph:
                graph[line] = set()
        else:
            s,d = line.rstrip().split(';')
            graph[s].add(d)
            graph[d].add(s)
    open_file.close()
    return graph


def graph_as_str(graph : {str:{str}}) -> str:
#     answer =''
#     for s,d in sorted(graph.items()):
#         answer += '  '+s+' -> '+str(sorted(d))+'\n'
#     return answer
    return '\n'.join('  '+s+' -> '+str(sorted(d)) for s,d in sorted(graph.items()))+'\n'


def find_influencers(graph : {str:{str}}, trace : bool = False) -> {str}:
    infl_dict = {v:[len(friends)-ceil(len(friends)*.5) if len(friends) != 0 else -1, len(friends),v] for v,friends in graph.items()}
    while True:
        remove_candidates = [(dist,friends,v) for (dist,friends,v) in infl_dict.values() if dist >= 0]
        if trace: print('influencer dictionary =',infl_dict, '\nremoval candidates    =',remove_candidates)
        if remove_candidates == []:
            return set(infl_dict)
        d,f,v =min(remove_candidates)
        if trace: print((d,f,v),'is the smallest candidate\nRemoving',v,'as key from influencer dictionary; decrementing friend\'s values there\n')
        del infl_dict[v]
        for f in graph[v]:
            if f in infl_dict:
                infl_dict[f][0] -= 1
                infl_dict[f][1] -= 1


def all_influenced(graph : {str:{str}}, influencers : {str}) -> {str}:
    influenced_dict = {v:(v in influencers) for v in graph.keys()}
    influenced_num  = len(influencers)
    while True:
        for v,i in influenced_dict.items():
            if not i:
                if len(graph[v]) != 0 and sum(influenced_dict[f] for f in graph[v]) >= ceil(len(graph[v])*.5):
                    influenced_dict[v] = True
        old_influenced, influenced_num = influenced_num, sum(i for i in influenced_dict.values())
        if influenced_num == old_influenced:
            return set(v for v in influenced_dict if influenced_dict[v])
       
            
    
if __name__ == '__main__':
    graph_file = safe_open('Enter a file storing a friendship graph', 'r', 'Could not find that file',default='graph1.txt')
    graph = read_graph(graph_file)
    print('Graph: node -> list of all friend nodes\n' + graph_as_str(graph))
    
    influencers = find_influencers(graph,prompt.for_bool('Trace the Algorithm',default=True))
    print('Influencers =', influencers)
    
    while True:
        influencer_set = prompt.for_string('\nEnter influencers set (or else quit)', default=str(influencers), is_legal = lambda core : core == 'quit' or all(c in graph for c in eval(core)))
        if influencer_set == 'quit':
            break;
        influenced = all_influenced(graph,eval(influencer_set))
        print('All Influenced ('+str(100*len(influenced)/len(graph))+'% of graph)=',influenced,'\n')
            
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
