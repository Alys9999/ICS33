import goody
#from collections import defaultdict

def read_ndfa(open_file : open) -> {str:{str:{str}}}:
    ndfa = dict()
    for line in open_file:
        trans = dict() #defaultdict(set)
        desc = line.strip().split(';')
        for (s,d) in zip(desc[1::2],desc[2::2]):
            trans.setdefault(s,set()).add(d) #trans[s].add(d)
        ndfa[desc[0]] = trans
    open_file.close()
    return ndfa


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    answer = ''
    for s in sorted(ndfa):
        answer += '  '+s+' transitions: '+str([(k,sorted(d)) for k,d in sorted(ndfa[s].items())])+'\n'
    return answer

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    result =[state]
    states = set([state])
    for i in inputs:
        # Thanks to a suggestion by Max Kim
#         states = {ns for s in states if i in ndfa[s] for ns in ndfa[s][i]}
#         result.append((i,states))
        new_states = set()
        for s in states:
            if i in ndfa[s]:
                new_states |= ndfa[s][i]
        result.append((i,new_states))
        if new_states == set():
            return result
        states = new_states
    return result


def interpret(result : [None]) -> str:
    answer = 'Start state = '+result[0]+'\n'
    for i in result[1:]:
        answer += '  Input = '+i[0]+'; new possible states = '+ str(sorted(i[1]))+'\n'
    answer += 'Stop state(s) = '+str(sorted(result[-1][1]))+'\n'
    return answer





if __name__ == '__main__':
    ndfa = read_ndfa(goody.safe_open('Enter file with non-deterministic finite automaton', 'r', 'Could not find that file'))
    print('Non-Deterministic Finite Automaton\n'+ndfa_as_str(ndfa))
    data = goody.safe_open('Enter file with start-state and input', 'r', 'Could not find that file')
    for line in data:
        print('\nStarting new simulation')
        desc = line.strip().split(';')
        print(interpret(process(ndfa,desc[0],desc[1:])),end='')
    data.close()
    
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
