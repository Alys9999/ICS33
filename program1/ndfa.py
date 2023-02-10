import goody


def read_ndfa(file : open) -> {str:{str:{str}}}:
    main_d={}
    s_main_d={}
    with open(file.name) as open_file:
        for line in open_file:
            main_set=set()
            line=line.rstrip().split(';')
            pair_d={}
            main_set=set()
            if len(line)==1:
                main_d[line[0]]={}
            for x in range(1,len(line)-1,2):
                if line[x] in pair_d.keys():
                    stored=pair_d[line[x]]
                    stored.add(line[x+1])
                    pair_d[line[x]]=stored
                else:
                    item=line[x+1]
                    pair_set={item,}
                    pair_d[line[x]]=pair_set
                main_d[line[0]]=pair_d
    return main_d

def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    s=''
    for x in sorted(ndfa.keys()):
        li=[]
        if len(ndfa[x])!=0:
            for y in sorted(ndfa[x].keys()):
               tu=(y,sorted(list(ndfa[x][y])))
               li.append(tu)
            li=sorted(li)
            s+='  '+str(x)+' transitions: '+str(li)+'\n'
        else:
            s+='  '+str(x)+ ' transitions: ' + '[]\n'
    print(s)
    return s

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    re_li=[state]
    possible_states=[state]
    for i in range(len(inputs)):
        current_states=set()
        for s in possible_states:
            try:
                for x in ndfa[s][inputs[i]]:
                    current_states.add(x)
            except KeyError:
                pass
        possible_states=list(sorted(current_states))
        re_li.append((inputs[i],current_states))
        if current_states==set():
            break
    return re_li


def interpret(result : [None]) -> str:
    s=''
    s+='Start state = '+result[0]+'\n'
    for x in range(1,len(result)):
        pair=result[x]
        s+='  Input = '+str(pair[0])+'; new possible states = '+str(sorted(list(pair[1])))+'\n'
    s+='Stop state(s) = '+str(sorted(list(result[x][1])))+'\n'
    print(s)
    return s




if __name__ == '__main__':
    # Write script here
    #print(read_ndfa(open('ndfaendin01.txt')))
    #ndfa1 = {'end': {}, 'start': {'1': {'start'}, '0': {'start', 'near'}}, 'near': {'1': {'end'}}}
    #ndfa2 = {'pass1': {'p': {'pass2'}, 'd': {'rest'}}, 'pass2': {'p': {'pass3'}, 'd': {'rest'}}, 'start': {'e': {'engine'}}, 'pass3': {'p': {'pass4'}, 'd': {'rest'}}, 'engine': {'e': {'engine', 'rest'}}, 'pass4': {'d': {'rest'}}, 'box1': {'b': {'rest'}}, 'rest': {'p': {'pass1'}, 'b': {'box1'}, 'c': {'done'}}}
    #ndfa_as_str(ndfa1)
    #"  end transitions: []\n  near transitions: [('1', ['end'])]\n  start transitions: [('0', ['near', 'start']), ('1', ['start'])]\n"
    #process(ndfa2,'start','e;e;e;b;p;p;d;c'.split(';'))    
    #process(ndfa1,'start','1;0;1;1;0;1'.split(';'))
    #i = ['start', ('1', {'start'}), ('0', {'start', 'near'}), ('1', {'end', 'start'}), ('1', {'start'}), ('0', {'start', 'near'}), ('1', {'end', 'start'})]
    #interpret(i)
    nd_file = goody.safe_open('Select a file storing a Non-Deterministic Finite Automaton','r','Illegal file name')
    print('Non-Determinisitc Finite Automaton: sorted states (str) and sorted lists of transitions [(str,[str])]')
    ndfa_d=read_ndfa(nd_file)
    ndfa_as_str(ndfa_d)
    print()
    ndinput_file=goody.safe_open('Select a file with each line showing a start-state and its inputs','r','Illegal file name')
    print()
    print('Calculated trace of NDFA from its start-state')
    with open(ndinput_file.name) as open_file:
        for line in open_file:
            line=line.rstrip().split(';')
            p=process(ndfa_d,line[0],line[1:])
            interpret(p)

    
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
