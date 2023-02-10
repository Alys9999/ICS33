import goody


def read_fa(file : open) -> {str:{str:str}}:
    fa_d={}
    with open(file.name) as open_file:
        for line in open_file:
            pair_d={}
            line=line.rstrip().split(';')
            for x in range(1,len(line)-1,2):
                pair_d[str(line[x])]=str(line[x+1])
            fa_d[str(line[0])]=pair_d
    return fa_d


def fa_as_str(fa : {str:{str:str}}) -> str:
    s=''
    for x in sorted(fa.keys()):
        li=[]
        for y in sorted(fa[x].keys()):
            tu=(y,fa[x][y])
            li.append(tu)
        s+="  "+str(x)+" transitions: " + str(li)+"\n"
    print(s)
    return s
    

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    re_li=[state]
    x=fa[state]
    for y in inputs:
        try:
            st=x[y]
            tu=(str(y),str(st))
            re_li.append(tu)
            x=fa[st]
        except KeyError:
            tu=(str(y),None)
            re_li.append(tu)
    return re_li
    


def interpret(fa_result : [None]) -> str:
    s=''
    s+='Start state = '+fa_result[0]+'\n'
    for x in range(1,len(fa_result)):
        st=fa_result[x][1]
        if st==None:
            s+='  Input = '+ str(fa_result[x][0])+'; illegal input: simulation terminated\n'
        else:
            s+='  Input = '+ str(fa_result[x][0])+'; new state = ' +str(st)+'\n'
    s+='Stop state = '+ str(st)+'\n'
    print(s)
    return s
    




if __name__ == '__main__':
    # Write script here
    #fa1 = {'odd': {'1': 'even', '0': 'odd'}, 'even': {'1': 'odd', '0': 'even'}}
    #fa_as_str(fa1)
    #read_fa(open('faparity.txt'))
    #fa1 = {'odd': {'1': 'even', '0': 'odd'}, 'even': {'1': 'odd', '0': 'even'}}
    #process(fa1,'even','1;0;1;1;0;x'.split(';'))
    #i = ['even', ('1', 'odd'), ('0', 'odd'), ('1', 'even'), ('1', 'odd'), ('0', 'odd'), ('1', 'even')]
    #interpret(i)
    f_file = goody.safe_open('Select a file storing the Finite Automaton','r','Illegal file name')
    print('  Finite Automaton: sorted states (str) and sorted lists of transitions [(str,str)]')
    ff_d=read_fa(f_file)
    fa_as_str(ff_d)
    print()
    s_file= goody.safe_open(' Select a file with each line showing a start-state and its inputs','r','Illegal file name')
    print('  Calculated trace of FA from its start-state')
    with open(s_file.name) as open_file:
        for line in open_file:
            line=line.rstrip().split(';')
            p=process(ff_d,line[0],line[1:])
            interpret(p)
    
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
