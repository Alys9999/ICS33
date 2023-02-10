import goody

def read_fa(open_file : open) -> {str:{str:str}}:
    fa = dict()
    for line in open_file:
        desc = line.strip().split(';')
        fa[desc[0]] = dict(zip(desc[1::2],desc[2::2]))
    open_file.close()
    return fa


def fa_as_str(fa : {str:{str:str}}) -> str:
#     answer = ''
#     for s in sorted(fa):
#         answer += '  '+s+' transitions: '+str(sorted(fa[s].items()))+'\n'
#     return answer
    return '\n'.join('  '+s+' transitions: '+str(sorted(fa[s].items())) for s in sorted(fa))+'\n'
    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    result =[state]
    for i in inputs:
        if i not in fa[state]:
            result.append((i,None))
            return result
        else:
            state = fa[state][i]
            result.append((i,state))
    return result


def interpret(fa_result : [None]) -> str:
    answer = 'Start state = '+fa_result[0]+'\n'
    for i in fa_result[1:]:
        answer += '  Input = '+i[0]+'; '
        if i[1] != None:
            answer += 'new state = '+i[1]+'\n'
        else:
            answer += 'illegal input: simulation terminated\n'
    answer += 'Stop state = '+str(fa_result[-1][1])+'\n'
    return answer





if __name__ == '__main__':
    fa = read_fa(goody.safe_open('Enter file with finite automaton', 'r', 'Could not find that file'))
    print('\nFinite Automaton Description\n'+fa_as_str(fa))
    data = goody.safe_open('Enter file with start-states and inputs', 'r', 'Could not find that file')
    for line in data:
        print('\nStarting new simulation')
        desc = line.strip().split(';')
        print(interpret(process(fa,desc[0],desc[1:])),end='')
    data.close()
              
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
